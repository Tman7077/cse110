import math

def main():
     def ask_shape():
          print('Type the number corresponding to one of the following shapes, or type "quit" to end.',
               "1. Square",
               "2. Circle",
               "3. Rectangle", sep="\n")
          return input("Which shape's area would you like to calculate? ")
     
     shape = ask_shape()

     while shape not in ["1", "2", "3", "quit"]:
          print(f'\n"{shape}" is not a valid input. Type 1, 2, 3, or quit.\n')
          ask_shape()
     
     if shape == "1":
          side = float(input("What is the side length of the square? "))
          area = compute_area_square(side)
          print(f'\nThe area of a square with side length {side} is {area} square units.\n')
          main()
     elif shape == "2":
          radius = float(input("What is the radius of the circle? "))
          area = compute_area_circle(radius)
          print(f'\nThe area of a circle with radius {radius} is {area} square units.\n')
          main()
     elif shape == "3":
          side1 = float(input("What is the first side length of the rectangle? "))
          side2 = float(input("What is the second side length of the rectangle? "))
          area = compute_area_rectangle(side1, side2)
          print(f'\nThe area of a square with side lengths {side1} and {side2} is {area} square units.\n')
          main()
     else: # if shape == "quit":
          return

def compute_area_square(s):
     return s ** 2

def compute_area_circle(r):
     return math.pi * (r ** 2)

def compute_area_rectangle(s1, s2):
     return s1 * s2

if __name__ == "__main__":
     main()