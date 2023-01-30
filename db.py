import sqlite3
import datetime
from habit import Habit


class HabitDB:
    def establish_a_connection(self):
        self.conn = sqlite3.connect('habits.db')
        self.cursor = self.conn.cursor()

    # Create habits table if it does not exist
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                period TEXT NOT NULL,
                created_at DATETIME NOT NULL
            )''')

    # Create completions table if it does not exist 
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS completions ( 
                habit_id INTEGER NOT NULL, 
                completed_at DATETIME NOT NULL, 
                FOREIGN KEY(habit_id) REFERENCES habits(id) ON 
                DELETE CASCADE  //added ON DELETE CASCADE to delete the related entries in completions when a row in habits is deleted 
            )''')

    def create_habit(self, name: str, period: str):
        self.cursor.execute(
            'INSERT INTO habits (name, period, created_at) VALUES (?, ?, ?)',
            (name, period, datetime.now())
        )
        self.conn.commit()

    def delete_habit(self, name: str):
        self.cursor.execute(
            'DELETE FROM habits WHERE name=?',
            (name,)
        )
        self.conn.commit()

    def mark_complete(self, name: str):
        self.cursor.execute(
            'SELECT id FROM habits WHERE name=?',
            (name,)
        )
        habit_id = self.cursor.fetchone()[0]
        self.cursor.execute(
            'INSERT INTO completions (habit_id, completed_at) VALUES (?, ?)',
            (habit_id, datetime.now())
        )
        self.conn.commit()

    def mark_incomplete(self, name: str):
        self.cursor.execute(
            'SELECT id FROM habits WHERE name=?',
            (name,)
        )
        habit_id = self.cursor.fetchone()[0]
        self.cursor.execute(
            'DELETE FROM completions WHERE habit_id=? ORDER BY completed_at DESC LIMIT 1',
            (habit_id,)
        )
        self.conn.commit()

    def get_habits(self):
        self.cursor.execute('SELECT * FROM habits')
        rows = self.cursor.fetchall()
        habits = []
        for row in rows:
            id, name, period, created_at = row
            self.cursor.execute(
                'SELECT completed_at FROM completions WHERE habit_id=?',
                (id,))
            completed_at_rows = self.cursor.fetchall()
            completed_at = [row[0] for row in completed_at_rows]
            habits.append(Habit(id, name, period, created_at, completed_at))
        return habits

    def get_habits_by_period(self, period: str):
        self.cursor.execute('SELECT * FROM habits WHERE period=?', (period,))
        rows = self.cursor.fetchall()
        habits = []
        for row in rows:
            id, name, _, created_at = row
            self.cursor.execute(
                'SELECT completed_at FROM completions WHERE habit_id=?',
                (id,)
            )
            completed_at_rows = self.cursor.fetchall()
