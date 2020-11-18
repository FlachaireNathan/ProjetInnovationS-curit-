# Prends en argument le nom du fichier de la base de donnée (extension comprise) ET une liste de séparateurs de mot
# Charge la base de donnée, sépare les mots de passe selon les séparateurs données puis retourne une liste contenant tous les mots de passe
def UploadDataBase(nameFile,separatorList):
	f = open(nameFile, "r") # Charle le fichier dans une variable
	allPassword = [] # Prédéfini la liste de mot de passe qu'on retournera
	passwordToInsert = "" # variable contenant un mot de passe construit progressivement et qui sera ajouté à la liste de tous les mots de passe
	doSplit = False # variable booléenne pour déterminer si une séparation est faite ou non
	for line in f: # Pour chaque ligne du fichier
		for ch in line: # Pour chaque caractère de la ligne
			for separator in separatorList: # Pour chaque séparateur donné en argument, on check s'il correspond au caractère
				if (ch == separator): # Si oui, on passe doSplit à true et ono arrète la boucle
					doSplit = True
					break
			if (doSplit == True): # Si doSplit est vrai
				if (passwordToInsert != ""): # et que passwordToInsert n'est pas vide
						allPassword.append(passwordToInsert) # on ajoute le mot de passe à la liste
						passwordToInsert = "" # et on reset passwordToInsert pour accueillir un nouveau mot de passe
				doSplit = False # on repasse doSplit à False poour le prochain caractère
			else: # Si doSplit n'est pas vrai
				passwordToInsert += ch # On ajoute le caractère à passwordToInsert
	return allPassword

	
## TEST ##
#data = UploadDataBase("hak_2352.txt",[" ","\n", "\\", "{", "}"])
data = UploadDataBase("Ashley-Madison.txt",["\n"])
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


