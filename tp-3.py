import random
import math;
#3.8
def lancer_de6(seed = None):
    if seed != None:
        random.seed(seed);
    varToReturn = math.floor(random.random()*6) + 1;
    return varToReturn

# jeu de test
assert(lancer_de6(10) == 4)
assert(lancer_de6(9) == 3)

def moyenne_plusieurs_lancers(n):
    sum = 0;
    index = 0;
    while index<n:
        sum  += lancer_de6(math.floor(random.random()*10000));
        index +=1;
    return (sum/n)

def frequance_valeur(r, n):
    index = 0;
    counterFrequance = 0;
    while index<n:
        valueLancerDe6 = lancer_de6(math.floor(random.random()*10000));
        if(valueLancerDe6 == r):
            counterFrequance += 1;
        index += 1;
    return counterFrequance/n

def lancer_deN(n):
    varToReturn = math.floor(random.random()*n) + 1;
    return varToReturn

print(frequance_valeur(3, 1000))
#3.7
def suit_racine(x, n):
    if n == 0:
        return 1.0
    else:
        
        
