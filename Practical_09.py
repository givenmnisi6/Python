print("QUESTION 1")
print("")

value = input("Enter value to convert to decimal: ")
base    = float(input("Enter the base of the value : "))		

if base==2:
    print(value,"in base",round(base),"=",int(value, 2),"in decimal")
elif base==8:
    print(value,"in base",round(base),"=",int(value ,8),"in decimal")
elif base==16:
    print(value,"in base",round(base),"=",int(value, 16),"in decimal")
print("")

print("QUESTION 2")
print("")
word = input("Enter the word to test for palindrome: ")
length = round(float(len(word))) 
revword = word[::-1]
x = 0
print("")
while x < length:
    print(word[0+x],"--",word[length-1-x])
    if word[0+x].upper() == word[length-1-x].upper():
        x = x + 1
    else: x = length 
print("")
if word.upper() == revword.upper():
    print("-->Palindrome")
else:
    print("-->Not Palindrome")
print("")

