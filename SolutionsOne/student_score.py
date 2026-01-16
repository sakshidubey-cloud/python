try:
    score = int(input("Enter your score : "))
    if 90 <= score <= 100:
        print("You got A grade")
    if 80 <= score <= 89:
        print("You got B grade")
    if 70 <= score <= 79:
        print("You got C grade")
    if 60 <= score <= 69:
        print("F")    
    else:
        print("Enter your original score")
except ValueError:
    print("Enter your score in number")