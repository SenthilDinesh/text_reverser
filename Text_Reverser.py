import re

while True:
    try:
        menu = int(input("""Choose an option (1 or 2):
       1. Reverse Character Order
       2. Reverse Word Order
       Choice: """))
        if menu not in [1, 2]:
            raise ValueError("Error: Please choose either 1 or 2.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        user_input = input("Enter a string: ").strip()
        if not user_input:
            raise ValueError("Error: Input cannot be empty.")
        if not re.match("^[a-zA-Z0-9 .,!?]*$", user_input):
            raise ValueError("Error: Special characters not allowed.")
        break
    except ValueError as e:
        print(e)

if menu == 1:
    print(f"Reversed character order: {user_input[::-1]}")
elif menu == 2:
    print("Reversed word order:", " ".join(user_input.split()[::-1]))
