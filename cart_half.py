cart = []

def menu():
     print("Input the number for the corresponding action:",
          "1. Add a new item",
          "2. Display the items currently in your cart",
          "3. Remove an item from your cart",
          "4. Calculate your current subtotal",
          "5. Quit",
          sep="\n")
     num = input("What would you like to do? ")
     if type(num) == int:
          num = int(num)
     else:
          print("Please enter a number from 1 to 5.")
          print()
          menu()
     if num == 1:
          add(cart)
     elif num == 2:
          display_cart(cart)
     elif num == 3:
          print("Not yet implemented.")
          menu()
     elif num == 4:
          print("Not yet implemented.")
          menu()
     elif num == 5:
          quit()
     else:
          print("That's not a valid option.")
          menu()

def add(cart):
     item = input("What item would you like to add? ")
     times = int(input("How many would you like to add? "))
     print()
     for _ in range(times):
          cart.append(item)
     if times == 1:
          print(f'{times} "{item}" has been added to the cart.')
     else:
          print(f'{times} "{item}"s have been added to the cart.')
     print()
     menu()

def display_cart(cart):
     print("Current Cart:")
     if range(len(cart)) == 0:
          print("Empty!")
     else:
          for num in range(len(cart)):
               print(f'{num + 1}. "{cart[num]}"')
     print()
     menu()

def quit():
     print("Thank you for shopping!")

if __name__ == "__main__":
     menu()