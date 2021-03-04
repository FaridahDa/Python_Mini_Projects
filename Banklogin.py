from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
attempt = 1
correct_pin = "9890"

# Log on for a bank, that requires correct pin to be used to log in and locks user out after 3 chances

print("------------------------")
print(f" Welcome to Forest Bank \n Logon time is: {current_time}")
print("-------------------------")

while attempt < 4:
    pin = input("Please enter your pin number:")
    if pin  == correct_pin :
        print("PIN accepted, you are now logged in")
        break
    else:
        print("Your pin was incorrect, please try again." + "" + "You have tried " + str(attempt) + " times")
    attempt = attempt + 1
    if attempt == 4:
        print("Sorry you are now locked out!")
