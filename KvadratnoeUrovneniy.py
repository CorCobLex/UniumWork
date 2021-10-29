import math

a = int (input())
b = int (input())
c = int (input())
D = 0
x = 0
y = 0

D = b**2-4*a*c
if(D>0):
    D=math.sqrt(D)
    x = (-b+D)/2*a
    y = (-b-D)/2*a
    print (x, y)
elif(D==0):
    x = (-b)/2*a
    print (x)
else:
    print ("Нет корней")
