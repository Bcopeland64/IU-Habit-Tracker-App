from db import HabitDB, get_db_connection
from habit import Habit
from datetime import datetime

# Example habits to test analytics
habits = [
    Habit('Drink water', 'daily'),
    Habit('Go for a run', 'weekly'),
    Habit('Read a book', 'monthly')
]

# Save the habits to the database
for habit in habits:
    habit.save()

# Example function to get the completion rate for a habit
def get_completion_rate(habit, start_date, end_date):
    """_summary_

    Args:
        habit (_str_): _description_
        start_date (_datetime_): _lists start dates_
        end_date (_datetime_): _lists end dates_

    Returns:
        _str_: _returns a string with number of completions divided by total habits_
    """
    with get_db_connection() as conn:
        cursor = conn.execute(
            'SELECT COUNT(*) FROM habits_completed WHERE habit_id=? AND date_completed BETWEEN ? AND ?',
            (habit.id, start_date, end_date))
        count = cursor.fetchone()[0]
        total = (end_date - start_date).days + 1
        return count / total

# Example usage of the get_completion_rate function
today = datetime.date.today()
start_date = today - datetime.timedelta(days=30)
end_date = today
for habit in habits:
    completion_rate = get_completion_rate(habit, start_date, end_date)
    print(f'{habit.name} completion rate: {completion_rate:.2f}')
