import random
import math;
#4.4 - 1
def nb_couples_intervalle(n, p):
    indexSum = 0;
    for index in range(n,p):
        currentPlace = index+1
        while currentPlace <= p:
            #print(index, currentPlace)
            indexSum +=1;
            currentPlace += 1;

    return indexSum;

print(nb_couples_intervalle(2, 6))

#4.4 - 2, 3
def nb_couples_divise(n, p):
    indexSum = 0;
    for index in range(n,p):
        currentPlace = index+1

        logCouple = "";
        logDivisions = "";
        
        while currentPlace <= p:
            if(index != 0):
                if(currentPlace%index == 0):
                    indexSum += 1;
                    logDivisions = str(logDivisions) + str(index) + " divise " + str(currentPlace) + "\n"
            logCouple += "couple ("+ str(index) +","+str(currentPlace)+")\n"
            currentPlace += 1;
        print(logCouple +"\n"+ "--------\n"+ logDivisions);
    return indexSum;
#print(nb_couples_divise(2, 6))

#4.4 - 4, 5
def existe_couples_divise_rapide(n, p):
    indexSum = 0;
    indexInt = n
    foundCouple = False;
    while indexInt < p: 
        currentPlace = indexInt+1
        while currentPlace <= p:
            indexSum +=1;
            if(indexInt != 0):
                if(currentPlace%indexInt == 0):
                    return True;
            currentPlace += 1;
        indexInt += 1
    return False

#4.4 - 6
def nombre_couples_divise_rapide(n, p):
    nombre = 0;
    indexInt = n
    foundCouple = False;
    while indexInt < p: 
        currentPlace = indexInt+1
        while currentPlace <= p:
            nombre +=1;
            if(indexInt != 0):
                if(currentPlace%indexInt == 0):
                    return nombre;
            currentPlace += 1;
        indexInt += 1
    return nombre


def existe_couples_devise_rapide_trace_tour(n,p):
    print("nombre de couples testes : "+str(nombre_couples_divise_rapide(n, p)));
    print(existe_couples_divise_rapide(n, p));

def existe_couples_devise_trace_tour(n,p):
    print("nombre de couples testes : "+str(nb_couples_intervalle(n, p)));
    print(existe_couples_divise_rapide(n, p));
    
print(existe_couples_devise_trace_tour(3,1000))    




