from coffee_machine_utility_functions import *
from ascii_art import *

coffee_machine_ON = True
print(logo)
while coffee_machine_ON:
    user_input = input("\nWhat would you like?\nType '1' for Espresso\nType '2' for Latte\nType '3' for Cappuccino"
                       "\n\nEnter your choice :").lower()

    if user_input in ["1", "2", "3", "report", "off"]:

        if user_input == "report":
            print_report()

        elif user_input in ["1", "2", "3"]:
            coffee_choice = get_coffee_choice(user_input)
            sufficient_resources = are_resources_sufficient(coffee_choice)

            if sufficient_resources:
                cost = get_coffee_cost(coffee_choice)
                print("\nInsert coins:")
                money_inserted = insert_money()
                try_transaction(coffee_choice, money_inserted, cost)

        elif user_input == "off":
            coffee_machine_ON = False
    else:
        print(f"\n{'+' * 40}")
        print("Kindly enter a valid input")
        print(f"{'+' * 40}")
