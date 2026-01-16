try:
    distance = float(input(f"Enter your traveling distance in km : "))
    if distance < 3:
        print("You can go by walk")
    elif 3 < distance < 15:
        print("You can go by bike")
    else:
        print("You can go by car")    
except ValueError:
    print("Enter the km in numbers")        