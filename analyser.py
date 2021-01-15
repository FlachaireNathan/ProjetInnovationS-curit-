import matplotlib.pyplot as plt # Permet de créer des graphiques visuels
import re # Permet d'utiliser des regex

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

# Prends en argument la liste des mots
# Retourne le mot le plus long
def getBiggestWordLength(listOfWords):
	biggestLength = 0
	for word in listOfWords:
		if (len(word) > biggestLength):
			biggestLength = len(word)
	return biggestLength

# Retourne le nombre de mots dans la liste qui ne contiennent que des lettres (a-z)
def getNbWordCorrespondingToRegex(listOfWords, Regex):
	counter = 0
	for word in listOfWords:
		allMatchingCharacters = ""
		for character in  re.findall(Regex,word):
			allMatchingCharacters += character
		if (word == allMatchingCharacters):
			counter += 1
	return counter

# Retourne le nombre de mot redondant dans la liste de mot
def getNbSameWords(listOfWords):
	counter = 0
	for word1 in listOfWords:
		for word2 in listOfWords:
			if (word1 == word2):
				counter += 1
	counter -= len(listOfWords)
	return counter

#Prends en arguement la liste des donnée, le label X et le label Y pour afficher un graphique 
def showData(dataForPlot, xLabel, yLabel):
	plt.plot(dataForPlot)
	plt.xlabel(xLabel)
	plt.ylabel(yLabel)
	plt.show()
	




### TEST ###

## Corpus Hak

# Chargement des données
dataTrain = UploadDataBase("text-generation/data/test.txt",[" ","\n", "\\", "{", "}"])

# Obtenir la moyenne de la longueur des mots
print("La moyenne des mots du corpus Hak est : ", getMeanOfWordLength(dataTrain))

# Obtenir le nombre d'occurence d'un caractère selon la taille des mots puis l'afficher sur un graph
dataForPlot = nbOccurenceOfSpecificCharacterByWordLength(dataTrain,"n")
showData(dataForPlot, "longueur du mot", "nombre d'occurence")

nbPasswords = len(dataTrain)
print("Le nombre total de mot de passe : ", nbPasswords)

# Obtenir le nombre de mots dans le corpus qui respecte le regex assigné (adns l'ordre lettre, chiffre)

# 1 #

OnlyLettersUpperCase = getNbWordCorrespondingToRegex(dataTrain, "[A-Z]")
print("Le nombre de mots qui ne contienne que des lettres uppercases : ", OnlyLettersUpperCase)

OnlyLettersLowerCase = getNbWordCorrespondingToRegex(dataTrain, "[a-z]")
print("Le nombre de mots qui ne contienne que des lettres lowercase : ", OnlyLettersLowerCase)

OnlyNumbers = getNbWordCorrespondingToRegex(dataTrain, "[0-9]")
print("Le nombre de mots qui ne contienne que des chiffres : ", OnlyNumbers)

OnlySpecials = getNbWordCorrespondingToRegex(dataTrain, "[^A-Za-z0-9]")
print("Le nombre de mots qui ne contienne que des caractères spéciaux : ", OnlySpecials)

Others = nbPasswords - OnlyLettersUpperCase - OnlyLettersLowerCase - OnlyNumbers - OnlySpecials
print("Les autres mot de passes : ", Others)

"""
# 2 #

OnlyLetters = getNbWordCorrespondingToRegex(dataTrain, "[a-zA-Z]") - OnlyLettersUpperCase - OnlyLettersLowerCase
print("Le nombre de mots qui ne contienne que des lettres : ", OnlyLetters)

OnlyLettersUpperCaseAndNumbers = getNbWordCorrespondingToRegex(dataTrain, "[A-Z0-9]") - OnlyLettersUpperCase - OnlyNumbers
print("Le nombre de mots qui ne contienne que des lettres uppercase et nombres : ", OnlyLettersUpperCaseAndNumbers)

OnlyLettersUpperCaseAndSpecials = getNbWordCorrespondingToRegex(dataTrain, "[^a-z0-9]") - OnlyLettersUpperCase - OnlySpecials
print("Le nombre de mots qui ne contienne que des lettres uppercase et caractères spéciaux : ", OnlyLettersUpperCaseAndNumbers)

OnlyLettersLowerCaseAndNumbers = getNbWordCorrespondingToRegex(dataTrain, "[a-z0-9]") - OnlyLettersLowerCase - OnlyNumbers
print("Le nombre de mots qui ne contienne que des lettres uppercase et caractères spéciaux : ", OnlyLettersLowerCaseAndNumbers)

OnlyLettersLowerCaseAndSpecials = getNbWordCorrespondingToRegex(dataTrain, "[^a-z0-9]") - OnlyLettersLowerCase - OnlySpecials
print("Le nombre de mots qui ne contienne que des lettres lowercase et caractères spéciaux : ", OnlyLettersLowerCaseAndSpecials)

OnlyNumbersAndSpecials = getNbWordCorrespondingToRegex(dataTrain, "[^a-z0-9]") - OnlyNumbers - OnlySpecials
print("Le nombre de mots qui ne contienne que des nombres et caractères spéciaux : ", OnlyNumbersAndSpecials)


# 3 #

OnlyLettersAndNumbers = getNbWordCorrespondingToRegex(dataTrain, "[a-zA-Z0-9]]") - OnlyLettersUpperCase - Only OnlyLetters - OnlyNumbers
print("Le nombre de mots qui ne contienne que des lettres et nombres : ", OnlyLettersAndNumbers)

OnlyLettersAndSpecials = getNbWordCorrespondingToRegex(dataTrain, "[^0-9]]") - OnlyLetters - OnlySpecials
print("Le nombre de mots qui ne contienne que des lettres et caractère spéciaux : ", OnlyLettersAndSpecials)

OnlyLettersUpperCaseAndNumbersAndSpecials = getNbWordCorrespondingToRegex(dataTrain, "[^a-z]") - OnlyLettersUpperCase - OnlyNumbers - OnlySpecials
print("Le nombre de mots qui ne contienne que des lettres uppercase, nombres et caractère spéciaux : ", OnlyLettersUpperCaseAndNumbersAndSpecials)

OnlyLettersLowerCaseAndNumbersAndSpecials = getNbWordCorrespondingToRegex(dataTrain, "[^a-z]") - OnlyLettersLowerCaseAndNumbers - OnlyNumbers - OnlySpecials
print("Le nombre de mots qui ne contienne que des lettres lowercase, nombres et caractère spéciaux : ", OnlyLettersLowerCaseAndNumbersAndSpecials)


# 4 #
OnlyLettersAndNumbersAndSpecials = nbPasswords - OnlyLetters - OnlyNumbers - OnlySpecials
print("Le nombre de mots qui contiennent tout type de caractères : ", OnlyNumbersAndSpecials)


OnlyNumbersOrSpecials = getNbWordCorrespondingToRegex(dataTrain, "[^a-zA-Z]") - OnlyNumbers - OnlySpecials

print("Le nombre de mots qui contient des lettres, nombres et caractères, spéciaux : ", getNbWordCorrespondingToRegex(dataTrain, "[^0-9]]"))

# Obtenir le nombre de mots redondant dans la liste
print("Le nombre de mot redondant : ", getNbSameWords(dataTrain))

"""

"""

## Corpus Ashley

# Chargement des données
dataAshley = UploadDataBase("Ashley-Madison.txt",["\n"])

# Obtenir la moyenne de la longueur des mots
print("La moyenne des mots du corpus Ashley est : ", getMeanOfWordLength(dataAshley))

# Obtenir le nombre d'occurence d'un caractère selon la taille des mots puis l'afficher sur un graph
dataForPlot = nbOccurenceOfSpecificCharacterByWordLength(dataAshley,"n")
showData(dataForPlot, "longueur du mot", "nombre d'occurence")

# Obtenir le nombre de mots dans le corpus qui respecte le regex assigné (adns l'ordre lettre, chiffre)
print("Le nombre de mots qui ne contienne que des lettres : ", getNbWordCorrespondingToRegex(dataAshley, "[a-zA-Z]"))
print("Le nombre de mots qui ne contienne que des chiffres : ", getNbWordCorrespondingToRegex(dataAshley, "[0-9_]"))
print("Le nombre de mots qui ne contienne que des caractères spéciaux : ", getNbWordCorrespondingToRegex(dataTrain, "[^A-Za-z0-9]"))

# Obtenir le nombre de mots redondant dans la liste
#print("Le nombre de mot redondant : ", getNbSameWords(dataAshley))

"""