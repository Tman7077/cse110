age = int(input("How old are you? "))
print(f'You\'ll be {age + 1} on your next birthday.')
eggs = int(input("How many full egg cartons do you have? "))
print(f'You have {eggs * 12} eggs.')
import math
cookies = int(input("How many cookies do you have? "))
people = int(input("How many people do you want to split the cookies between? "))
if cookies % people == 1:
     cookie_s = "cookie"
else:
     cookie_s = "cookies"
print(f'In order to split {cookies} cookies between {people} people, each person will get {math.floor(cookies / people)} cookies and you\'ll have {cookies % people} {cookie_s} left over.')