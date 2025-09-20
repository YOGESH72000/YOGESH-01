def calculator():
    print("Welcome to the Simple Calculator!")
    
    # Get input from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter your choice (1/2/3/4): ")

    # Perform calculation
    if operation == '1':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == '4':
        if num2 == 0:
            print("\nError: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nInvalid operation choice.")

# Run the calculator
calculator()
