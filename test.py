import unittest
import sqlite3
from datetime import datetime
from habit import Habit, HabitDB


class TestHabitTracker(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.db = HabitDB()
        cls.db.cursor.execute('DELETE FROM habits')
        cls.habit1 = Habit('Drink water', 'daily')
        cls.habit2 = Habit('Read a book', 'weekly')
        cls.db.save_habit(cls.habit1)
        cls.db.save_habit(cls.habit2)

    @classmethod
    def tearDownClass(cls):
        cls.db.cursor.execute('DELETE FROM habits')
        cls.db.conn.close()

    def test_save_habit(self):
        habit = Habit('Exercise', 'daily')
        self.db.save_habit(habit)
        self.assertTrue('Exercise' in [row[0] for row in self.db.get_all_habits()])
        
    def test_update_habit(self):
        self.habit1.mark_complete()
        self.db.update_habit(self.habit1)
        self.assertTrue(self.habit1.is_complete())
        self.assertFalse(self.habit2.is_complete())

    
    def test_delete_habit(self):
        habit = Habit('Exercise', 'daily')
        self.db.save_habit(habit)
        self.db.delete_habit(habit)
        self.assertFalse('Exercise' in [row[0] for row in self.db.get_all_habits()])

    def test_list_habits_by_frequency(self):
        daily_habits = self.db.list_habits_by_frequency('daily')
        weekly_habits = self.db.list_habits_by_frequency('weekly')
        self.assertEqual(len(daily_habits), 1)
        self.assertEqual(len(weekly_habits), 1)
        self.assertEqual(daily_habits[0].name, 'Drink water')
        self.assertEqual(weekly_habits[0].name, 'Read a book')

    def test_is_complete(self):
        self.assertFalse(self.habit1.is_complete())
        self.assertFalse(self.habit2.is_complete())
        self.habit1.mark_complete()
        self.assertTrue(self.habit1.is_complete())
        self.assertFalse(self.habit2.is_complete())

    def test_get_streak(self):
        self.assertEqual(Habit.get_streak(), 0)
        self.habit1.mark_complete()
        self.assertEqual(Habit.get_streak(), 1)


if __name__ == '__main__':
    unittest.main()
