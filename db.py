import sqlite3
from datetime import datetime, timedelta


class Habit:
    def __init__(self, name="", frequency="", completed=[]):
        self.name = name
        self.frequency = frequency
        self.completed = []

    def mark_complete(self):
        """marks habit as complete for today"""
        today = datetime.today().date()
        self.completed.append(today)

    def is_complete(self):
        """marks habit as complete for today

        Returns:
            _str_: _returns completed habits_
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


class HabitDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS habits
                        (name TEXT PRIMARY KEY, frequency TEXT, completed TEXT)''')

    def __del__(self):
        self.conn.close()

    def add_habit(self, habit):
        """_adds a habit to the database

        Args:
            habit (_str_): _adds a habit with frequency and default completed values_
        """
        self.cursor.execute('INSERT INTO habits (name, frequency, completed) VALUES (?, ?, ?)',
                            (habit.name, habit.frequency, habit.completed))
        self.conn.commit()

    def delete_habit(self, habit_name):
        """removes a habit from the database

        Args:
            habit_name (_str_): _will delete string values listed as habits from the database_
        """
        self.cursor.execute('DELETE FROM habits WHERE name = ?', (habit_name,))
        self.conn.commit()

    def update_habit(self, habit):
        """udpates a habit in the database

        Args:
            habit (_type_): _description_
        """
        self.cursor.execute('UPDATE habits SET completed = ? WHERE name = ?', (str(habit.completed), habit.name))
        self.conn.commit()

    def get_all_habits(self):
        """gets all habits from the database

        Returns:
            _str_: _gets list of all habits created_
        """
        self.cursor.execute('SELECT name, frequency, completed FROM habits')
        rows = self.cursor.fetchall()
        habits = []
        for row in rows:
            habit = Habit(row[0], row[1])
            habit.completed = [datetime.date.fromisoformat(date_str) for date_str in row[2].split(',')]
            habits.append(habit)
        return [Habit(row[0], row[1], row[2]) for row in self.cursor.fetchall()]


    def list_by_frequency(self, frequency):
        """_summary_

        Args:
            frequency (_type_): _description_

        Returns:
            _str_: _lists all habits plus their frequency_
        """
        self.cursor.execute('SELECT name FROM habits WHERE frequency = ?', (frequency,))
        return [row[0] for row in self.cursor.fetchall()]

    def get_streak(self, habit_name):
        """_summary_

        Args:
            habit_name (_type_): _description_

        Returns:
            _type_: _returns streak of all habits_
        """
        streak = 0
        today = datetime.today().date()
        for day in range((today - timedelta(days=30)).days, (today - timedelta(days=1)).days + 1):
            date = today - timedelta(days=day)
            habit = self.get_habit(habit_name)
            if habit and date in habit.completed:
                streak += 1
            else:
                break
        return streak

    def get_habit(self, habit_name):
        """gets a habit from the database

        Args:
            habit_name (_type_): _description_
        """
        self.cursor.execute('SELECT name, frequency, completed FROM habits WHERE name = ?', (habit_name,))
        row = self.cursor.fetchone()
        if row is None:
            return
        
    def save(self):
        """saves the database
        """
        self.conn.commit()
        
    def is_complete(self, habit_name):
        """_summary_

        Args:
            habit_name (_type_): _description_

        Returns:
            _bool_: _returns whether a habit is complete by true or false_
        """
        habit = self.get_habit(habit_name)
        if habit:
            return habit.is_complete()
        return False
