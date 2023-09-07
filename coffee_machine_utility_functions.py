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


