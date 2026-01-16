year = int(input("Enter a year to check weather it is leap or not : "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year}, is a Leap year")
else:
    print(f"{year}, is not a Leap year")    