weather_list = ["Sunny", "Rainy", "Cold", "Snowy"]
weather = input("How's the weather at your side : ")

weather = weather.capitalize()

if weather not in weather_list:
    print("Please tell me the weather to know what can you do..")
    exit()

if weather == "Sunny":
    print("You can go for a walk")
elif weather == "Rainy":
    print("You can read a book")
elif weather == "Cold":
    print("You can have a hot tea")
elif weather == "Snowy":
    print("Build a snowman")           
else:
    print("Please tell me the weather to know what can you do.. ")