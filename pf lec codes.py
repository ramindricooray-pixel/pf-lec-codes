correct_pin = "1234"

while True:
    entered_pin = input("Enter your PIN: ")
    
    if entered_pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN. Please try again.")





total_bill = 0

for i in range(1, 6):
    price = float(input(f"Enter price for item {i}: "))
    total_bill += price

discount = 0
if total_bill > 5000:
    discount = total_bill * 0.20

final_amount = total_bill - discount

print(f"Total Amount: Rs. {total_bill}")
print(f"Discount Applied: Rs. {discount}")
print(f"Final Payable Amount: Rs. {final_amount}")
