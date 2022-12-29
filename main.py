#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:09:18 2022

@author: brandon
"""

import questionary as qt
from datetime import date
from habit import *
from analytics import *

#Welcome message
print('Welcome to your Habit Tracker App!')
print('Remember to stay consistent and keep up the good work!')
print('You must add a habit before you can view any data.')

#Create Interface   
def interface():
    choices = qt.select("What would you like to do?", 
        choices=["Add a habit",
                 "Remove a habit", 
                 "View all habits", 
                 "View habit data", 
                 "View longest streak", 
                 "View daily habits", 
                 "View weekly habits", 
                 "View monthly habits", 
                 "Exit"]).ask()
    
   #Add Habit 
    if choices == "Add a habit":
        description = qt.select("Choose a habit type?", choices=["Physical Habit", "Educational Habit", "Other Habit"]).ask()
        duration = qt.select("Choose a duration?", choices=["Daily", "Weekly", "Monthly"]).ask()
        name = qt.text("What is the name of the habit you want to add?").ask()        
        habit = Habit(name, description, duration)
        habit.add_habit()


#Remove Habit
    if choices == "Remove a habit":
        name = qt.text("What is the name of the habit you want to remove?").ask()
        habit = Habit(name, description, duration)
        habit.remove_habit()

#View all habits
    if choices == "View all habits":
        conn = establish_connection('main.db')
        habits = get_all_habits(conn)
        print(habits)

#View habit data    
    if choices == "View habit data":
        name = qt.text("What is the name of the habit you want to view?").ask()
        habit_name = Habit(name, description, duration)
        habit_data = list_habit_data(conn, habit_name)
    
        print(habit_data)

#View longest streak
    if choices == "View longest streak":
        conn = establish_connection('main.db')
        streak = update_streak()
        longest_streak = longest_streak(conn, streak)
        print(longest_streak)

#View daily habits
    if choices == "View daily habits":
        conn = establish_connection('main.db')
        duration_list = daily_duration_list(conn, duration)
        print(duration_list)

#View weekly habits

    if choices == "View weekly habits": 
        conn = establish_connection('main.db')
        duration_list = weekly_duration_list(conn, duration)
        print(duration_list)

#View monthly habits
    if choices == "View monthly habits":    
        conn = establish_connection('main.db')
        duration_list = monthly_duration_list(conn, duration)
        

    
    elif choices == "Exit":
     exit()
               
if __name__ == "__main__":
    while True:
        interface() 
   





