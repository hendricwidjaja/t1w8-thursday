def convert_to_integer(value):
    try:
        result = int(value)
        print(f"conversion Successful! Result: {result}")
    except ValueError:
        print("Conversion failed, please enter a valid integer.")
    finally: # optional
        print("Closing any open resources")

# User input
user_input = input("Enter a number to convert to integer: ")

# Convert the number
convert_to_integer(user_input)