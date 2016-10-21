def perimetre(largeur, longueur):
    """int*int->int
    hypothese : (largeur>=0) and (longueur>=0)
    hypothese : longueur >= largeur
    retourne le perimetre du rectangle defini par sa largeur et sa l     omgu eur."""
    return 2*(largeur + longueur)
#jeu de test
assert perimetre(2, 5)  == 14

def surface(largeur, longueur):
    """int*int->int
    hypothese : (largeur>=0) and (longueur>=0)
    hypothese : longueur >= largeur
    retourne le perimetre du rectangle defini par sa largeur et sa l     omgu eur."""
    return (largeur*longueur)

# jeu de test
assert surface(0, 0) == 0
assert surface(0, 10) == 0
assert surface(10, 0) == 0
assert surface(10, 0) == 0
assert surface(1, 1) == 1
assert surface(10, 20) == 200

def dessine_carre (x,y,c):
    """float*float*float->image
    construit un carre dont le point en bas a gauche est de coordonn     ees (x,y) et le cote de longueur c"""
    show_image(draw_line(x,y,x,y+c, color="red"))
    show_image(draw_line(x,y+c,x+c,y+c, color="red"))
    show_image(draw_line(x+c,y+c,x+c,y, color="red"))
    show_image(draw_line(x+c,y,x,y, color="red"))

dessine_carre(0,0, 0.6)
