#!/usr/bin/env python3

import pytest
from habit import Habit
import database
import pytest

def test_habit_exists():
    assert database.habit_exists('main.db', 'test') == False
    
def test_add_habit():        
    assert database.add('main.db', 'test', 'test', 'Daily', '10/20/2022', 0) == True
    
def test_remove_habit():
    assert database.remove('main.db', 'test') == True
    
def test_update_duration():   
    assert database.update_duration('main.db', 'test', 'Weekly') == True            

def test_update_streak():
    assert database.update_streak('main.db', 'test', 1) == True
    
def test_update_start_time():
    assert database.update_start_time('main.db', 'test', '10/20/2022') == True
    
def test_get_all_habits():
    assert database.get_all_habits('main.db') == [('test', 'test', 'Weekly', '10/20/2022', 1)]
    
def test_daily_duration_list():
    assert database.daily_duration_list('main.db', 'Daily') == [('test', 'test', 'Weekly', '10/20/2022', 1)]
    
def test_weekly_duration_list():
    assert database.weekly_duration_list('main.db', 'Weekly') == [('test', 'test', 'Weekly', '10/20/2022', 1)]
    
def test_monthly_duration_list():
    assert database.monthly_duration_list('main.db', 'Monthly') == []
    
def test_longest_streak():
    assert database.longest_streak('main.db', 1) == [('test', 'test', 'Weekly', '10/20/2022', 1)]   
    
def test_list_habit_data():
    assert database.list_habit_data('main.db', 'test') == [('test', 'test', 'Weekly', '10/20/2022', 1)]
    
def test_get_streak():
    assert database.get_streak('main.db', 'test') == 1
    
def test_get_duration():
    assert database.get_duration('main.db', 'test') == 'Weekly'
    
def test_get_start_time():
    assert database.get_start_time('main.db', 'test') == '10/20/2022'
    
def test_get_description():
    assert database.get_description('main.db', 'test') == 'test'    
    
def test_get_habit():    
    assert database.get_habit('main.db', 'test') == 'test'
    
