import unittest
from habit import Habit
from datetime import datetime


class TestHabit(unittest.TestCase):
    """_summary_This class tests the Habit class

    Args:
        unittest (_type_): _creates testing class_
    """
    def test_create_habit(self):
        """_summary_This method tests the creation of a habit"""
        h = Habit('Drink 8 glasses of water', 'daily')
        self.assertEqual(h.name, 'Drink 8 glasses of water')
        self.assertEqual(h.frequency, 'daily')
        self.assertFalse(h.completed)

    def test_mark_habit_complete(self):
        """_summary_This method tests the marking of a habit as complete"""
        h = Habit('Go for a walk', 'daily')
        h.mark_complete()
        self.assertTrue(h.completed)

         
    def test_is_complete_daily(self):
        """_summary_This method tests the is_complete method"""
        h = Habit('Go for a walk', 'daily')
        h.mark_complete()
        self.assertTrue(h.completed)
        
    def test_is_complete_weekly(self):
        """_summary_This method tests the is_complete method"""
        h = Habit('Go for a walk', 'weekly')
        h.mark_complete()
        self.assertTrue(h.completed)
        
    def test_is_complete_monthly(self):
        """_summary_This method tests the is_complete method"""
        h = Habit('Go for a walk', 'monthly')
        h.mark_complete()
        self.assertTrue(h.completed)
        
    def test_list_by_frequency(self):
        """_summary_This method tests the list_by_frequency method"""
        h = Habit('Go for a walk', 'daily')
        h.mark_complete()
        self.assertTrue(h.completed)
        
    def test_list_all(self):
        """_summary_This method tests the list_all method"""
        h = Habit('Go for a walk', 'daily')
        h.mark_complete()
        self.assertTrue(h.completed)


if __name__ == '__main__':
    unittest.main()
