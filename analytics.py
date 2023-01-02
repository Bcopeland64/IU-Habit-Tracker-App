from typing import List
from habit import HabitTracker
from habit import Habit
import db

def get_all_habits(tracker: HabitTracker) -> List[Habit]:
    return tracker.get_habits()

def get_habits_by_period(tracker: HabitTracker, period: str) -> List[Habit]:
    return tracker.get_habits_by_period(period)

def get_longest_streak(tracker: HabitTracker) -> Habit:
    return tracker.get_longest_streak()

def get_longest_streak_by_habit(tracker: HabitTracker, name: str) -> int:
    return tracker.get_longest_streak_by
