#exercise 1: print strings: ballot_box_with a check: 
#creating string types variable 

print('twinkle twinkle little star, \n\t how I wonder what you are! \n\t\t Up above the world so high \n\t\t like a diamond in the sky. \ntwinkle, twinkle, little star \n How I wonder what you are!')

#exercises 2: Write a Python Program to Print The Version of Python version that you are using: ballot_box_with_check:
#this is the solution of exercise: 

#Python version 

import sys 
print("python version")
print(sys.version)
print("version info. ")
print(sys.version_info)

# Exercise 3: Print date and time: ballot_box_with_a_check
#Write a python program to display the current date and time: 

from datetime import date 

today = date.today()

#dd/mm/yy
d1 = today.strftime("%d/ %m / %y")
print("d1= ",d1 )
 
#textual month, day, and year 
d2 = today.strftime("%b %b, %y")
print("d2 = ",d2 )

#mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

#month abbreviation, day and year
d4 = today.strftime("%b-%d-%y")
print("d4 =", d4)

#Exercise 4: Strings concatination: ballot_box_with_check: 
#Write three strings in different variables and print the output of one string 

#this program is creating variable 

a = "Hello"
b = "there"
c = ",mate"

print( a, " " + b,  " " + c )

#Exercise 5: Compute the area of a circle: ballot_box_with_check:
#Write a python program which accepts the radius of a circle from the user to compute the area 

import math as M
Radius = float (input('please enter the radius of the given circle: '))
area_of_the_circle = M.pi * Radius * Radius 
print("the area of the given circle is: ", area_of_the_circle )




