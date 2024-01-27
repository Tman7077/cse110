child_meal = float(input("What is the price of a child's meal? "))
number_child_meals = int(input("How many child meals do you want? "))
adult_meal = float(input("What is the price of an adult's meal? "))
number_adult_meals = int(input("How many adult meals do you want? "))
# tax_rate = float(input("what is the sales tax rate (e.g. 6.00 or 8.2) "))
subtotal = child_meal * number_child_meals + adult_meal * number_adult_meals
print(f'Subtotal: ${subtotal:.2f}')