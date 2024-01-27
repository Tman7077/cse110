import sys

def main():
     rider1_age = float(input("How old is the first rider in years? "))
     rider1_height = float(input("How tall is the first rider in inches? "))
     two_people = input("Is there a second rider (yes/no)? ")
     if two_people.lower() == "yes":
          rider2_age = float(input("How old is the second rider in years? "))
          rider2_height = float(input("How tall is the second rider in inches? "))

          rider1 = rider_check(rider1_age, rider1_height)
          rider2 = rider_check(rider2_age, rider2_height)

          check2(rider1, rider2)
     else:
          rider1 = rider_check(rider1_age, rider1_height)

          check1(rider1, 1)


def rider_check(age, height):
     if age >= 18:
          adult = True
     else:
          adult = False
     
     if height >= 62:
          tall = True
          tall_enough = True
     else:
          tall = False
          if height >= 36:
               tall_enough = True
          else:
               tall_enough = False
     
     return [adult, tall, tall_enough]

def check1(rider, number):
     if rider[2] == False:
          sys.exit(f'Rider {number} may not ride if they are under 36 inches tall.')
     else:
          if rider[0] == True:
               if rider[1] == True:
                    sys.exit(f'Rider {number} may ride.')
               else:
                    sys.exit(f'Rider {number} may not ride alone if they are under 62 inches tall.')
          else:
               sys.exit(f'Rider {number} may not ride if they are under 18 years old.')

def check2(rider1, rider2):
     pass


if __name__ == "__main__":
     main()