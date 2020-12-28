a = str(input("enter the line : "))
l=u=dig=alp=0

for i in a :
    if i.islower()==True:
        l=l+1

    elif i.isupper()==True:
        u=u+1
    elif i.isdigit()==True:
        dig=dig+1
    elif i.isalpha()==True:
        alp=alp+1

print('lower char are',l)
print('upper :', u)
print('digits :', dig)
print('alphabets :', alp)
