'''
File: greeter_and_age_math.py
Author: Phillip Bridgeman
Date: November 11, 2025
Description: A simple program that greets the user and performs age-related calculations.
Version: 1.0.0
Copyright: Copyright (c) 2025 Phillip Bridgeman
License: MIT License
'''
import datetime

def greet_user(name):
    """Greets the user by name."""
    return f"Hello, {name}! Welcome!"

name = input("Enter your name: ")
print(greet_user(name))
birth_date = input("Enter your birth date (dd/mm/yyyy): ")

def calculate_age(birth_date):
    """Calculates the user's age in years. Based on string input of birth date."""
    day, month, year = map(int, birth_date.split("/"))
    # Check for valid date
    if not (1 <= day <= 31 and 1 <= month <= 12 and year > 0):
        return "Invalid date format. Please use dd/mm/yyyy."
    birth_date = datetime.date(year, month, day)
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

age = calculate_age(birth_date)
print(f"You are {age} years old.")

def age_in_days(age):
    """Calculates the user's age in days."""
    return age * 365

age_days = age_in_days(age)
print(f"You are {age_days} days old.")