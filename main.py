import click
from habit import HabitTracker
import questionary
from db import *

tracker = HabitTracker()

@click.group()
def cli():
    pass

@cli.command()
def create():
    name = questionary.text("Enter the habit name: ").ask()
    period = questionary.select("Enter the habit period:", choices=["daily", "weekly"]).ask()
    tracker.create_habit(name, period)
    click.echo(f'Habit "{name}" with period "{period}" created successfully!')

@cli.command()
def delete():
    name = questionary.text("Enter the habit name: ").ask()
    tracker.delete_habit(name)
    click.echo(f'Habit "{name}" deleted successfully!')

@cli.command()
def list():
    habits = tracker.get_habits()
    click.echo('Current habits:')
    for habit in habits:
        click.echo(f'- {habit.name} ({habit.period})')

@cli.command()
def list_period():
    period = questionary.select("Enter the habit period:", choices=["daily", "weekly", "monthly"]).ask()
    habits = tracker.get_habits_by_period(period)
    click.echo(f'Current {period} habits:')
    for habit in habits:
        click.echo(f'- {habit.name}')

@cli.command()
def longest_streak():
    longest_streak_habit = tracker.get_longest_streak()
    if longest_streak_habit:
        click.echo(f'Habit with longest streak: {longest_streak_habit.name} ({longest_streak_habit.get_streak()})')
    else:
        click.echo('No habits with a streak.')

@cli.command()
def longest_streak_habit():
    name = questionary.text("Enter the habit name: ").ask()
    streak = tracker.get_longest_streak_by_habit(name)
    if streak:
        click.echo(f'Longest streak for habit "{name}": {streak}')
    else:
        click.echo(f'Habit "{name}" not found.')
        
@cli.command()
def mark():
    name = questionary.text("Enter the habit name: ").ask()
    tracker.mark_complete(name)
    click.echo(f'Habit "{name}" marked successfully!')
    
@cli.command()
def unmark():
    name = questionary.text("Enter the habit name: ").ask()
    tracker.mark_incomplete(name)
    click.echo(f'Habit "{name}" unmarked successfully!')

if __name__ == '__main__':
    cli()


def main():
    while True:
        command = input('Enter a command (create, delete, list, list-period, longest-streak, longest-streak-habit, or exit): ')
        if command == 'create':
            name = input('Enter the habit name: ')
            period = input('Enter the habit period (daily or weekly): ')
            tracker.create_habit(name, period)
            click.echo(f'Habit "{name}" with period "{period}" created successfully!')
        elif command == 'delete':
            name = input('Enter the habit name: ')
            tracker.delete_habit(name)
            click.echo(f'Habit "{name}" deleted successfully!')
        elif command == 'list':
            habits = tracker.get_habits()
            click.echo('Current habits:')
            for habit in habits:
                click.echo(f'- {habit.name} ({habit.period})')
