#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:10:58 2022

@author: brandon
"""
from datetime import date
from datetime import datetime
from analytics import *
from database import *

class Habit: 
    
    def __init__(self, name: str = None, description: str = None, duration: str = None, database = 'main.db'):
        """
        Initializes a habit
        
        Params:
        ++++++++
        
        Name: Name of the habit
        Description: Description of the habit
        Duration: Duration of the habit
        Database: Database to store the habit 
        Streak: Sets the habit streak number
        Start Time: Sets the habit start time   
       
        """
            
        self.name = name
        self.description = description
        self.duration = duration
        self.database = establish_connection('main.db')
        self.streak = 0
        self.start_time = date.today().strftime("%m/%d/%Y")
        
    def add_habit(self):
        if habit_exists(self.database, self.name) is False:
            self.database.add(self.database, self.name, self.description,
                              self.duration, self.start_time, self.streak)
            print(
                f'{self.name} has been added to the database as a {self.duration} habit starting on {self.start_time}\n')
            
        else: 
            print(f'{self.name} already exists in the database\n')
            
    
    def remove_habit(self):
        if habit_exists(self.database, self.name) is True:
            self.database.remove(self.database, self.name)
            print(f'{self.name} has been removed from the database\n')
            
        else: 
            print(f'{self.name} does not exist in the database\n')
            
            
    def change_duration(self):
        self.database.update_duration(self.db, self.name, self.duration)
        print(f'{self.name} has been updated to a {self.duration} habit\n')
        
        
    def increment_habit_duration(self):
        self.streak = self.database.get_streak(self.database, self.name)
        self.streak += 1
        
        
    def decrement_habit_duration(self):
        self.streak = self.database.get_streak(self.database, self.name)
        self.streak -= 1
        print(f'{self.name} has been reset to zero.\n')
        
        
    def reset_habit_streak(self):
        self.streak = 0
        self.database.update_streak(self.database, self.name, self.streak, self.start_time)
        print(f'{self.name} has been reset to zero because you missed your habit streak.\n')
        
        
    def update_habit_streak(self):
        self.streak = self.database.get_streak(self.database, self.name)
        self.database.update_streak(self.database, self.name, self.streak, self.start_time)
        print(f'{self.name} has been updated to a streak of {self.streak}\n')
        
        
    def habit_check(self):
        if self.duration == 'daily':
            self.increment_habit_duration()
            self.update_habit_streak()
            
        elif self.duration == 'weekly':
            if date.today().weekday() == 0:
                self.increment_habit_duration()
                self.update_habit_streak()
                
            else:
                self.decrement_habit_duration()
                self.reset_habit_streak()
                
        elif self.duration == 'monthly':
            if date.today().day == 1:
                self.increment_habit_duration()
                self.update_habit_streak()
                
            else:
                self.decrement_habit_duration()
                self.reset_habit_streak()
                
        else:
            print('Invalid duration')
            
            
    def habit_verifier(self):
        pass
    
   
        
            
    
        


        
        
        
        
        
    
        
        
        
        
        
        
    
        
        
       
        
    

