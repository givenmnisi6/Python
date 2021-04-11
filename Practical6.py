import math
print("BMI Calculator")
print()
print("1. Weight in pounds, height in inches")
print("2. Weight in kilograms, height in meters")
print()
choice=int(input("Choice: "))
bmi=float()
if choice==2:
    print()
    weight=float(input("Weight in kilograms?: "))
    print()
    height=float(input("Height in meters?: "))
    print()
    bmi   =weight/(height**2)
    print("Results..............")
    print()
    print("Weight:\t" + str(round(weight,1))+ " kilograms")
    print("Height:\t" + str(round(height,1))+ " meters")
    print("BMI:\t" + str(round(bmi,1))+ "")

elif choice==1:
    print()
    weight=float(input("Weight in pounds?: "))
    print()
    height=float(input("Height in inches?: "))
    print()
    bmi   =weight/height**2*703
    print("Results..............")
    print()
    print("Weight:\t" + str(round(weight,1))+ " pounds")
    print("Height:\t" + str(round(height,4))+ " inches")
    print("BMI:\t" + str(round(bmi,1))+ "")

status=str()
if (bmi>=30):
    status = "Obese" 

elif (bmi>25 and bmi<29):
      status = "Overweight"

elif (bmi>18.5 and bmi<25):
      status = "Normal"

elif (bmi<18.5):
      status = "Underweight"

print("Status:\t"+ status)  
    
    
