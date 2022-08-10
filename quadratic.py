import math
a=float(input("enter  a num"))
b=float(input("enter the num"))
c=float(input("enter the num"))
d=(b*b)-(4*a*c)
sol1=(-b-math.sqrt(d))/(2*a)
sol2=(-b+math.sqrt(d))/(2*a)
print("solution are",(sol1,sol2))