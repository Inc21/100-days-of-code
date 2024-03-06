print("Welcome to the tip calculator!")
input_bill = float(input("What was the total bill? $"))
input_tip = int(input(
    "What percentage tip would you like to give? 10, 12, or 15? "))
input_people = int(input("How many people to split the bill? "))

bill_with_tip = input_tip / 100 * input_bill + input_bill
split = bill_with_tip / input_people
final_bill = round(split, 2)
final_bill = "{:.2f}".format(split)
print(f"Each person should pay: ${final_bill}")
