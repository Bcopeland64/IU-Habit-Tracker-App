#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:12:02 2022

@author: brandon
"""
from database import *

def get_all_habits(db):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM habits')
    habits_list = cursor.fetchall()
    return habits_list

def daily_duration_list(db, duration):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM habits WHERE duration = "Daily"')
    duration_list = cursor.fetchall()
    return duration_list

def weekly_duration_list(db, duration):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM habits WHERE duration = "Weekly"')
    duration_list = cursor.fetchall()
    return duration_list

def monthly_duration_list(db, duration):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM habits WHERE duration = "Monthly"')
    duration_list = cursor.fetchall()
    return duration_list

def longest_streak(db, streak):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM habits WHERE streak = (SELECT MAX(streak) FROM habits)')
    longest_streak = cursor.fetchall()
    return longest_streak

def list_habit_data(db, name):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM habits WHERE habit = ?', (name,))
    habit_data = cursor.fetchall()
    return habit_data


    
