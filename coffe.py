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
    "water": 30,
    "milk": 200,
    "coffee": 100,
}
#quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
ballance = 0
isMachineOn = True

    
while isMachineOn == True:
    userChoice = input("\nWhat would you like? (espresso/latte/cappuccino):").lower()

    def check_resources(item=userChoice,resources=resources,MENU=MENU): 
       #check if item requirement is satisfied by resources 
       
       if resources['water'] < MENU[item]['ingredients']['water']:
           print("Sorry, There is not enough water.")
           return
       elif resources['coffee'] < MENU[item]['ingredients']['coffee']:
           print("Sorry, There is not enough coffee.") 
           return
       elif resources['milk'] < MENU[item]['ingredients']['milk']:
           print("Sorry, There is not enough milk.")
           return       
        
        
    if userChoice =='off':
        print('good bye!')
        isMachineOn = False 

    elif(userChoice == 'report'):
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${ballance}")
        
    elif userChoice not in MENU:
       print('no such option')
       
    else:
        check_resources()
        
 
