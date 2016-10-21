import math;
def polynomiale(a, b, c, d, x):
    """float*float*float*float*float->float
    retourne le valeur de fonction a*x^3+b*x^2+c*x+d"""
    return (a*math.pow(x, 3))+(b*math.pow(x, 2))+(c*math.pow(x, 1))+d;

print(polynomiale(2, 3, 4, 5, 6))
# jeu de test
assert polynomiale(1, 2, 3, 4, 6) == 310.0;
assert polynomiale(2, 3, 4, 5, 6) == 569.0;
