# Simple Calculator

# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Choose operation

print("Take between: between 1 to 4")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    result = num1 + num2
    print("Result:", result)

elif choice == '5':
    result = num1 - num2
    print("Result:", result)

elif choice == '3':
    result = num1 * num2
    print("Result:", result)

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error! Division by zero.")

else:
    print("Invalid choice oof yours")


print("Hi World")