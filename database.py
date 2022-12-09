#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:13:06 2022

@author: brandon
"""
import sqlite3
from datetime import date


def establish_connection(name='main.db'):
    """Creates a connection to the database

    Args:
        name (str, optional): _description_. Defaults to 'main.db'.

    Returns:
        _type_: _description_
    """
    db = sqlite3.connect(name)
    create_table(db)
    return db

def create_table(db):
    """Creates a table in the database

    Args:
        db (sqlite3.connect): _description_
    """
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS habits (
        habit TEXT PRIMARY KEY,
        name TEXT, 
        description TEXT, 
        duration TEXT,
        habit_type TEXT, 
        start_time TEXT,
        end_time TEXT, 
        streak INTEGER)''')
    db.commit()
    
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS habit_log (
        habit TEXT,
        finished BOOL, 
        streak INTEGER default 0,
        end_time TEXT,
        foreign key (habit) references habits(habit))''')
    db.commit()
    
    
def add(db, name, description, duration, start_time, streak):
    """Adds a habit to the database

    Args:
        db (sqlite3.connect): _description_
        name (str): _description_
        description (str): _description_
        duration (str): _description_
        start_time (str): _description_
        streak (int): _description_
    """
    cursor = db.cursor()
    cursor.execute('''INSERT INTO habits (name, description, duration, start_time, streak) VALUES (?, ?, ?, ?, ?)''', (name, description, duration, start_time, streak))
    db.commit()
    
    
def update_habit_log(db, name, finished, streak, end_time):
    """Updates the habit log

    Args:
        db (sqlite3.connect): _description_
        name (str): _description_
        finished (bool): _description_
        streak (int): _description_
        end_time (str): _description_
    """
    cursor = db.cursor()
    cursor.execute('''INSERT INTO habit_log (habit, finished, streak, end_time) VALUES (?, ?, ?, ?)''', (name, finished, streak, end_time))
    db.commit()
    
    
def habit_exists(db, name):
    """Checks if the habit exists in the database

    Args:
        db (sqlite3.connect): _description_
        name (str): _description_

    Returns:
        bool: _description_
    """
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM habits WHERE name = ?''', (name,))
    if cursor.fetchone() is not None:
        return True
    else:
        return False
    
def update_duration(db, name, duration):
    """Updates the duration of the habit

    Args:
        db (sqlite3.connect): _description_
        name (str): _description_
        duration (str): _description_
    """
    cursor = db.cursor()
    cursor.execute('''UPDATE habits SET duration = ? WHERE name = ?''', (duration, name))
    db.commit()
    
    
def get_streak(db, name):
    """Gets the streak of the habit

    Args:
        db (sqlite3.connect): _description_
        name (str): _description_

    Returns:
        int: _description_
    """
    cursor = db.cursor()
    cursor.execute('''SELECT streak FROM habits WHERE name = ?''', (name,))
    return cursor.fetchone()[0]

def update_streak(db, name, streak):
    """Updates the streak of the habit

    Args:
        db (sqlite3.connect): _description_
        name (str): _description_
        streak (int): _description_
    """
    cursor = db.cursor()
    cursor.execute('''UPDATE habits SET streak = ? WHERE name = ?''', (streak, name))
    db.commit()
    
    
def remove(db, name):
    """Removes the habit from the database

    Args:
        db (sqlite3.connect): _description_
        name (str): _description_
    """
    cursor = db.cursor()
    cursor.execute('''DELETE FROM habits WHERE name = ?''', (name,))
    db.commit()
    
    
def get_categories(db):
    """Gets the categories of the habits

    Args:
        db (sqlite3.connect): _description_

    Returns:
        list: _description_
    """
    cursor = db.cursor()
    cursor.execute('''SELECT DISTINCT category FROM habits''')
    return cursor.fetchall()

def delete_habit_type(db, habit_type):
    """Deletes the habit type from the database

    Args:
        db (sqlite3.connect): _description_
        habit_type (str): _description_
    """
    cursor = db.cursor()
    cursor.execute('''DELETE FROM habits WHERE habit_type = ?''', (habit_type,))
    db.commit()
    
    
def update_habit_duration(db, name, duration):
    """Updates the duration of the habit

    Args:
        db (sqlite3.connect): _description_
        name (str): _description_
        duration (str): _description_
    """
    cursor = db.cursor()
    cursor.execute('''UPDATE habits SET duration = ? WHERE name = ?''', (duration, name))
    db.commit()
    
    
def get_habit_duration(db, name):
    """Gets the duration of the habit

    Args:
        db (sqlite3.connect): _description_
        name (str): _description_

    Returns:
        str: _description_
    """
    cursor = db.cursor()
    cursor.execute('''SELECT duration FROM habits WHERE name = ?''', (name,))
    return cursor.fetchone()[0]

def reset_habit_log(db, name):
    """Resets the habit log

    Args:
        db (sqlite3.connect): _description_
        name (str): _description_
    """
    cursor = db.cursor()
    cursor.execute('''DELETE FROM habit_log WHERE habit = ?''', (name,))
    db.commit()
    
    
def get_habit_end_time(db, name):
    """Gets the end time of the habit

    Args:
        db (sqlite3.connect): _description_
        name (str): _description_

    Returns:
        str: _description_
    """
    cursor = db.cursor()
    cursor.execute('''SELECT end_time FROM habits WHERE name = ?''', (name,))
    return cursor.fetchone()[0]

def get_habit_duration(db, name):
    """Gets the duration of the habit

    Args:
        db (sqlite3.connect): _description_
        name (str): _description_

    Returns:
        str: _description_
    """
    cursor = db.cursor()
    cursor.execute('''SELECT duration FROM habits WHERE name = ?''', (name,))
    return cursor.fetchone()[0]
        