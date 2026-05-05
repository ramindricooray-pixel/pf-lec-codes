pin = "1234"
balance = 5000  # Example starting balance
attempts = 0

while attempts < 3:
    user_pin = input("Enter your 4-digit PIN: ")
    if user_pin == pin:
        print("Access Granted.")
        amount = float(input("Enter withdrawal amount: "))
        
        if amount > balance:
            print("Error: Withdrawal amount exceeds balance.")
        elif (balance - amount) < 500:
            print("Error: Minimum remaining balance must be Rs. 500.")
        else:
            balance -= amount
            print(f"Withdrawal successful! Remaining balance: Rs. {balance}")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. Attempts left: {3 - attempts}")

if attempts == 3:
    print("Account locked due to too many incorrect attempts.")
