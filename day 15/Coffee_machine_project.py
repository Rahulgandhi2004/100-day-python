import time
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money":0,
}

profit=0

def check_ingredients(drink):
    ingredients=MENU[drink]["ingredients"]
    a=[]
    for item in ingredients:
        if ingredients[item]>resources.get(item,0):
            print(f"Sorry.😓, {item} is not available.🙊")
            return False

        else:
            time.sleep(1)
            print(f"{item} is 🤫available.")
            a.append(item)
            if len(ingredients)==len(a):
                time.sleep(1)
                print("All items are available.💕")
                return True
    return None
def coffe_image():
    time.sleep(1)
    print("      )  (")
    time.sleep(1)
    print("     (   ) )")
    time.sleep(1)
    print("      ) ( (")
    time.sleep(1)
    print("    _______)_")
    time.sleep(1)
    print(" .-'---------|")
    time.sleep(1)
    print("( C|/\\/\\/\\/\\|")
    time.sleep(1)
    print(" '-./\\/\\/\\/\\|")
    time.sleep(1)
    print("   '_________'")
    time.sleep(1)
    print("    '-------'")
    time.sleep(1)

def coin_insert(coffe_type):

    if check_ingredients(coffe_type):
        ingredients = MENU[coffe_type]["ingredients"]
        coffe_cost = MENU[coffe_type]["cost"]
        time.sleep(2)
        print(f"Plz insert the amount🫴 of espresso {coffe_cost}$")
        time.sleep(2)
        quarters=int(input("how many 🪙quarter?:"))
        time.sleep(1)
        dimes=int(input("how many 🤑dimes?:"))
        time.sleep(1)
        nicks=int(input("how many 💰nickles?:"))
        time.sleep(1)
        pennies=int(input("how many 🟨pennies?:"))
        time.sleep(2)
        entered_amount=quarters*0.25+dimes*0.10+nicks*0.05+pennies*0.01
        if coffe_cost<=entered_amount:
            print(f"{coffe_type} 🔃is preparing...")
            coffe_image()
            time.sleep(1)
            global profit
            profit+=coffe_cost
            for item in ingredients:
                resources[item]-=MENU[coffe_type]["ingredients"][item]
            print(f"{coffe_type} is Ready💐...Have a good day!")
            time.sleep(2)
            print(f"Your balance 💸is {entered_amount-coffe_cost}$")
            time.sleep(2)

        else:
            print(f"Your amount is not enough,insert the balance{coffe_cost-entered_amount}$ or Select another one or Return back your amount")


is_on = True
while is_on:
    choice=input("What would you like? (espresso🐦‍🔥/latte👌/cappuccino💕):")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water🫗: {resources['water']}ml")
        print(f"Milk🥛: {resources['milk']}ml")
        print(f"Coffee🍵: {resources['coffee']}ml")
        print(f"Money💰: {profit}")
    elif choice=="espresso":
        coin_insert(choice)
    elif choice=="latte":
        coin_insert(choice)
    elif choice=="cappuccino":
        coin_insert(choice)



