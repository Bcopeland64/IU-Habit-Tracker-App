from habit import HabitDB, Habit
from questionary import prompt, select, text

def create_habit():
    """creates a habit"""
    # Get input from user
    name = input("Enter habit name: ")
    frequency = input("Enter habit frequency: ")
    completed = False

    # Create habit object
    habit = Habit(name, frequency, completed)

    # Save habit to database
    habit.save_habit()  # pass habit object to save_habit method
    print(f"Habit '{name}' created successfully")


def mark_habit_complete():
    """marks a habit as complete"""
    db = HabitDB()
    habits = db.get_all_habits()
    if habits:
        print("Select the habit you want to mark as complete:")
        for habit in habits:
            print(habit)

        habit_id = int(input())  # user selects habit by id
        for habit in habits:
            if habit.id == habit_id:
                habit.completed = True
                habit.save_habit()  # update habit in database
                print(f"Marked {habit.name} as complete!")
                break
        else:
            print("Invalid selection.")
    else:
        print("There are no habits to mark as complete.")

def delete_habit():
    """deletes a habit"""
    db = HabitDB()
    habits = db.get_all_habits()
    if not habits:
        print("You don't have any habits to delete.")
        return
    print("Which habit would you like to delete?")
    for i, habit in enumerate(habits):
        print(f"{i + 1}. {habit[1]}")
    habit_index = int(input("> ")) - 1
    habit_id = habits[habit_index][0]
    db.delete_habit(habit_id)
    print(f"Habit '{habits[habit_index][1]}' deleted.")


def list_habits():
    """Lists all habits"""
    frequency = select("Which frequency do you want to list habits for?", choices=["daily", "weekly", "monthly"]).ask()
    habits = HabitDB.list_habits_by_frequency(frequency)
    if not habits:
        print(f"No habits found with frequency '{frequency}'")
    else:
        print(f"Habits with frequency '{frequency}':")
        for habit in habits:
            print(habit)

def get_streak():
    """gets the streak for a habit"""
    habits = HabitDB.get_all_habits()
    habit_names = [habit.name for habit in habits]
    habit_name = select("Which habit do you want to get the streak for?", choices=habit_names).ask()
    habit = next(filter(lambda h: h.name == habit_name, habits))
    streak = habit.get_streak()
    print(f"The streak for habit '{habit_name}' is {streak} days")
    
def save_habit():
    """saves a habit to the database"""
    # Get input from user
    name = input("Enter habit name: ")
    frequency = input("Enter habit frequency: ")
    completed = False

    # Create habit object
    habit = Habit(name, frequency, completed)

    # Save habit to database
    habit.save_habit()  # pass habit object to save_habit method
    
def help():
    """generates help text"""
    print("Commands:")
    print("create_habit - create a habit")
    print("mark_habit_complete - mark a habit as complete")
    print("delete_habit - delete a habit")
    print("list_habits - list all habits")
    print("get_streak - get the streak for a habit")
    print("exit - exit the program")

if __name__ == "__main__":
    help()
    while True:
        command = select("What would you like to do?", choices=["create_habit", "mark_habit_complete", "delete_habit", "list_habits", "get_streak", "exit"]).ask()
        if command == "create_habit":
            create_habit()
        elif command == "mark_habit_complete":
            mark_habit_complete()
        elif command == "delete_habit":
            delete_habit()
        elif command == "list_habits":
            list_habits()
        elif command == "get_streak":
            get_streak()
        elif command == "exit":
            break
        else:
            print("Invalid command")
    