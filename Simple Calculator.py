def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y


print("\n---Simple Calculator---")
print("Basic Operations:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter your choice:")
    if choice == '5':
        print("exit")
        break
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Addition of {num1} and {num2} is:", add(num1, num2))
    elif choice == '2':
        print(f"Subtraction of {num1} and {num2} is:", subtract(num1, num2))
    elif choice == '3':
        print(f"Multiplication of {num1} and {num2} is:", multiply(num1, num2))
    elif choice == '4':
        print(f"Division of {num1} and {num2} is:", divide(num1, num2))
    else:
        print("Invalid input")
