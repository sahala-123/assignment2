String=input("Enter String : ")
String=String.casefold()
reverse=reversed(String)
if list(String) == list(reverse):
    print("The string",String,"is Palindrome")
else:
    print("The string",String,"is not Palindrome")