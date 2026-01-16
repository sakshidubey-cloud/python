price = [8, 12]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]   

age = int(input("Enter an age : "))
day = input("Enter the day : ")

if day not in days:
    print("??")    
    exit()

day = day.capitalize()

if age < 18:
    ticket_price = price[0]
else:
    ticket_price = price[1]    

if day == "Wednesday":
    ticket_price -= 2
print(f"Your movie ticket price is: ${ticket_price}")