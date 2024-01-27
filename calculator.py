import os
def add(a,b):
    print(("addition is:"))
    return a+b
def subtract(a,b):
    print("subtraction is:")
    return a-b
def multiply(a,b):
    print("multiplication is:")
    return a*b
def divide(a,b):
    print("division is:")
    return a/b

operations_dict = {

    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    number1 = int(input("enter first number:"))

    continue_flag = True
    while continue_flag:
        for i in operations_dict:
            print(i)
        op_symbol = input("pick an operation from above:")
        number2 = int(input("enter second number:"))
        calculate_fun = operations_dict[op_symbol]
        result = calculate_fun(number1, number2)
        print(result)
        should_continue = input(f"enter 'y' to continue calculation with {result} or 'n' to stat new calculation :")
        if should_continue == 'y' or should_continue == 'Y':
            number1 = result
        elif should_continue == 'n' or should_continue == 'N':
            continue_flag = False
            os.system('cls')
            calculator()
        elif should_continue == x:
            continue_flag=False


calculator()


