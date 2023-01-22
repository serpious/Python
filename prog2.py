#Program 2

import math as m

def square(s=5):
    return s*s

def rectangle(l=10,b=5):
    return l*b

def circle(r=7):
    return r*r*m.pi

def trapezium(h=5,a=4,b=3):
    return 0.5*h*(a+b)

def cylinder(r=5,h=15):
    return m.pi*r*r*h

def cube(a=5):
    return a*a*a

def sphere(r=7):
    return (4/3)*m.pi*r*r*r

def cone(r=7,h=14):
    return m.pi*(1/3)*r*r*h

print("\nSelect a shape and enter its parameters to get area/volume.\nAvailable shapes are : 1 square, 2 circle, 3 cube, 4 sphere, 5 rectangle, 6 cylinder, 7 cone & 8 trapezium,")
n = int(input("\tPlease select the corresponding number: "))

print("\nPlease enter the dimensions in centimeters:")

a = 5
b = 5
r = 5
h = 5

if n<=4:
    a = int(input("a : "))
elif n<8:
    h = int(input("height: "))
    r = int(input("base/radius: "))
else:
    h = int(input("height: "))
    a = int(input("top side: "))
    b = int(input("base side: "))

s = {}
s[1] = square(a)
s[2] = circle(a)
s[3] = cube(a)
s[4] = sphere(a)
s[5] = rectangle(r,h)
s[6] = cylinder(r,h)
s[7] = cone(r,h)
s[8] = trapezium(h,a,b)

if n == 3 or n == 4 or n == 6 or n == 7:
    print("The volume of the shape is",round(s[n],2),"cube centimeters")
else:
    print("The area of the shape is",round(s[n],2),"square centimeters")

print("\n")