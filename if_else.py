
# read 5 sub marks of a student , calculte total % and check grade if percenttage
a =int(input("Enter the mark in 1st sub : "))
b =int(input("Enter the mark in 2nd sub : "))
c =int(input("Enter the mark in 3rd sub : "))
d =int(input("Enter the mark in 4th sub : "))
e =int(input("Enter the mark in 5th sub : "))
perc =  (a+b+c+d+e)/5
print(f"you got {perc}%")
if perc >= 90 and perc<100 :
    print("grade A")
elif perc >= 80 and perc<90 :
    print("grade B")
elif perc >= 70 and perc < 80:
    print("grade C")
elif perc >= 60 and perc < 70:
    print("grade D")
elif perc >= 50 and perc < 60 :
    print("grade E")

elif perc >=40 and perc<50:
    print("Grade F ")
else:
    print('you  faild. ')

