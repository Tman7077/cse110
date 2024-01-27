import random
def game():
     answer = random.randint(1,100)
     inp = 0
     guesses = 0
     while inp != answer:
          guesses += 1
          inp = int(input("Guess: "))
          if inp < answer:
               print("Too low.")
          else:
               print("Too high.")
     print(f'Correct. You took {guesses} guesses.')
     if input("Would you like to play again (yes/no)? ").lower() == "yes":
          game()
game()