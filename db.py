import sqlite3
from datetime import datetime
from habit import Habit

class HabitDB:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency
        self.completed = []
        
    
    def mark_complete(self):
        """_summary_This method marks a habit as complete"""
        today = datetime.date.today()
        self.completed.append(today)

    def is_complete(self):
        """_summary_This method checks if a habit is complete

        Returns:
            _str_: _list of completed habits_
        """
        if self.frequency == 'daily':
            return datetime.date.today() in self.completed
        elif self.frequency == 'weekly':
            start_of_week = (datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday()))
            end_of_week = start_of_week + datetime.timedelta(days=6)
            for day in range((end_of_week - start_of_week).days + 1):
                date = start_of_week + datetime.timedelta(days=day)
                if date in self.completed:
                    return True
            return False
        elif self.frequency == 'monthly':
            today = datetime.date.today()
            if today.day >= 28:
                end_of_month = today.replace(day=28) + datetime.timedelta(days=4)
                for day in range((end_of_month - today).days + 1):
                    date = today + datetime.timedelta(days=day)
                    if date in self.completed:
                        return True
                return False
            else:
                return today.replace(day=1) in self.completed

    def delete(self):
        """_summary_This method deletes a habit"""
        with sqlite3.connect('habits.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM habits WHERE name = ?', (self.name,))

    @staticmethod
    def list_by_frequency(frequency):
        """_summary_

        Args:
            frequency (_datetime_): _daily, weekly, monthly periodicity_

        Returns:
            _str_: _list of habit frequencies_
        """
        with sqlite3.connect('habits.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT name FROM habits WHERE frequency = ?', (frequency,))
            return [row[0] for row in cursor.fetchall()]

    def save(self):
        """_summary_This method saves a habit"""
        with sqlite3.connect('habits.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO habits (name, frequency, completed) VALUES (?, ?, ?)', (self.name, str(self.frequency), str(self.completed)))


    def update(self):
        """_summary_This method updates a habit"""
        with sqlite3.connect('habits.db') as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE habits SET completed = ? WHERE name = ?', (self.completed, self.name))

    @staticmethod
    def get_all_habits():
        """_summary_This method gets all habits

        Returns:
            _str_: _list of all habits created_
        """
        with sqlite3.connect('habits.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT name, frequency, completed FROM habits')
            rows = cursor.fetchall()
            habits = []
            for row in rows:
                habit = Habit(row[0], row[1])
                habit.completed = [datetime.date.fromisoformat(date_str) for date_str in row[2].split(',')]
                habits.append(habit)
            return habits

def create_table():
    """_summary_This method creates a table"""
    with sqlite3.connect('habits.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS habits
                          (name TEXT PRIMARY KEY, frequency TEXT, completed TEXT)''')

def get_db_connection():
    """_summary_This method gets the database connection

    Returns:
        _conn_: _establishes an sqlite3 connection_
    """
    
    return sqlite3.connect('habits.db')