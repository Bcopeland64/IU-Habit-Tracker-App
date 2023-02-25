import sqlite3
from datetime import datetime, timedelta

class Habit:
    def __init__(self, name="", frequency="", completed=[]):
        """_summary_

        Args:
            name (str, optional): _description_. Defaults to "".
            frequency (str, optional): _description_. Defaults to "".
            completed (list, optional): _description_. Defaults to [].
        """
        self.name = name
        self.frequency = frequency
        self.completed = datetime.date()
        
    def __str__(self):
        return self.name
    
    def mark_complete(self):
        """marks habit as complete for today"""
        today = datetime.today().date()
        self.completed.append(today)
    
    def is_complete(self):
        """marks habit as complete for today

        Returns:
            _datetime_: _returns datetime completion date_
        """
        if self.frequency == 'daily':
            return datetime.today().date() in self.completed
        elif self.frequency == 'weekly':
            start_of_week = (datetime.today().date() - timedelta(days=datetime.today().date().weekday()))
            end_of_week = start_of_week + timedelta(days=6)
            for day in range((end_of_week - start_of_week).days + 1):
                date = start_of_week + timedelta(days=day)
                if date in self.completed:
                    return True
            return False
        elif self.frequency == 'monthly':
            today = datetime.today().date()
            if today.day >= 28:
                end_of_month = today.replace(day=28) + timedelta(days=4)
                for day in range((end_of_month - today).days + 1):
                    date = today + timedelta(days=day)
                    if date in self.completed:
                        return True
                return False
            else:
                return today.replace(day=1) in self.completed
    
    def get_streak():
        """_summary_

        Returns:
            _str_: _returns list of habit streaks_
        """
        streak = 0
        today = datetime.today().date()
        habit_db = HabitDB()
        habits = habit_db.get_all_habits()
        for habit in habits:
            if today in habit.completed:
                streak += 1
            else:
                break
        return streak
    
    def save_habit(self):
        """save a habit to the database"""
        db = HabitDB()
        db.save_habit(self)

class HabitDB:
    def __init__(self, name="", frequency="", completed=[]):
        self.conn = sqlite3.connect('habits.db')
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        """creates a table in the database"""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS habits
                          (name TEXT PRIMARY KEY, frequency TEXT, completed TEXT)''')
    
    def save_habit(self, habit):
        """saves a habit to the database

        Args:
            habit (_str_): _saves a habit to the database in string format_
        """
        with self.conn:
            self.cursor.execute('INSERT INTO habits (name, frequency, completed) VALUES (?, ?, ?)', (habit.name, habit.frequency, str(habit.completed)))

        
    
    def update_habit(self, habit):
        """updates a habit in the database

        Args:
            habit (_str_): _updates a habit as a string in the database_
        """
        self.cursor.execute('UPDATE habits SET completed = ? WHERE name = ?', (str(habit.completed), habit.name))
        self.conn.commit()
    
    def delete_habit(self, habit):
        """delete a habit from the database

        Args:
            habit (_str_): _deletes a habit as a string from the database_
        """
        self.cursor.execute('DELETE FROM habits WHERE name = ?', (habit.name,))
        self.conn.commit()
    
    @staticmethod
    def list_habits_by_frequency(frequency):
        """lists habits by frequency

        Args:
            frequency (_str_): _inputs frequency by daily, weekly, or monthly_

        Returns:
            _str_: _list of habits by frequency_
        """
        with sqlite3.connect("habits.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM habits WHERE frequency=?", (frequency,))
            rows = c.fetchall()
            habits = [Habit(*row) for row in rows]
            return habits
    
    def get_all_habits(self):
        """gets all habits from the database

        Returns:
            _str_: _list of all habits_
        """
        self.cursor.execute('SELECT * FROM habits')
        rows = list(self.cursor.fetchall())
        return rows
    
    
