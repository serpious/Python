# Program 2 UNIT 1
# ASTHA YADAV KMC PHYSICS HONORS

import math as m
import random as ra

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

print("\nWe are going to find area (for 2D shapes) and volumes (for 3D shapes) with random dimensions.")
print("You can choose the shape, available shapes are : 1 square, 2 circle, 3 cube, 4 sphere, 5 rectangle, 6 cylinder, 7 cone & 8 trapezium,")

n = int(input("\tPlease select the corresponding number: "))
print("You can choose the range from which the dimensions are selected")
s = float(input("Start of range: "))
e = float(input("End of range: "))

a = round(ra.uniform(s, e), 2)
b = round(ra.uniform(s, e), 2)
r = round(ra.uniform(s, e), 2)
h = round(ra.uniform(s, e), 2)

s = {}
s[1] = square(a)
s[2] = circle(a)
s[3] = cube(a)
s[4] = sphere(a)
s[5] = rectangle(r,h)
s[6] = cylinder(r,h)
s[7] = cone(r,h)
s[8] = trapezium(h,a,b)

if n == 1 or n == 3: print("The randomized side is",a)
elif n == 2 or n == 4: print("The randomized radius is",a)
elif n == 5: print("The randomized sides are",a,b)
elif n == 6 or n == 7: print("The randomized height is",h,"while base radius is",r)
else: print("The randomized height is",h,"and sides are",a,b)

if n == 3 or n == 4 or n == 6 or n == 7:
    print("The volume of the shape is",round(s[n],2),"cube centimeters")
else:
    print("The area of the shape is",round(s[n],2),"square centimeters")

print("\n")
