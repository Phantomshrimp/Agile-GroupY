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

# 3GG ============= Functions for 1st Option =============================
def race_results(races_location):
    for i in range(len(races_location)):
        # changed the output to display starting with number 1
        print(f"{i+1}: {races_location[i]}")
    user_input = read_integer_between_numbers("Choice > ", 1, len(races_location))
    venue = races_location[user_input -1]
    id, time_taken = reading_race_results(venue)
    return id, time_taken, venue

def race_venues():
    with open("races.txt") as input:
        lines = input.readlines()
    races_location = []
    for line in lines:
        split_line = line.split(',')
        # ======= split the name of the races for opening by the first word only
        races_location.append(split_line[0])
    return races_location

def winner_of_race(id, time_taken):
    quickest_time = min(time_taken)
    winner = ""
    for i in range(len(id)):
        if quickest_time == time_taken[i]:
            winner = id[i]
    return winner

def display_races(id, time_taken, venue, fastest_runner):
    MINUTE = 50
    print(f"Results for {venue}")
    print(f"="*37)
    minutes = []
    seconds = []
    for i in range(len(time_taken)):
        minutes.append(time_taken[i] // MINUTE)
        seconds.append(time_taken[i] % MINUTE)
    for i in range(len(id)):
        print(f"{id[i]:<10s} {minutes[i]} minutes and {seconds[i]} seconds")
    print(f"{fastest_runner} won the race.")

def reading_race_results(location):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        split_line = line.split(",")
        id.append(split_line[0].strip('\n'))
        time_taken.append(int(split_line[1].strip('\n')))
    return id, time_taken
# ======================== OPTION 1 WORKING =============================


# ==================== Create a Placeholder Menu =========================
def main():
    races_location = race_venues()
    #runners_name, runners_id = runners_data()
    MENU = "1. Show the results for a race \n2. Add results for a race \n3. Show all competitors by county " \
           "\n4. Show the winner of each race \n5. Show all the race times for one competitor " \
           "\n6. Show all competitors who have won a race \n7. Quit \n>>> "
    input_menu = read_integer_between_numbers(MENU, 1, 7)
    # 2nd mistake found on debugger (= 7 changed to <= 7)
    while input_menu <= 7:
        if input_menu == 1:
            id, time_taken, venue = race_results(races_location)
            fastest_runner = winner_of_race(id, time_taken)
            display_races(id, time_taken, venue, fastest_runner)
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

