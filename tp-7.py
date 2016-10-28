import re
#7.8
def chargement_fichier(nom_fichier):
	L1 = []
	L2 = []
	with open(nom_fichier, 'r') as f:
		L1 = f.readlines()
	for ligne in L1:
		if(ligne and ligne[-1] == '\n'):
			L2.append(ligne[:-1])
		else:
			L2.append(ligne)
	return L2
def sauvegarde_fichier(nom_fichier, Contenu):
	with open(nom_fichier, 'w') as f:
		for ligne in Contenu:
			f.write(ligne)
			f.write('\n')
	return None
sauvegarde_fichier('haiku.txt', 'Papillon voltige\nDans un monde\nSans espoir.\n(Kobayashi Issa)')
chargement_fichier('haiku.txt')
def decoupage_mots(string):
	wordList = string.split()
	return wordList
def lecture_produit(string):
	return tuple(decoupage_mots(string))
def lecture_commande(L):
	listToReturn = []
	index = 0
	print(len(L))
	while index < len(L):
		listToReturn.append(lecture_produit(L[index]))
		index += 1
	return listToReturn
def gen_facture(L):
	listToRet = []
	listToRet.append('Produit Prix')
	listToRet.append('_______ ____')
	index = 0
	while index < len(L):
		tmpVar = L[index]
		index += 1

