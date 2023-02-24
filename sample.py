from datetime import datetime, timedelta
from habit import HabitDB, Habit

def get_daily_habits_completed_today():
    """provides the user with a sample of the habits completed today

    Returns:
        _type_: _description_
    """
    today = datetime.today().date()
    habit_db = HabitDB()
    habits = habit_db.get_all_habits()
    completed_habits = []
    for habit in habits:
        if habit.frequency == 'daily' and today in habit.completed:
            completed_habits.append(habit)
    return completed_habits

def get_weekly_habits_completed_this_week():
    """provide a user with a sample of the habits completed this week

    Returns:
        _type_: _description_
    """
    start_of_week = (datetime.today().date() - timedelta(days=datetime.today().date().weekday()))
    end_of_week = start_of_week + timedelta(days=6)
    habit_db = HabitDB()
    habits = habit_db.get_all_habits()
    completed_habits = []
    for habit in habits:
        if habit.frequency == 'weekly':
            for day in range((end_of_week - start_of_week).days + 1):
                date = start_of_week + timedelta(days=day)
                if date in habit.completed:
                    completed_habits.append(habit)
    return completed_habits

def get_monthly_habits_completed_this_month():
    """provides a user with a sample of the habits completed this month

    Returns:
        _type_: _description_
    """
    today = datetime.today().date()
    habit_db = HabitDB()
    habits = habit_db.get_all_habits()
    completed_habits = []
    for habit in habits:
        if habit.frequency == 'monthly':
            if today.day >= 28:
                end_of_month = today.replace(day=28) + timedelta(days=4)
                for day in range((end_of_month - today).days + 1):
                    date = today + timedelta(days=day)
                    if date in habit.completed:
                        completed_habits.append(habit)
            else:
                if today.replace(day=1) in habit.completed:
                    completed_habits.append(habit)
    return completed_habits
