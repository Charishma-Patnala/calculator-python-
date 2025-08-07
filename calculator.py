def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers, with a check for division by zero."""
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

def main():
    """Main function to run the calculator CLI."""
    # A dictionary to map user's choice to the corresponding function
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    print("Simple Calculator CLI App")
    # Joining the operations for a dynamic menu
    print("Operations:")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

    while True:
        choice = input("Select operation (1/2/3/4 or q to quit): ")

        if choice.lower() == 'q':
            print("Thanks for choosing me!")
            break

        # Check if the choice is a valid operation key
        if choice in operations:
            try:
                # Using float allows for decimal inputs
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                # Retrieve the function from the dictionary and call it
                calculation_function = operations[choice]
                result = calculation_function(num1, num2)
                print("Result:", result)

            except ValueError:
                print("Invalid input. Please enter numeric values.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid input. Please select a valid operation.")

# Ensures the main function is called only when the script is executed directly
if __name__ == "__main__":
    main()
    