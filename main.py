"""
function about user info
"""

import datetime


def get_year_of_birth(age):
    """Get the year"""
    current_year = datetime.date.today().year
    return current_year - age


def hello_user(name):
    """Greeting with the user"""
    return "Hello, " + name + "! "


def get_age_user(age):
    """Getting the user's age"""
    return "You are " + str(age) + '. '


def get_year_user(age):
    """Getting the user's year of birth"""
    year_of_birth = get_year_of_birth(age)
    return "You were born in " + str(year_of_birth) + '.'


def get_ifo_about_user(name, age):
    """Getting full information about the user"""
    return hello_user(name) + get_age_user(age) + get_year_user(age)
