#constants
HEAT_CAPACIY_WATER = 4.184
HEAT_OF_FUSION_WATER = 334

print("Welcome to the DIY Tea & Juice Maker!")
base = int(input(
        "What kind of base do you want? \
        Please enter 1 for milk or 2 for fruit: "))

#defines the drink for the final output
if base == 1:
    Lactose_Tolerance = input(
        "Do you have lactose intolerance? y for yes, n for no: ")
    
    if Lactose_Tolerance == "y":
        milk = input(
            "Do you want soy milk or oat milk? \
            Please type in your choice [soy/oat]: ")
    else:
        milk = "regular"
    
    drink = milk + " milk"
else:
    fruit = input(
        "Which fruit do you want? \
        Please type in your choice [mango/strawberry]: ")
    
    drink = fruit + "juice" #same variable name to be used at the end

#pick the tea
tea = input(
    "From the following tea type:\n- No Tea\n- Black Tea\n- Green Tea\n\
    - Matcha\nPlease choose a tea type: ")

#checks if matcha was chosen with fruit, proceeds otherswise
if base == 2 and tea == "Matcha":
    print("Invalid choice! End of the program")
else:
    toppings = input(
        "From the following toppings:\n- No Topping\n- Bobas\n\
            - Coconut Jelly\nPlease enter your choice for toppings: ")

    size = input(
        "Please enter your desired size of cup \
        (Please enter s for small, m for medium, or l for large): ")
    
    if size == "s":
        mass = 355
    elif  size == "m":
        mass = 473
    elif size == "l":
        mass = 621

    temperature = float(input(
        "Please enter your desired temperature of your beverage \
        (between 1 and 4 degrees): "))

    #decides which temperature to use in the formula depending on the input
    if temperature >= 1 and temperature <= 10:
        if temperature >= 1 and temperature <=4:
            Final_Temp = temperature #temperature to use in the equation
        else:
            Final_Temp = 4
        
        Delta_Drink = 25 - Final_Temp
        NumOfIce = (
            (mass * HEAT_CAPACIY_WATER * Delta_Drink)/
            (HEAT_OF_FUSION_WATER + HEAT_CAPACIY_WATER * Final_Temp)
            )/5
        
        print("Your drink is a", drink, "and", tea, "with", toppings + ".")
        print("The temperature of your beverage will be", float(Final_Temp),
              "Celcius degree after all", int(NumOfIce), "ice cubes melted.")
        print("Have a nice day!")
    else:
        print("Invalid choice! End of the program")