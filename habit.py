from datetime import datetime, date

class Habit:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency
        self.completed = []

    def mark_complete(self):
        """This method marks a habit as complete"""
        today = datetime.now()
        self.completed.append(today)
        
    def mark_incomplete(self):
        """_summary_This method marks a habit as incomplete"""
        today = datetime.now()
        self.completed.remove(today)
        

    def is_complete(self):
        """_summary_This method checks if a habit is complete

        Returns:
            _datetime_: _description_The date the habit was completed"""
            
        if self.frequency == 'daily':
            return datetime.now() in self.completed
        elif self.frequency == 'weekly':
            start_of_week = (datetime.date.now() - datetime.timedelta(days=datetime.now().weekday()))
            end_of_week = start_of_week + datetime.timedelta(days=6)
            for day in range((end_of_week - start_of_week).days + 1):
                date = start_of_week + datetime.timedelta(days=day)
                if date in self.completed:
                    return True
            return False
        elif self.frequency == 'monthly':
            today = datetime.now()
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
        del self
        

    @staticmethod
    def list_by_frequency(habits, frequency):
        """_summary_

        Args:
            habits (_str_): _string of habits_
            frequency (_datetime_): _datetime object_

        Returns:
            __: _list of habits with periodicity_
        """
        
        result = []
        for habit in habits:
            if habit.frequency == frequency:
                result.append(habit.name)
        return result
    
    def list_all(habits):
        """_summary_

        Args:
            habits (_str_): _list of habits_

        Returns:
            _str_: _list of habits_
        """
        result = []
        for habit in habits:
            result.append(habit.name)
        return result
    
    
