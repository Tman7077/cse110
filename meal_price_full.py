child_meal = float(input("What is the price of a child's meal? "))
number_child_meals = int(input("How many child meals do you want? "))
adult_meal = float(input("What is the price of an adult's meal? "))
number_adult_meals = int(input("How many adult meals do you want? "))
tax_rate = float(input("what is the sales tax rate (e.g. 6.00 or 8.2) "))
subtotal = child_meal * number_child_meals + adult_meal * number_adult_meals
sales_tax = (tax_rate / 100) * subtotal
total = subtotal + sales_tax
# print(f'The price of {number_child_meals} child meals and {number_adult_meals} adult meals is ${subtotal:.2f} before tax, and ${total:.2f} after tax.')
print(f'Subtotal: ${subtotal:.2f}\nSales Tax: ${sales_tax:.2f}\nTotal: ${total:.2f}')
payment = float(input('How much would you like to pay? '))
if payment < round(total, 2):
     payment = float(input('That is not enough. How much would you like to pay? '))
else:
     print('Thanks.')
does_tip = ""
if payment > round(total*1.05, 2):
     over = payment - round(total, 2)
     does_tip = input('Does that include a tip? Input "y" or "n". ')
if does_tip == "y":
     tip_amount = float(input(f'How much? Max ${over:.2f}. '))
else:
     tip_amount = 0
print(f'Total: ${(total + tip_amount):.2f}\nChange: ${(payment - (total + tip_amount)):.2f}')