# Calculator CLI App

# Function for Addition
def add(a, b):
    return a + b

# Function for Subtraction
def subtract(a, b):
    return a - b

# Function for Multiplication
def multiply(a, b):
    return a * b

# Function for Division
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# Store operations in a dictionary
operations = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide)
}

print("===================================")
print("     Welcome to Calculator CLI App")
print("===================================")

while True:

    print("\n========== Calculator CLI App ==========")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "5":
        print("\nThank you for using Calculator CLI App!")
        print("Goodbye! 👋")
        break

    if choice not in operations:
        print("\nInvalid choice! Please select a valid option.")
        continue

    try:
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number: "))
    except ValueError:
        print("\nInvalid input! Please enter numeric values.")
        continue

    operation_name, operation = operations[choice]
    result = operation(num1, num2)

    print(f"\n{operation_name} Result = {result}")