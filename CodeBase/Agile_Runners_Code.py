# blank canvas to start

# Check the error catches for user input:
# ensuring numbers entered when choosing an option
# are between the required range
def read_integer_between_numbers(prompt, mini, maximum):
    while True:
        try:
            users_input = int(input(prompt))
            # changed the order and sentence of mini <= users <= maximum
            if mini <= users_input <= maximum:
                return users_input
            else:
                print(f"Numbers from {mini} to {maximum} only.")
        except ValueError:
            # spelling fix here
            print("Sorry number only please")

# Makes sure the user enters a string when required
# no changes here
def read_nonempty_string(prompt):
    while True:
        users_input = input(prompt)
        if len(users_input) > 0 and users_input.isalpha():
            break
    return users_input

# ensuring the user enters an integer
def read_integer(prompt):
    while True:
        try:
            users_input = int(input(prompt))
            if users_input >= 0:
                return users_input
        except ValueError:
            # spelling change here
            print("Sorry number only please")
