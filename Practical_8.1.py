print("Question 1")
#hexadecimal system have base 16
#the symbols are 0-9 and A-F (the A-F is 11-15)

def hexadecimal (number):                               
    if number == 10:            
        return "A"
    elif number == 11:          #number equals to 11
        return "B"
    elif number == 12:          #number equals to 11
        return "C"
    elif number == 13:          #number equals to 11
        return "D"              
    elif number == 14:          #number equals to 11
        return "E"
    elif number == 15:          
        return "F"
    else:
        return number
        
def decimaltobase (decimal, base):
    output = ""
    while (decimal!=0) :                #decimal not equals to 0
        remainder = decimal % base      
        decimal = decimal // base       # quotient (//) rounds the result down to the nearest whole number
        output = str (hexadecimal(remainder)) + output 
    return output

decimal = int(input("Enter decimal to convert to base: "))
base    = int(input("Enter base for conversion: "))
print("    ___")                 #the space in the after the first " is for the base and |
print(base, "|",decimal)
print("Base", base, "value of", decimal, "=", decimaltobase(decimal,base))






