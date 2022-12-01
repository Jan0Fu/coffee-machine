import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_res(drink):
    return drink["ingredients"]["water"] <= resources["water"]\
           and drink["ingredients"]["milk"] <= resources["milk"] \
           and drink["ingredients"]["coffee"] <= resources["coffee"]


def check_value():
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    value = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return value

loop_breaker = False

while not loop_breaker:
    user_input = input("What would you like? (espresso/latte/capuccino): ")
    if user_input == "report":
        report()
    if not check_res(user_input):
        print("Sorry, not enough resources")
    else:
        print("Please insert coins")
        if check_value() >= MENU[user_input]["cost"]:
            print(f"Here is {check_value() - MENU[user_input]['cost']}")
            profit += MENU[user_input]["cost"]
            print(f"Here is your {user_input} Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")










