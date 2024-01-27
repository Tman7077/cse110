cart = []
prices = []

def menu():
     print("Input the number for the corresponding action:",
          "1. Add a new item",
          "2. Display the items currently in your cart",
          "3. Remove an item from your cart",
          "4. Calculate your current subtotal",
          "5. Quit",
          sep="\n")
     num = input("What would you like to do? ")
     print()
     if num in ['1', '2', '3', '4', '5']:
          num = int(num)
     else:
          print("Please enter a number from 1 to 5.")
          print()
          menu()
     if num == 1:
          add(cart, prices)
     elif num == 2:
          display_cart(cart, prices)
     elif num == 3:
          remove_item(cart, prices)
     elif num == 4:
          calc_subtotal(cart, prices)
     elif num == 5:
          quit()
     else:
          print("That's not a valid option.")
          menu()

def add(cart, prices):
     item = input("What item would you like to add? ")
     price = input(f'What is the price of "{item}"? $')
     times = int(input("How many would you like to add? "))
     print()
     for _ in range(times):
          cart.append(item)
          prices.append(price)
     if times == 1:
          print(f'{times} "{item}" has been added to the cart for $2{price}.')
     else:
          print(f'{times} "{item}"s have been added to the cart for $2{price} each.')
     print()
     menu()

def display_cart(cart, prices):
     print("Current Cart:")
     if range(len(cart)) == 0:
          print("Empty!")
     else:
          for num in range(len(cart)):
               print(f'{num + 1}. "{cart[num]}" - ${prices[num]}')
     print()
     menu()

def remove_item(cart, prices):
     if len(cart) == 0:
          print("Your cart is empty! You cannot remove anything.")
          print()
          menu()
     item = input("Which item would you like to remove from your cart? ")
     if item in cart:
          i = cart.index(item)
          count = cart.count(item)
          if count > 1:
               print(f'{item} is in your cart {count} times.')
               one_all = input('Would you like to remove "one" or "all" of them? ') 
               if one_all == "one":
                    cart.pop(i)
                    prices.pop(i)
                    print(f'"{item}" was removed from your cart.')
                    print()
                    menu()
               elif one_all == "all":
                    for _ in range(cart.count(item)):
                         cart.pop(i)
                         prices.pop(i)
                    print(f'{count} instances of "{item}" were removed from your cart.')
                    menu()
               else:
                    print("That's not a valid input. Please try again.")
                    print()
                    remove_item(cart, prices)
          print()
     else:
          print(f'"{item}" is not in your cart. Please try again.')
          remove_item(cart, prices)


def calc_subtotal(cart, prices):
     if len(cart) == 0:
          print("Your cart is empty.")
     subt = 0
     for i in range(len(prices)):
          subt += float(prices[i])
     print(f'Your current subtotal is ${subt}.')
     print()
     menu()

def quit():
     print("Thank you for shopping!")

if __name__ == "__main__":
     menu()