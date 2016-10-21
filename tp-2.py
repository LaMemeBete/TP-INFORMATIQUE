#2.8 + 2.7
def rectangle(x,y,h,w):
    firstTriangle = fill_triangle(x,y,x+w,y,x+w,y+h);
    secondTriangle = fill_triangle(x,y,x,h+y,w+x,h+y);
    return overlay(firstTriangle, secondTriangle)

def tour(h, w1, w2,x,y):
    firstTour = rectangle(x,y,h,w1)
    cordinateX = (w1/2-w2/2)+x;
    cordinateY = y+h;
    secondTour = rectangle(cordinateX,cordinateY,h,w2)
    show_image(overlay(firstTour, secondTour))
    
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
    
def sablier(height, width, x, y):
    halfW = width/2;
    halfH = height/2;
    firstTriangle = fill_triangle(x,y,halfW+x,halfH+y,-1*halfW+x,halfH+y, color="black");
    secondTriangle = fill_triangle(x,y,halfW+x,-1*halfH+y,-1*halfW+x,-1*halfH+y, color="black");
    finalImage = overlay(firstTriangle, secondTriangle);
    show_image(finalImage)


def sablier(height, width, x, y):
    halfW = width/2;
    halfH = height/2;
    firstTriangle = fill_triangle(x,y,halfW+x,halfH+y,-1*halfW+x,halfH+y, color="black");
    secondTriangle = fill_triangle(x,y,halfW+x,-1*halfH+y,-1*halfW+x,-1*halfH+y, color="black");
    finalImage = overlay(firstTriangle, secondTriangle);
    show_image(finalImage)






