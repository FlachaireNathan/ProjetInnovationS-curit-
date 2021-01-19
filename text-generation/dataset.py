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


	def load_words(self, nameFile, separator):

		nbWords = 10000

		passwords = []
		passwordsToReturn = []
		f = open(nameFile, "r")
		for line in f: 
			passwords.append(line)
		random.shuffle(passwords)
		
		# Select x number of password from the coprus randomly
		for i in range(nbWords):
			for j in range(len(passwords[i])):
				if (passwords[i][j] != "\n"):
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