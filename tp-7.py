#7.8
def chargement_fichier(nom_fichier):
	L1 = []
	L2 = []
	with open(nom_fichier, 'r') as f:
		L1 = f.readlines()
	for ligne in L1:
		if(ligne and lign[-1] == '\n'):
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

def decoupage_mots(str):
	index  = 0;
	while(index<len(str)):
		if(str[index])


