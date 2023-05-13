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
}
#quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
ballance = 0

userChoice = input("What would you like? (espresso/latte/cappuccino):").lower()

if(userChoice == 'report'):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${ballance}")
    
# uncomment this when the playgame() function is created.
# if(userChoice == 'off'):
#     print("Good bye.")
    # return    
    