import pytest
import datetime 
import db 
import analytics

def test_habit_mark_complete(habit):
    habit.mark_complete()
    assert len(habit.completed_at) == 1
    assert habit.completed_at[0] == datetime.now()

def test_habit_get_streak(habit):
    assert habit.get_streak() == 0
    habit.completed_at = [datetime.now()]
    assert habit.get_streak() == 1

def test_habit_tracker_create_habit(tracker):
    tracker.create_habit('Exercise', 'daily')
    assert len(tracker.habits) == 1
    assert tracker.habits[0].name == 'Exercise'
    assert tracker.habits[0].period == 'daily'

def test_habit_tracker_delete_habit(tracker):
    tracker.create_habit('Exercise', 'daily')
    assert len(tracker.habits) == 1
    tracker.delete_habit('Exercise')
    assert len(tracker.habits) == 0

def test_habit_tracker_get_habits(tracker):
    tracker.create_habit('Exercise', 'daily')
    tracker.create_habit('Meditate', 'daily')
    assert len(tracker.get_habits()) == 2

def test_habit_tracker_get_habits_by_period(tracker):
    tracker.create_habit('Exercise', 'daily')
    tracker.create_habit('Meditate', 'daily')
    tracker.create_habit('Read', 'weekly')
    assert len(tracker.get_habits_by_period('daily')) == 2
    assert len(tracker.get_habits_by_period('weekly')) == 1
    
def test_get_longest_streak(tracker):
    tracker.create_habit('Exercise', 'daily')
    tracker.create_habit('Meditate', 'daily')
    tracker.create_habit('Read', 'weekly')
    tracker.habits[0].completed_at = [datetime.now()]
    tracker.habits[1].completed_at = [datetime.now(), datetime.now()]
    tracker.habits[2].completed_at = [datetime.now(), datetime.now(), datetime.now()]
    assert tracker.get_longest_streak().name == 'Read'
    
def test_get_longest_streak_by_habit(tracker):
    tracker.create_habit('Exercise', 'daily')
    tracker.create_habit('Meditate', 'daily')
    tracker.create_habit('Read', 'weekly')
    tracker.habits[0].completed_at = [datetime.now()]
    tracker.habits[1].completed_at = [datetime.now(), datetime.now()]
    tracker.habits[2].completed_at = [datetime.now(), datetime.now(), datetime.now()]
    assert tracker.get_longest_streak_by_habit('Exercise') == 1
    assert tracker.get_longest_streak_by_habit('Meditate') == 2
    assert tracker.get_longest_streak_by_habit('Read') == 3
    assert tracker.get_longest_streak_by_habit('Write') == 0
    

