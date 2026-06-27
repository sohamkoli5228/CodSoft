# Simple Calculator

print("===== SIMPLE CALCULATOR =====")

# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Choose operation
print("\nChoose an operation:")
print("+ : Addition")
print("- : Subtraction")
print("* : Multiplication")
print("/ : Division")

operation = input("Enter operation (+, -, *, /): ")

# Perform calculation
if operation == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid operation selected.")





    