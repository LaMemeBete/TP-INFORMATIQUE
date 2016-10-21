#6.4
def liste_diviseurs(a):
	i = 1
	listToReturn = [];
	while i <= a:
		if(a%i == 0):
			listToReturn.append(i);
		i = i +1
	return listToReturn
def liste_diviseurs_impairs(a):
	i = 1
	listToReturn = [];
	while i <= a:
		if(a%i == 0 and i%2 == 1):
			listToReturn.append(i);
		i = i +1
	return listToReturn

def liste_diviseurs_pairs(a):
	i = 1
	listToReturn = [];
	while i <= a:
		if(a%i == 0 and i%2 == 0):
			listToReturn.append(i);
		i = i +1
	return listToReturn

#6.6
def list_mult(L, K):
	i = 0
	listToReturn = [];
	while i < len(L):
		listToReturn.append(L[i]*K);
		i = i +1
	return listToReturn

def list_div(L, K):
	i = 0
	listToReturn = [];
	while i < len(L):
		if(L[i]%K == 0):
			listToReturn.append(L[i]/K);
		i = i +1
	return listToReturn

#6.7
def decoupage_simpe(L, i, j):
	index = i
	listToReturn = [];
	while index <= j:
		listToReturn.append(L[index]);
		index = index +1
	return listToReturn

def decoupage_pas(L, i, j, p):
	index = i
	listToReturn = [];
	while index <= j:
		listToReturn.append(L[index]);
		index = index + p
	return listToReturn

def decoupage_pas_inv(L, i, j, p):
	index = i
	listToReturn = [];
	while index >= j:
		listToReturn.append(L[index]);
		index = index + p
	return listToReturn

comptine = ['ca', 'cb', 'ac', 'gd', 'gf', 'en', 'eh']
#print(comptine[5:2:-1])
print(decoupage_pas_inv(comptine, 5, 2, -2))
assert decoupage_pas(comptine, 2, 5, 2) == comptine[2:5:2]
assert decoupage_pas_inv(comptine, 5, 2, -2) == comptine[5:2:-2]

#6.8
def entrelacement(L1, L2):
	index = 0
	listToRetuen = []
	while(index<len(L1)):
		listToRetuen.append(L1[index])
		listToRetuen.append(L2[index])
		index += 1
	return listToRetuen;
print(entrelacement([1, 2,3], [4, 5, 6]))







