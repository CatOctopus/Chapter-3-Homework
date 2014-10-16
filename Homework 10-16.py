#Homework due 10-16

def sphere(radius):
    from math import pi
    V=(4/3)*(pi)*(radius**3)
    A=4*(pi)*(radius**2)
    return V, A
def order_cost(pounds):
    return pounds*10.5+pounds*.86+1.5
def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)
