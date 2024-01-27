def main():
     percent = float(input(f'What is your percentage grade in the class, ignoring the % sign? '))
     grade = determine_grade(percent)
     sign = determine_sign(grade, percent)
     passing = determine_passing(percent)
     print(f'You have a grade of {grade}{sign} in the class.')
     print(f'You are{passing} passing the class.')

def determine_grade(percent):
     grade = "F"
     if percent >= 60:
          grade = "D"
     if percent >= 70:
          grade = "C"
     if percent >= 80:
          grade = "B"
     if percent >= 90:
          grade = "A"
     return grade

def determine_passing(percent):
     passing = " not"
     if percent >= 70:
          passing = ""
     return passing

def determine_sign(grade, percent):
     import math
     percent = str(math.trunc(percent))
     digit = int(percent[-1])
     if (grade == "F")\
          or (grade == "A" and digit > 2)\
          or (digit > 2 and digit < 7):
          return ""
     if digit < 3:
          return "-"
     if digit > 6:
          return "+"

if __name__ == "__main__":
     main()