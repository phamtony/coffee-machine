from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = True

while coffee_machine:
    coffee_service = True
    menu_list = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while coffee_service:
        user_input = input(f"What would you like? ({menu_list.get_items()}) ")

        if user_input == "off":
            coffee_service = False
            coffee_machine = False
        elif user_input == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink_details = menu_list.find_drink(order_name=user_input)

            if drink_details:
                sufficient_resource = coffee_maker.is_resource_sufficient(drink=drink_details)

                if sufficient_resource:
                    sufficient_money = money_machine.make_payment(drink_details.cost)

                    if sufficient_money:
                        coffee_maker.make_coffee(drink_details)