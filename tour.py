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
tour(0.1,0.8,0.5,0.7,0);
