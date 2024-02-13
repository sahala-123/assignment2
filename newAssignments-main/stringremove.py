String= "Hello, How Are You"
print(String)
Vowels=['a','e','i','o','u','A','E','I','O','U']
Result=""
for i in range(len(String)):
    if String[i] not in Vowels:
        Result=Result+String[i]
    print("\nAfter removing Vowles : ",Result)