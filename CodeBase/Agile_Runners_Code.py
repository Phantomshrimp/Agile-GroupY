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
    races_eta = []
    for line in lines:
        split_line = line.split(',')
        # ======= split the name of the races for opening by the first word only
        races_location.append(split_line[0])
        races_eta.append(float(split_line[1]))
    return races_location, races_eta

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

# ======================== Option 2 Functions ===========================
# another look at the race input is needed
# this may need to be looke at
def users_venue(races_location, races_eta, runners_id):
    while True:
        user_location = read_nonempty_string("Where will the new race take place?: ").capitalize()
        user_eta = float(input("How long should the race take on average?: "))
        if user_location not in races_location:
            break
    connection = open(f"{user_location}.txt", "a")
    races_location.append(user_location)
    races_eta.append(user_eta)
    time_taken = []
    updated_runners = []
    for i in range(len(runners_id)):
        time_taken_for_runner = read_integer(f"Time for {runners_id[i]}>> ")
        # !!! FIRST BUG found on debug == changed = 0 to != 0
        if time_taken_for_runner != 0:
            time_taken.append(time_taken_for_runner)
            updated_runners.append(runners_id[i])
            print(f"{runners_id[i]},{time_taken_for_runner}", file=connection)
    connection.close()

# now including the eta of a race when editing the races.txt file
def updating_races_file(races_location, races_eta):
    connection = open(f"races.txt", "w")
    for i in range(len(races_location)):
        print(f"{races_location[i]}, {races_eta[i]}", file=connection)
    connection.close()


# ==================== Option 3 ====================================
# code was missing the call for other county codes number 5 I think

# THIRD CHANGE === fixed list out of index range
# the issue was the \n was still being attached to the id
def runners_data():
    with open("runners.txt") as input:
        lines = input.readlines()
    runners_name = []
    runners_id = []
    for line in lines:
        split_line = line.split(',')
        runners_name.append(split_line[0])
        runners_id.append(split_line[1].strip('\n'))
    return runners_name, runners_id

def competitors_by_county(name, id):
    print()
    print("=" * 20)
    print("Cork runners")
    print("-" * 20)
    for i in range(len(name)):
        if id[i].startswith("CK"):
            print(f"{name[i]} ({id[i]})")
    print()
    print("=" * 20)
    print("Kerry runners")
    print("-" * 20)
    for i in range(len(name)):
        if id[i].startswith("KY"):
            print(f"{name[i]} ({id[i]})")
    print()
    print("=" * 20)
    print("Limerick runners")
    print("-" * 20)
    for i in range(len(name)):
        if id[i].startswith("LK"):
            print(f"{name[i]} ({id[i]})")
    print()
    print("=" * 20)
    print("Tipperary runners")
    print("-" * 20)
    for i in range(len(name)):
        if id[i].startswith("TP"):
            print(f"{name[i]} ({id[i]})")
    print()
    print("=" * 20)
    print("Waterford runners")
    print("-" * 20)
    for i in range(len(name)):
        if id[i].startswith("WD"):
            print(f"{name[i]} ({id[i]})")

# ========================== OPTION 4 =========================
def displaying_winners_of_each_race(races_location):
    # Changed Looser to Winner - the times were double checked
    print("Venue             Winner")
    print("="*24)
    for i in range(len(races_location)):
        id, time_taken = reading_race_results(races_location[i])
        fastest_runner = winner_of_race(id, time_taken)
        print(f"{races_location[i]:<18s}{fastest_runner}")


# ================= Option 5 ===========================
def relevant_runner_info(runners_name, runners_id):
    for i in range(len(runners_name)):
        # added in a runner id in case two runners names were the same
        # for example - there are two Des Kelly-s one cork, one waterford
        print(f"{i + 1}: {runners_name[i]} {runners_id[i]}")
    user_input = read_integer_between_numbers("Which Runner > ", 1, len(runners_name))
    runner = runners_name[user_input - 1]
    id = runners_id[user_input -1]
    return runner, id

def reading_race_results_of_relevant_runner(location, runner_id):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        id.append(split_line[0])
        time_taken.append(int(split_line[1].strip("\n")))
    for i in range(len(id)):
        if runner_id == id[i]:
            time_relevant_runner = time_taken[i]
            return time_relevant_runner
    return None

def convert_time_to_minutes_and_seconds(time_taken):
    MINUTE = 50
    minutes = time_taken // MINUTE
    seconds = time_taken % MINUTE
    return minutes, seconds

def sorting_where_runner_came_in_race(location, time):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        t = int(split_line[1].strip("\n"))
        time_taken.append(t)

    time_taken.sort()
    return time_taken.index(time) + 1, len(lines)

def displaying_race_times_one_competitor(races_location, runner, id):
    print(f"{runner} ({id})")
    print(f"-"*35)
    for i in range(len(races_location)):
        time_taken = reading_race_results_of_relevant_runner(races_location[i], id)
        if time_taken is not None:
            minutes, seconds = convert_time_to_minutes_and_seconds(time_taken)
            came_in_race, number_in_race = sorting_where_runner_came_in_race(races_location[i], time_taken)
            print(f"{races_location[i]} {minutes} mins {seconds} secs ({came_in_race} of {number_in_race})")

# ============================== OPTION 6 ====================================
def finding_name_of_winner(fastest_runner, id, runners_name):
    runner = ""
    for i in range(len(id)):
        if fastest_runner == id[i]:
            runner = runners_name[i]
    return runner



# bug here was in glengarriff where KY-12 was entered as 0 incorrectly
def displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id):
    print(f"The following runners have all won at least one race:")
    print(f"-" * 55)
    winners = []
    runners = []
    for i, location in enumerate(races_location):
        id, time_taken = reading_race_results(location)
        fastest_runner = winner_of_race(id, time_taken)
        name_of_runner = finding_name_of_winner(fastest_runner, runners_id, runners_name)
        if fastest_runner not in winners:
            winners.append(fastest_runner)
            runners.append(name_of_runner)
    for i, fastest_runner in enumerate(winners):
        print(f"{runners[i]} ({fastest_runner})")

# ==================== Create a Placeholder Menu =========================
def main():
    races_location, races_eta = race_venues()
    runners_name, runners_id = runners_data()
    MENU = "1. Show the results for a race \n2. Add results for a race \n3. Show all competitors by county " \
           "\n4. Show the winner of each race \n5. Show all the race times for one competitor " \
           "\n6. Show all competitors who have won a race \n7. Upcoming features \n8. Quit \n>>> "
    input_menu = read_integer_between_numbers(MENU, 1, 8)
    # 2nd mistake found on debugger (= 7 changed to <= 7)
    # changed the menu list to 8 to accommodate the missing function
    while input_menu <= 8:
        if input_menu == 1:
            id, time_taken, venue = race_results(races_location)
            fastest_runner = winner_of_race(id, time_taken)
            display_races(id, time_taken, venue, fastest_runner)
        elif input_menu == 2:
            users_venue(races_location, races_eta, runners_id)
        elif input_menu == 3:
            competitors_by_county(runners_name, runners_id)
        elif input_menu == 4:
            displaying_winners_of_each_race(races_location)
        elif input_menu == 5:
            runner, id = relevant_runner_info(runners_name, runners_id)
            displaying_race_times_one_competitor(races_location, runner, id)
        elif input_menu == 6:
            displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)
        elif input_menu == 7:
            print("=" * 20)
            print('COMING SOON')
            print("=" * 20)
            print("Option to see which runners did not reach the podium")
            print("Rumour has it, there may even be a dark mode of the app coming... shhhhh")
            print("Yaml check")
        # added a quitting message
        # took out placeholder messages
        else:
            print('Thank you for using the program. Goodbye!')
            break
        print()
        input_menu = read_integer_between_numbers(MENU, 1, 8)
    updating_races_file(races_location, races_eta)


main()


