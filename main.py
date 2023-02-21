import datetime
import questionary
from db import HabitDB
from habit import Habit

def main():
    """This is the main entry point of the program"""
    while True:
        choices = [
            {'name': 'Create a habit', 'value': create_habit},
            {'name': 'List habits', 'value': list_habits},
            {'name': 'Mark habit complete', 'value': mark_complete},
            {'name': 'Mark habit incomplete', 'value': mark_incomplete},
            {'name': 'Delete a habit', 'value': delete_habit},
            {'name': 'Exit', 'value': exit}
        ]
        choice = questionary.select('What would you like to do?', choices=choices).ask()

        if choice:
            choice()

def create_habit():
    """This function creates a habit"""
    name = questionary.text('Enter the name of the habit:').ask()
    frequency = questionary.select('How often should this habit be completed?', choices=['daily', 'weekly', 'monthly']).ask()
    completed = False
    habit = HabitDB(name, frequency)
    habit.save()
    print(f'Habit "{name}" with frequency "{frequency}" created successfully!')

def list_habits():
    """This function lists all habits"""
    habits = Habit.list_all()
    for habit in habits:
        print(f'{habit.name} ({habit.frequency} days) - {"Complete" if habit.completed else "Incomplete"}')

def mark_complete():
    """This function marks a habit as complete"""
    habits = Habit.list_all()
    habit_choices = [{'name': habit.name, 'value': habit} for habit in habits]
    habit = questionary.select('Which habit would you like to mark as complete?', choices=habit_choices).ask()
    habit.mark_complete()
    print(f'Habit "{habit.name}" marked as complete!')

def mark_incomplete():
    """This function marks a habit as incomplete"""
    habits = Habit.list_all()
    habit_choices = [{'name': habit.name, 'value': habit} for habit in habits]
    habit = questionary.select('Which habit would you like to mark as incomplete?', choices=habit_choices).ask()
    habit.mark_incomplete()
    print(f'Habit "{habit.name}" marked as incomplete!')

def delete_habit():
    """This function deletes a habit"""
    habits = Habit.list_all()
    habit_choices = [{'name': habit.name, 'value': habit} for habit in habits]
    habit = questionary.select('Which habit would you like to delete?', choices=habit_choices).ask()
    habit.delete()
    print(f'Habit "{habit.name}" deleted successfully!')
    
def help():
    """This function displays the help menu"""
    print('''
    This is a habit tracker app. You can use it to create habits, mark them as complete, and delete them.
    ''')
    
def list_commands():
    """This function lists all commands"""
    print('''
    create_habit - Create a habit
    list_habits - List all habits
    mark_complete - Mark a habit as complete
    mark_incomplete - Mark a habit as incomplete
    delete_habit - Delete a habit
    help - Display the help menu
    list_commands - List all commands
    exit - Exit the app
    ''')

if __name__ == '__main__':
    main()
