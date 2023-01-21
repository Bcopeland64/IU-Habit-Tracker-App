from datetime import datetime


class Habit:
    def __init__(self, name: str, period: str):
        self.name = name
        self.period = period
        self.created_at = datetime.now()
        self.completed_at = []
    
    def mark_complete(self):
        self.completed_at.append(datetime.now())
        
    def mark_incomplete(self):
        self.completed_at.pop()
    
    def get_streak(self):
        if not self.completed_at:
            return 0
        current_streak = 1
        for i in range(1, len(self.completed_at)):
            if self.completed_at[i] - self.completed_at[i-1] == self.period:
                current_streak += 1
            else:
                break
        return current_streak

class HabitTracker:
    def __init__(self):
        self.habits = []
    
    def create_habit(self, name: str, period: str):
        new_habit = Habit(name, period)
        self.habits.append(new_habit)
    
    def delete_habit(self, name: str):
        for i, habit in enumerate(self.habits):
            if habit.name == name:
                del self.habits[i]
                break
    
    def get_habits(self):
        return self.habits
    
    def get_habits_by_period(self, period: str):
        return [habit for habit in self.habits if habit.period == period]
    
    def get_longest_streak(self):
        longest_streak = 0
        longest_streak_habit = None
        for habit in self.habits:
            streak = habit.get_streak()
            if streak > longest_streak:
                longest_streak = streak
                longest_streak_habit = habit
        return longest_streak_habit
    
    def get_longest_streak_by_habit(self, name: str):
        for habit in self.habits:
            if habit.name == name:
                return habit.get_streak()
        return 0
    
    def mark_complete(self, name: str):
        for habit in self.habits:
            if habit.name == name:
                habit.mark_complete()
                break
            
    def mark_incomplete(self, name: str):
        for i, completed_at in enumerate(self.completed_at):
            if self.name == name:
                del self.completed_at[i] 
            
    def relationships(self):
        for habit in self.habits:
            print(habit.name, habit.get_streak())       
            
