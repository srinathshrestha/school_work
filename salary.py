#wap to read the basic salary of an employee. calculate TA , DA HRA, GROSS , EPS, AD and check grade of employee by below

salary = int(input("Enter your salary : "))
if salary >= 15000:
    TA = salary* 15/100
    DA = salary* 20/100
    HRA = salary*25/100
elif salary>= 10000:
    TA = salary* 10/100
    DA = salary* 15/100
    HRA = salary*20/100
else:
    TA = salary* 3/100
    DA = salary* 5/100
    HRA = salary*10/100
gross  = salary + TA + DA+HRA
if gross  >= 25000:
    E = gross * 25/100
elif gross >= 20000:
    E = gross*20/100
elif gross >= 15000:
    E = gross * 15/100
else :
    E = gross * 10/100
AD = gross - E
print(f"In basic = {salary}\n TA = {TA} \n DA = {DA} \n HRA = {HRA} \n gross = {gross} \n EPF = {E} \n Ampunt drawn = {AD}")
if AD >= 20000:
    print("GRADE A EMPLOYEE")
elif AD >= 15000:
    print("GRADE B EMPLOYEE")
elif AD >= 10000:
    print("GRADE C EMPLOYEE")
else:
    print("GRADE D EMPLOYEE")