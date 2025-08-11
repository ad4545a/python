#write a program that calculate and print the area and curfrance of a circle using math module
import math
# radius=int(input("enter the radius:- "))
# area=3.14*pow(radius,2)
# curfrance=2*3.14*radius
# print(f"area:- {area} curfrance:- {curfrance}")
#to find the factriol of an enetred number using math module
# n=int(input())
# print(math.factorial(n))
#3
# n=float(input())
# print(round(n))
#4
# n=float(input())
# print(math.ceil(n))
#5
# n=float(input())
# print(math.floor(n))
#6
base,hight=float(input("base:- ")),float(input("hight:- "))
hyp=float(math.isqrt(round(pow(base,2)+pow(hight,2))))
print(hyp)