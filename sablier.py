def sablier(height, width, x, y):
    halfW = width/2;
    halfH = height/2;
    firstTriangle = fill_triangle(x,y,halfW+x,halfH+y,-1*halfW+x,halfH+y, color="black");
    secondTriangle = fill_triangle(x,y,halfW+x,-1*halfH+y,-1*halfW+x,-1*halfH+y, color="black");
    finalImage = overlay(firstTriangle, secondTriangle);
    show_image(finalImage)
sablier(0.3,0.5,0.1,0.7);
