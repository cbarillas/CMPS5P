# Carlos Barillas
# cbarilla@ucsc.edu
# Programming Assignment 1
# Computes the volume and surface area of a sphere whose radius is entered by user

from math import pi as p

radius = float(input("Enter the radius of the sphere: "))
surfaceArea = 4* p*radius**2
volume = 4/3*p*radius**3

print("The volume is: "+str(volume))
print("The surface area is: "+str(surfaceArea))

