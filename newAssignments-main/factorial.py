number=int(input("Enter a number : "))
am=number
fact=1
while(number >= 1):
    fact=fact*number
    number=number-1
print("Factorial of",am,"is",fact)