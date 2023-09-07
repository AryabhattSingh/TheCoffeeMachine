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


def get_coffee_cost(coffee_choice):
    """This function takes coffee name as parameter and returns the cost of the coffee"""
    return MENU[coffee_choice]['cost']


def print_warning_message():
    """This function prints warning message if user enters non-numeric inputs"""
    print(f"\n{'+' * 40}")
    print("Kindly enter integer value only.")
    print(f"{'+' * 40}\n")


def take_input(coin_name):
    """This function take the name of the coin(either Quarters, Dimes, Nickels or Pennies) as a parameter and return
     the count of the coins as input by the user"""
    coin_value = ""
    while not coin_value.isnumeric():
        coin_value = input(f"How many {coin_name}? : ")
        if not coin_value.isnumeric():
            print_warning_message()
    return int(coin_value)


def insert_money():
    """This function prompts the user to enter different types of coins, and it returns the total value of all the coins
    inserted by the user"""
    quarters = take_input("Quarters")
    dimes = take_input("Dimes")
    nickels = take_input("Nickels")
    pennies = take_input("Pennies")

    if quarters >= 0 and dimes >= 0 and nickels >= 0 and pennies >= 0:
        return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    else:
        print(f"\n{'+' * 40}")
        print("Kindly enter only positive value.")
        print(f"{'+' * 40}")
