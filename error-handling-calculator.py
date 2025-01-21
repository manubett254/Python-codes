# 1. Basic Calculator with Error Handling
import operator

def calculator():
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    try:
        num1 = float(input("Enter the first number: "))
        op = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        if op in ops:
            result = ops[op](num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid operator!")
    except Exception as e:
        print(f"Error: {e}")

calculator()