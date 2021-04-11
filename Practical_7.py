print ("Question 1")
print ()

n = int(input(("Enter the number of values to display: ")))# n means that any number you put
i = 1                                                      #Starting point is 1
while i<=n:                                                # n represents the nth number, and it must be included
    print (i)
    i= 1+i                                                 #add one from the previous number


print ("Question 2")
print ()

sum = 0.0
while True:
    number = float(input("Enter value number : "))
    if (number >=0):                                      #all values (numbers) must be positive 
        sum += number
    else:                                                 #if a negative number is put the code will stop and give us the sum of the other numbers
        break
print ("The sum of 6 values", "=" ,float(sum))


print("Question 3")
print()

fib = int(input("Enter number of terms to complete: "))  
count = 0                                                #must start counting from 0
f0 = 0                                                   #term number 1
f1 = 1                                                   #term number 2
f2 = f0 + f1                                             #general formula of Fibonacci
print("Fibonacci series")
while count < fib :                                      # count < fib because the last value we enter must not be included 
        print(f0)
        f2 = f0 + f1                                     #general formula of Fibonacci
        f0 = f1
        f1 = f2
        count  = count + 1                               #add one from the previous number
