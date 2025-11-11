'''
File: greeter_and_age_math.py
Author: Phillip Bridgeman
Date: November 11, 2025
Description: A simple program that greets the user and performs age-related calculations.
Version: 1.1.0
License: MIT
'''
from __future__ import annotations
from datetime import date

def greet_user(name: str) -> str:
    """Greets the user by name."""
    name = name.strip() or "friend"
    return f"Hello, {name}! Welcome!"

def parse_birthdate_ddmmyyyy(text: str) -> date:
    """Parse 'dd/mm/yyyy' into a date object. Raises ValueError on invalid input."""
    parts = text.strip().split("/")
    if len(parts) != 3:
        raise ValueError("Please enter your birth date as dd/mm/yyyy.")
    try:
        day, month, year = (int(p) for p in parts)
    except ValueError:
        raise ValueError("Day, month, and year must be numbers (dd/mm/yyyy).")
    bd = date(year, month, day)  # may raise ValueError (invalid calendar date)
    if bd > date.today():
        raise ValueError("Birth date cannot be in the future.")
    return bd

def compute_age_years(birth_date: date, today: date | None = None) -> int:
    """Exact age in whole years as of 'today'."""
    today = today or date.today()
    years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return years

def approx_age_days(birth_date: date, today: date | None = None) -> int:
    """Approximate days lived using a date delta (better than years*365)."""
    today = today or date.today()
    return (today - birth_date).days

def ask_for_birthdate() -> date:
    while True:
        raw = input("Enter your birth date (dd/mm/yyyy): ")
        try:
            return parse_birthdate_ddmmyyyy(raw)
        except ValueError as e:
            print(f"❌ {e}")
            print("Please try again.\n")

def main() -> None:
    name = input("Enter your name: ")
    print(greet_user(name))
    today = date.today()
    bd = ask_for_birthdate()

    years = compute_age_years(bd)
    months = (today.year - bd.year) * 12 + (today.month - bd.month)
    if today.day < bd.day:
        months -= 1
    days = approx_age_days(bd)

    print(f"You are {years} years old.")
    print(f"You are about {months} months old.")
    print(f"You are about {days} days old.")

if __name__ == "__main__":
    main()
