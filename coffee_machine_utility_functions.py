import os
from menu import *
from ascii_art import *

profit = 0


def print_report():
    """This function prints the report of the resources currently available in the coffee machine"""
    print(f"\n{'-' * 40}")
    print(f"{' ' * 17}REPORT{' ' * 17}")
    print(f"{'-' * 40}")
    print(f"Water  : {resources['water']}"
          f"\nMilk   : {resources['milk']}"
          f"\nCoffee : {resources['coffee']}"
          f"\nMoney  : {profit}")
    print(f"{'-' * 40}")


def get_coffee_choice(user_input):
    """This function takes user_input(1, 2 or 3) as string returns the name of the coffee that the user has selected"""
    if user_input == "1":
        return "espresso"
    elif user_input == "2":
        return "latte"
    else:
        return "cappuccino"
