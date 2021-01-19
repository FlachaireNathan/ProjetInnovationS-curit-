import argparse
import torch
import numpy as np
from torch import nn, optim
from torch.utils.data import DataLoader
from model import Model
from dataset import Dataset
import string

def train(dataset, model, args):
	model.train()

	dataloader = DataLoader(dataset, batch_size=args.batch_size)
	criterion = nn.CrossEntropyLoss()
	optimizer = optim.Adam(model.parameters(), lr=0.001)

	for epoch in range(args.max_epochs):
		state_h, state_c = model.init_state(args.sequence_length)

		for batch, (x, y) in enumerate(dataloader):
			optimizer.zero_grad()

			y_pred, (state_h, state_c) = model(x, (state_h, state_c))
			loss = criterion(y_pred.transpose(1, 2), y)

			state_h = state_h.detach()
			state_c = state_c.detach()

			loss.backward()
			optimizer.step()

			print({ 'epoch': epoch, 'batch': batch, 'loss': loss.item() })


def predict(dataset, model, text, next_letters):
	model.eval()

	words = [char for char in text]
	state_h, state_c = model.init_state(len(words))

	for i in range(0, next_letters):
		
		x = torch.tensor([[dataset.word_to_index[w] for w in words[i:]]])
		y_pred, (state_h, state_c) = model(x, (state_h, state_c))

		last_word_logits = y_pred[0][-1]
		p = torch.nn.functional.softmax(last_word_logits, dim=0).detach().numpy()
		word_index = np.random.choice(len(last_word_logits), p=p)
		words.append(dataset.words[word_index])

	return words


def predicts(dataset, model, words):
	words_predicted = []
	for word in words:
		skip = False
		found = False
		for c1 in word[0: 3]:
			for c2 in dataset.word_to_index:
				if (c1 == c2):
					found = True
				if (c1 == "*" or c1 == "," or c1 == "#" or c1 == "-" or c1 == "&" or c1 == "(" or c1 == "[" or c1=="=" or c1=="?"):
					skip = True

		if found == False:
			skip = True

		if (skip == False):
			temp = predict(dataset, model, word[0: 3], len(word)-3)
			#print(word, " => ", temp)
			word_predicted = ""
			for letter in temp:
				word_predicted += letter
			words_predicted.append(temp)
		else:
			words_predicted.append("")
	return words_predicted

def precision(dataset, words_predicted):
	nb_good_predictions = 0
	for word in dataset.words:
		for word_predicted in words_predicted:
			if (word == word_predicted):
				nb_good_predictions += 1
				break
	return nb_good_predictions/len(words_predicted)


parser = argparse.ArgumentParser()
parser.add_argument('--max-epochs', type=int, default=3)
parser.add_argument('--batch-size', type=int, default=128)
parser.add_argument('--sequence-length', type=int, default=4)
args = parser.parse_args()

dataset = Dataset(args)



if torch.cuda.is_available():
	device = torch.device("cpu")
else:
	device = torch.device("cuda:0")

# Train model from scratch
"""
model = Model(dataset).to(device)
train(dataset, model, args)
torch.save(model, "model_train")
"""
# Model class must be defined somewhere

#Load it from saved model file
model = torch.load("model")
model.eval()


# Load test corpus in file and test preditions of the model
f = open("data/test.txt", "r")
test_words = []
for line in f:
	test_words.append(line)

words_predicted = predicts(dataset, model, test_words)

f = open("output.txt", "a")
for i in range(len(test_words)):
	s = ""
	for c in test_words[i]:
		s += c
	s += " => "
	for c in words_predicted[i]:
		s += c
	s += "\n"
	f.write(s)
print("Precision : " , precision(dataset, words_predicted) , "%")
f.write("Precision : " + string(precision(dataset, words_predicted)) + "%")
f.close()
