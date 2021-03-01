from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

KEEP_WORKING = True
ingredients_information = CoffeeMaker()
money_operations = MoneyMachine()
user_drink = Menu()

while KEEP_WORKING:
    drinks_that_can_be_made = Menu()
    user_choice = input(f'What would you like? ({drinks_that_can_be_made.get_items()}): ').lower()
    
    if user_choice == 'off':
        print('Coffee machine is off')
        KEEP_WORKING = False
    elif user_choice == 'report':
        ingredients_information.report()
        money_operations.report()
    else:
        user_drink_name = user_drink.find_drink(user_choice)

        if user_drink_name is None:
            continue
        else:
            ingredients_are_ok = ingredients_information.is_resource_sufficient(user_drink_name)

        if ingredients_are_ok:
            user_drink_cost = user_drink_name.cost
            payment_process = money_operations.make_payment(user_drink_cost)

            if payment_process:
                ingredients_information.make_coffee(user_drink_name)
