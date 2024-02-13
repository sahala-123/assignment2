List=['apricote','banana','cherry','cocnut','avocado','pineapple','orange','grapes','apple']
check='a'
print("The original list : ",str(List))
res=[]
for i in List:
    if(i.find(check) == 0 or i.find(check.lower()) == 0):
        res.append(i)
print("List of matching letter : ",str(res))