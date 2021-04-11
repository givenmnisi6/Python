print ("Question 1")
print ()

n = int(input("Enter the number of values to display: "))
for i in range (0,n):#Must start from 0 to n 
	print(i+1)       #From the starting point which is 0 we must add one so the first number will be one
	
print ("Question 2")
print ()
def powerInt (base, exponent): 
    for i in range (exponent):
        output = base**exponent
    return output   
base = int(input("Enter base value: "))
exponent = int(input("Enter exponent value: "))
print (base, "raised to the power of",exponent, "=", powerInt(base, exponent)) 
