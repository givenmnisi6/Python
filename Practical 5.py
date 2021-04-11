import math
from math import pi
from math import sqrt
from math import pow
print ("Assignment 1")
print()

variable1=float(input("Enter value 1: "))
variable2=float(input("Enter value 2: "))
variable3=float(input("Enter value 3: "))
variable4=float(input("Enter value 4: "))
variable5=float(input("Enter value 5: "))

average = float ((variable1+variable2+variable3+variable4+variable5)/5)
print()

print("The average of the values is: ", average)

print()

print ("Assignment 2")
print()
radius = float(input("What is the radius of the circle?:" ))
diameter = float(2*radius)
circumference = float(2*pi*radius)
area = float(pi*radius**2)
print()
print("The radius of the circle is: ",radius)
print("The diameter of the circle is: ",diameter)
print("The circumference of the circle is: ",round (circumference,2))
print("The area of the circle is: ",round (area,2))

print()

print ("Assignment 3")
print()
x1=float (input("Enter coordinate 1 for point X: "))
x2=float (input("Enter coordinate 2 for point X: "))
y1=float (input("Enter coordinate 1 for point Y: "))
y2=float (input("Enter coordinate 2 for point Y: "))
distance=float(sqrt((x1-y1)**2 + (x2-y2)**2))
print("The distance between point1 and point2 is: ",distance)

print()

print("Assignment 4")
print()
test1=float(input("Enter value for test 1: "))
test2=float(input("Enter value for test 2: "))
test3=float(input("Enter value for test 3: "))
testaverage = float((test1+test2+test3)/3)
print("The test average is: ",testaverage)
if testaverage>75:
    print("Congragulations students for passing the test")
else:print("Sorry students, Theres always room for improvement")




