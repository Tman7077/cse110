fname = input("What is your first name? ")
lname = input("What is your last name? ")
email = input("What is your email address? ")
phone = input("What is your phone number? ")
title = input("What is your job title? ")
idnum = input("What is your ID number? ")
hairc = input("What is your hair color? ")
eyesc = input("What is your eye color? ")
month = input("What month did you start work? ")
train = input('Have you completed advanced training? Input "y" or "n": ')
month_from_left = 7 + len(month)
if train == "y":
     train = "Yes"
     train_from_right = 13
else:
     train = "No"
     train_from_right = 12
hair_from_left, eyes_from_right = 6 + len(hairc), 6 + len(eyesc)
hair_eye_spacing = 50 - hair_from_left - eyes_from_right
month_train_spacing = 50 - month_from_left - train_from_right
if train_from_right > eyes_from_right:
     hair_eye_spacing = 50 - hair_from_left - train_from_right
else:
     month_train_spacing = 50 - month_from_left - eyes_from_right
separator = "--------------------------------------------------"
print(separator)
print(f'{lname.upper()}, {fname.capitalize()}\n{title.title()}\nID: {idnum}\n\n{email.lower()}\n{phone}\n\nHair: {hairc.capitalize()}{" " * hair_eye_spacing}Eyes: {eyesc.capitalize()}\nMonth: {month.capitalize()}{" " * month_train_spacing}Training: {train}')
print(separator)