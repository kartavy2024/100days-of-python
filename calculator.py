num1 =10
num2 =20

def calculate(operation,number1,number2):
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    else:
        return number1 / number2
    
calculations = calculate("-",45,45)

print(calculations)