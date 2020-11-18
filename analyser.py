import matplotlib.pyplot as plt

# Prends en argument le nom du fichier de la base de donnée (extension comprise) ET une liste de séparateurs de mot
# Charge la base de donnée, sépare les mots de passe selon les séparateurs données puis retourne une liste contenant tous les mots de passe
def UploadDataBase(nameFile,separatorList):
	f = open(nameFile, "r") # Charle le fichier dans une variable
	allWord = [] # Prédéfini la liste de mot de passe qu'on retournera
	wordToInsert = "" # variable contenant un mot de passe construit progressivement et qui sera ajouté à la liste de tous les mots de passe
	doSplit = False # variable booléenne pour déterminer si une séparation est faite ou non
	for line in f: # Pour chaque ligne du fichier
		for character in line: # Pour chaque caractère de la ligne
			for separator in separatorList: # Pour chaque séparateur donné en argument, on check s'il correspond au caractère
				if (character == separator): # Si oui, on passe doSplit à true et on arrète la boucle
					doSplit = True
					break
			if (doSplit == True): # Si doSplit est vrai
				if (wordToInsert != ""): # et que wordToInsert n'est pas vide
						allWord.append(wordToInsert) # on ajoute le mot de passe à la liste
						wordToInsert = "" # et on reset wordToInsert pour accueillir un nouveau mot de passe
				doSplit = False # on repasse doSplit à False poour le prochain caractère
			else: # Si doSplit n'est pas vrai
				wordToInsert += character # On ajoute le caractère à wordToInsert
	return allWord

# Renvoie la moyenne de la longueur des mots de la liste donnée en argument (int)
def getMeanOfWordLength(listOfWords):
	nbOfCharactersFromAllWords = 0
	nbWords = len(listOfWords)
	for word in listOfWords:
		nbOfCharactersFromAllWords += len(word)
	return nbOfCharactersFromAllWords/nbWords

# Prends en argument la liste des mots et le caractère
# Renvoie une liste du nombre de mots apparu selon la taille du mot
# L'index est égale à la taille du mots
# La valeur au nombre de mots
def nbOccurenceOfSpecificCharacterByWordLength(listOfWords, character):
	listToReturn = []
	for i in range(0,getBiggestWordLength(listOfWords)+1):
		listToReturn.append(0)
	for word in listOfWords:
		for letter in word:
			if (letter == character):
				listToReturn[len(word)] += 1
	return listToReturn

def getBiggestWordLength(listOfWords):
	biggestLength = 0
	for word in listOfWords:
		if (len(word) > biggestLength):
			biggestLength = len(word)
			print(word)
	return biggestLength

	
## TEST ##
#data = UploadDataBase("hak_2352.txt",[" ","\n", "\\", "{", "}"])
data = UploadDataBase("Ashley-Madison.txt",["\n"])
#print(getMeanOfWordLength(data))
print(nbOccurenceOfSpecificCharacterByWordLength(data,"n"))
"""
print("data 0 : ",data[0])
print("data 1 : ",data[1])
print("data 2 : ",data[2])
print("data 3 : ",data[3])
print("data 4 : ",data[4])
print("data 5 : ",data[5])
print("data 6 : ",data[6])
print("data 7 : ",data[7])
print("data 8 : ",data[8])
print("data 9 : ",data[9])
print("data 10 : ",data[10])
print("data 11 : ",data[11])
print("data 12 : ",data[12])
print("data 13 : ",data[13])
print("data 14 : ",data[14])
print("data 15 : ",data[15])
print("data 16 : ",data[16])
print("data 17 : ",data[17])
print("data 18 : ",data[18])
print("data 19 : ",data[19])
print("data 20 : ",data[20])
"""


