def divide_numbers():
    try:
        # Get input from the user
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))

        # Perform the division
        result = dividend / divisor
        print(f"Result of division: {result}")

    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")
    except ValueError:
        print("Error! please enter valid numbers")
    except Exception as e: # incase any other errors occur that you may not be aware of (kind of like a back up default error message)
        print(f"An unexpected error occured: {e}")
    finally:
        print("Division operation closed.")

# Perform the division
divide_numbers()
    