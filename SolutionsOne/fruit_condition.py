fruit = input("Name of fruit : ")
color = input(f"enter the color to know to {fruit}'s condition : ")
fruit_color = ["green", "yellow", "brown"]

if color not in fruit_color:
    print("??")
    exit()

if color == "green":
    print("unripe")
elif color == "yellow":
    print("ripe")
elif color == "brown":
    print("overripe")    
else:
    print("enter fruit name")