
# Prends en argument le nom du fichier de la base de donnée (extension comprise)
# Charge la base de donnée et retourne une liste contenant tous les mots de passe
def UploadDataBaseLineByLine(nameFile):
	f = open(nameFile, "r") # Charle le fichier dans une variable
	allPassword = [] # Prédéfini la liste de mot de passe qu'on retournera
	allLines = f.readlines() # Sépare toutes les lignes du fichier 
	# Pour chaque ligne du fichier, on ajoute la ligne dans allPassword car c'est une mot de passe
	for line in allLines:
		allPassword.append(line)
	return allPassword

print(UploadDataBaseLineByLine("Ashley-Madison.txt"))

