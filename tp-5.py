def suppression_second(c, s):
    return s.replace(c, '');
def suppression(c, s):
    strSum = '';
    for i in range(0,len(s)):
        if(s[i] != c):
            strSum += s[i];
    return strSum;

def suppression_debut(c, s):
    strSum = '';
    booleanCheck = False;
    for i in range(0,len(s)):
        if(booleanCheck == True):
            strSum += s[i];
        else:
            if(s[i] != c ):
                strSum += s[i];
            else:
                booleanCheck = True;
    return strSum;

def suppression_dernier(c, s):
    strSum = '';
    booleanCheck = False;
    i = len(s) -1
    while i >= 0:
        if(booleanCheck == True):
            strSum += s[i];
        else:
            if(s[i] != c ):
                strSum += s[i];
            else:
                booleanCheck = True;
        i = i - 1;
    return strSum;
#5.7
def chiffre(c):
    return ord(c) - 48;
def entier(s):
    finalNum = 0;
    for i in range(0, len(s)):
        finalNum += chiffre(s[i]) * (10**(len(s)-i-1));
    return finalNum;

def caractere(n):
    return(chr(n + 48))
def chaine(n):
    strFinal = '';
    while n > 10:
        valueToGet = n%10
        n = n//10
        print(valueToGet)
        if(valueToGet<10):
            strFinal += caractere(valueToGet)
    return strFinal;
print(chaine(421))
