correct_pin = "1234"

while True:
    entered_pin = input("Enter your PIN: ")
    
    if entered_pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN. Please try again.")
        
