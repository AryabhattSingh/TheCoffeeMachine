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


def are_resources_sufficient(coffee_choice):
    """This functions takes the coffee choice as parameter, and returns a boolean, after checking whether the current
    available resources are enough to make the selected coffee"""
    coffee_details = MENU[coffee_choice]
    required_ingredients = coffee_details['ingredients']
    for item in required_ingredients:
        if required_ingredients[item] > resources[item]:
            print(f"\n{'-' * 35}")
            print(f"Sorry, there is NOT enough {item}")
            print(f"{'-' * 35}")
            return False
    return True
