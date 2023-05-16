units = int(input("Enter the number of units consumed: "))
total_bill = 0
surcharge_percent = 20
if units <= 50:
total_bill = units * 0.5
elif units <= 150:
total_bill = 25 + (units - 50) * 0.75
elif units <= 250:
total_bill = 100 + (units - 150) * 1.20
else:
total_bill = 220 + (units - 250) * 1.50
surcharge_amount = (surcharge_percent / 100) * total_bill
total_bill += surcharge_amount
print(f"Total electricity bill (including {surcharge_percent}%
surcharge): Rs. {total_bill:.2f}")