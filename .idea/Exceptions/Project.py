import logging

# Configure logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(levelname)s:%(message)s')

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError as e:
            print("Invalid input! Please enter a valid number.")
            logging.error(f"ValueError occurred: {e}")

def perform_operation(choice):
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    try:
        if choice == '1':
            result = num1 + num2
            print(f"The result is: {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"The result is: {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"The result is: {result}")
        elif choice == '4':
            result = num1 / num2
            print(f"The result is: {result}")
    except ZeroDivisionError as e:
        print("Oops! Division by zero is not allowed.")
        logging.error(f"ZeroDivisionError occurred: {e}")
    except Exception as e:
        print("An unexpected error occurred.")
        logging.error(f"Unexpected error: {e}")
    finally:
        print("Operation completed.\n")

def calculator():
    print("Welcome to the Error-Free Calculator!")

    while True:
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("> ")

        if choice == '5':
            print("Goodbye!")
            break
        elif choice in ['1', '2', '3', '4']:
            perform_operation(choice)
        else:
            print("Invalid option. Please choose a number between 1 and 5.\n")

# Run the calculator
calculator()
