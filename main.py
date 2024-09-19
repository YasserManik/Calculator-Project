def calculate():
    # Get operator and numbers from the user
    operator = input("Enter an operator (+, -, *, /): ")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input, please enter valid numbers.")
        return

# Perform calculation based on the operator

    if operator == "+":
        result = num1 + num2
        
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        # Handle division by 0
        if num2 == 0:
            print("Error, Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print(f"Error, '{operator}' is not a valid operator.")
        return
    
    # Output the result rounded to 3 decimal places
    print(f"The result is '{round(result, 3)}'")

if __name__ == "__main__":
    calculate()