income = int(input("Enter your income : " ))
tax = 0
def main_calculator (percentage):
    result = int((income-100000)*percentage/100)
    return  result

if income <= 100000:
    print(f'you have to pay {tax} Rupees')
elif income > 100000 and income < 300000 :
     print(f'you have to pay {main_calculator(10)} rupees')
elif income >= 300000 and income < 500000:
    print(f'you have to pay {main_calculator(20)} rupees')
elif income >= 500000:
    print(f'you have to pay {main_calculator(30)} rupees')
else:
    print("Enter a vaild input!!")
