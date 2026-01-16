password = input("Please enter your password to check how much strong it is : ")
if len(password) <= 6:
    strength = "Weak"
elif 7 < len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print(f"Your password strength is : {strength}")    
