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
isMachineOn = True

    
    
while isMachineOn == True:
    userChoice = input("\nWhat would you like? (espresso/latte/cappuccino):").lower()

    def check_resources(item=userChoice,resources=resources,MENU=MENU): 
       #check if item requirement is satisfied by resources 
       areResourcesSufficient = True
       #retrieve ingredients dictionary 
       ingredients = MENU[item]['ingredients']
       for ingredient, quantity in ingredients.items():
                    
           if resources[ingredient] < quantity:
               areResourcesSufficient = False
               print(f"Sorry, there is not enough {ingredient}")        
       return areResourcesSufficient       
       
       
 
        
        
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
     if   check_resources():
         #process payment
         user_inserted_value = 0
         quarters = int(input('how many quarters?'))
         user_inserted_value += quarters * 0.25
         dimes = int(input('How many dimes?'))
         user_inserted_value += dimes * 0.10
         nickles = int(input('how many nickles?'))
         user_inserted_value += nickles * 0.05
         pennies = int(input('how many pennies'))
         user_inserted_value += pennies * 0.01
         if user_inserted_value < MENU[userChoice]['cost']:
             print(f"Sorry, not enough money.${user_inserted_value} Refunded.")
         elif user_inserted_value > MENU[userChoice]['cost']:
              ballance += MENU[userChoice]['cost']
              change = round(user_inserted_value - MENU[userChoice]['cost'],2) 
              print(f"here is your ${change} dollars in change.")   
             
            
 
