pets = ["cat", "dog"]
pet = input("What is your pet's species : ").lower()

if pet not in pets:
    print("We have info only about cats and dogs")
    exit()

age = int(input("What's your pet's age : "))

if pet == "dog" and age < 2:
    food = "Puppy food"
elif pet =="cat" and age > 5:
    food = "Senior cat food"
else:
    food = "Regular pet food"    

print(f"Recommended food for your pet is, '{food}'")        