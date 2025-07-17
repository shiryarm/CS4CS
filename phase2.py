#The user needs to choose what operation they perform

user_num1 = int(input("Enter the first number: "))

operation = input(f"Enter the operation (+, -, *, /): ")

user_num2 = int(input("Enter the second number: "))

if operation == '+':
    add = user_num1 + user_num2
    print(f"Result: {add}")
elif operation == '-':
    maxi = max(user_num1,user_num2)
    mini = min(user_num1,user_num2)
    subtract = maxi - mini
    print(f"Results: {subtract}")
elif operation == '*':
    multiply = user_num1*user_num2
    print(f"Results: {multiply}")
elif operation == '/':
    divide = user_num1/user_num2
    print(f"Results: {int(divide)}")