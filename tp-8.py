#10.4 cmd + b
LivresBD = {'Les miserables':('Victor Hugo', 5), 'Le Dernier des Mohicons': ('James F. Cooper', 0), 'Un animal doue de raison':('Robert Merle', 6), 'Le grand Meaulnes': ('Alain Fournier', 1), 'Notre-dame de paris':('Victor Hugo', 4), 'Les comtemplations':('Victor Hugo', 0)}
#print(LivresBD[LivresBD.keys()[0]][0])
def auteurs(Livres):
	listToReturn = [];
	for x in range(len(Livres.keys())):
		boolToCheck = True
		for z in range(len(listToReturn)):
			if(listToReturn[z] == Livres[Livres.keys()[x]][0]):
				boolToCheck = False;
		if(boolToCheck == True):
			listToReturn.append(Livres[Livres.keys()[x]][0])
	return listToReturn

def titres_empruntables(Livres):
	return Livres.keys()
#print(titres_empruntables(LivresBD))

def titres_auteur(nom, Livres):
	listToReturn = [];
	for x in range(len(Livres)):
		print(Livres[Livres.keys()[x]][0])
		if(Livres[Livres.keys()[x]][0] == nom):
			listToReturn.append(Livres.keys()[x])
	return listToReturn

#print(titres_auteur('Victor Hugo', LivresBD))



#10.4
Grandes_Lignes = {'Paris': {'Strasburg', 'Dijon', 'Toulouse', 'Lille', 'Lyon', 'Bordeaux'}, 'Strasburg': {'Paris', 'Dijon', 'Munchen'}, 'Munchen':{'Strasburg'}, 'Dijon':{'Paris', 'Strasburg', 'Lyon', 'Toulouse'}, 'Lyon':{'Paris', 'Dijon', 'Toulouse'}, 'Toulouse':{'Paris', 'Lyon', 'Dijon'}, 'Bordeaux':{'Nantes', 'Paris'}, 'Nantes':{'Paris', 'Bordeaux', 'Quimper'}, 'Quimper':{'Nantes'}, 'Ajaccio':{'Bastia'}, 'Bastia':{'Ajaccio'}, 'Lille':{'Paris'}};
#print('Strasburg' in Grandes_Lignes['Paris'])
def trajet_direct(carte, st1, st2):
	if(st1 in carte[st2]):
		return True
	else:
		return False
def ajout_station(station, s, Grandes_Lignes):
	j = Grandes_Lignes.copy()
	Grandes_Lignes[station] = s;
	for x in s:
		j.add(station)
	return Grandes_Lignes


#print(ajout_station('Limoges', {'Paris', 'Toulouse', 'Bordeaux'}, Grandes_Lignes))
#print(trajet_direct(Grandes_Lignes, 'Strasburg', 'Bordeaux'))

def stations_atteignables(Grandes_Lignes, nom, k):
	if( k == 0):
		return {nom}
print(stations_atteignables(Grandes_Lignes, 'Paris', 0))
