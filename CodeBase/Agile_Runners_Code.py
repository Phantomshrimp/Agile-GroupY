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

# ==================== Create a Placeholder Menu =========================
def main():
    MENU = "1. Show the results for a race \n2. Add results for a race \n3. Show all competitors by county " \
           "\n4. Show the winner of each race \n5. Show all the race times for one competitor " \
           "\n6. Show all competitors who have won a race \n7. Quit \n>>> "
    input_menu = read_integer_between_numbers(MENU, 1, 7)
    # 2nd mistake found on debugger (= 7 changed to <= 7)
    while input_menu <= 7:
        if input_menu == 1:
            # id, time_taken, venue = race_results(races_location)
            # fastest_runner = winner_of_race(id, time_taken)
            # display_races(id, time_taken, venue, fastest_runner)
            print("Option 1")
        elif input_menu == 2:
            # users_venue(races_location, runners_id)
            print("option 2")
        elif input_menu == 3:
            # competitors_by_county(runners_name, runners_id)
            print("Option 3")
        elif input_menu == 4:
            # displaying_winners_of_each_race(races_location)
            print("Option 4")
        elif input_menu == 5:
            # runner, id = relevant_runner_info(runners_name, runners_id)
            # displaying_race_times_one_competitor(races_location, runner, id)
            print("Option 5")
        elif input_menu == 6:
            # displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)
        # added a quitting message
            print("Option 6")
        else:
            print('Thank you for using the program. Goodbye!')
            break
        print()
        input_menu = read_integer_between_numbers(MENU, 1, 7)
    # updating_races_file(races_location)


main()

