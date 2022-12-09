#!/usr/bin/env python3

import pytest
from habit import Habit
import database

def db():
    db = database.establish_connection('test.db')
    return db

def test_add():
    habit = Habit('test', 'test', 'Daily', db())
    habit.add_habit()
    assert database.habit_exists(db(), 'test') is True
    
def test_remove():
    habit = Habit('test', 'test', 'Daily', db())
    habit.remove_habit()
    assert database.habit_exists(db(), 'test') is False
    
def test_change_duration():
    habit = Habit('test', 'test', 'Daily', db())
    habit.add_habit()
    habit.duration = 'Weekly'
    habit.change_duration()
    assert database.get_duration(db(), 'test') == 'Weekly'
    
def test_increment_habit_duration():
    habit = Habit('test', 'test', 'Daily', db())
    habit.add_habit()
    habit.increment_habit_duration()
    assert database.get_streak(db(), 'test') == 1
    
def test_decrement_habit_duration():
    habit = Habit('test', 'test', 'Daily', db())
    habit.add_habit()
    habit.increment_habit_duration()
    habit.decrement_habit_duration()
    assert database.get_streak(db(), 'test') == 0
    
def test_reset_habit_streak():
    habit = Habit('test', 'test', 'Daily', db())
    habit.add_habit()
    habit.increment_habit_duration()
    habit.reset_habit_streak()
    assert database.get_streak(db(), 'test') == 0
    
def test_update_habit_streak():
    habit = Habit('test', 'test', 'Daily', db())
    habit.add_habit()
    habit.increment_habit_duration()
    habit.update_habit_streak()
    assert database.get_streak(db(), 'test') == 1
    
def test_habit_check_daily():
    habit = Habit('test', 'test', 'Daily', db())
    habit.add_habit()
    habit.habit_check()
    assert database.get_streak(db(), 'test') == 1
    
def test_habit_check_weekly_missed():
    habit = Habit('test', 'test', 'Weekly', db())
    habit.add_habit()
    habit.habit_check()
    habit.habit_check()
    assert database.get_streak(db(), 'test') == 0
    
def test_habit_check_monthly():
    habit = Habit('test', 'test', 'Monthly', db())
    habit.add_habit()
    habit.habit_check()
    assert database.get_streak(db(), 'test') == 1
    

    


