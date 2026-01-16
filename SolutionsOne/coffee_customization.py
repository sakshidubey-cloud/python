coffee_size = ["Small", "Medium", "Large"]
# espresso = ["Yes", "No"]

coffee = input("Which coffee cup size do you want to order : ")
coffee = coffee.capitalize()

if coffee not in coffee_size:
    print("Write the coffee cup size you want to order")
    exit()

if coffee in coffee_size:
    print(f"Your {coffee} cup coffee ordered is received.")
else:
    print("Please write the size of cup for coffee you want to order")  
    

extra_shot = input("Do you want an Extra shot of Espresso ? : ")
extra_shot = extra_shot.capitalize()
if extra_shot == "Yes":
    print(f"Sure, Your {coffee} cup coffee with an Extra shot of Espresso ordered is received.")

elif extra_shot == "No":
    print(f"Sure, Your {coffee} cup coffee order is received.")    

else:
    print("Please write Yes or No")    