import torch
import pandas as pd
from collections import Counter
import random

class Dataset(torch.utils.data.Dataset):
	def __init__(
			self,
			args,
	):
			self.args = args
			self.words = self.load_words("data/train.txt", "\n")
			
			self.uniq_words = self.get_uniq_words()

			self.index_to_word = {index: word for index, word in enumerate(self.uniq_words)}
			self.word_to_index = {word: index for index, word in enumerate(self.uniq_words)}

			self.words_indexes = [self.word_to_index[w] for w in self.words]
			

			#print("self.args")
			#print(self.args)

			#print("self.words")
			#print(self.words)

			#print("self.uniq_words")
			#print(self.uniq_words)

			#print("self.index_to_word")
			#print(self.index_to_word)

			#print("self.word_to_index")
			#print(self.word_to_index)

			#print("self.words_indexes")
			#print(self.words_indexes)


	def load_words(self, nameFile, separator):
		passwords = []
		passwordsToReturn = []
		f = open(nameFile, "r") # Charle le fichier dans une variable
		counter = 0
		for line in f: # Pour chaque ligne du fichier
			passwords.append(line)
		random.shuffle(passwords)
		
		for i in range(4000):
			for j in range(len(passwords[i])):
						passwordsToReturn.append(passwords[i][j])
		return passwordsToReturn

	def get_uniq_words(self):
			word_counts = Counter(self.words)
			return sorted(word_counts, key=word_counts.get, reverse=True)

	def __len__(self):
			return len(self.words_indexes) - self.args.sequence_length

	def __getitem__(self, index):
			return (
					torch.tensor(self.words_indexes[index:index+self.args.sequence_length]),
					torch.tensor(self.words_indexes[index+1:index+self.args.sequence_length+1]),
			)