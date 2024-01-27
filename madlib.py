'''The other day, I was really in trouble. It all started when I saw a very
[adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
I could think to do was to [verb] over and over. Miraculously,
that caused it to stop, but not before it tried to [verb]
right in front of my family.'''
print("Please enter the following:")
aj1 = input("Adjective:   ")
an1 = input("Animal:      ")
vb1 = input("Verb:        ")
exc = input("Exclamation: ")
vb2 = input("Verb:        ")
vb3 = input("Verb:        ")
aj2 = input("Adjective:   ")
an2 = input("Animal:      ")
if aj2.lower()[:1] == "a" or aj2.lower()[:1] == "e" or aj2.lower()[:1] == "i" or aj2.lower()[:1] == "o" or  aj2.lower()[:1] == "u":
     aj2_art = "an"
else:
     aj2_art = "a"
if an2.lower()[:1] == "a" or an2.lower()[:1] == "e" or an2.lower()[:1] == "i" or an2.lower()[:1] == "o" or  an2.lower()[:1] == "u":
     an2_art = "an"
else:
     an2_art = "a"
if an1.lower()[:1] == "a" or an1.lower()[:1] == "e" or an1.lower()[:1] == "i" or an1.lower()[:1] == "o" or  an1.lower()[:1] == "u":
     an1_art = "an"
else:
     an1_art = "a"
print(f'Here is your story:\n\nThe other day, I was really in trouble. It all started when I saw a very {aj1.lower()} {an1.lower()} {vb1.lower()} down the hallway. "{exc.capitalize()}!" I yelled. But all I could think to do was to {vb2.lower()} over and over. Miraculously, that caused it to stop, but not before it tried to {vb3.lower()} right in front of my family. Oh, what {aj2_art} {aj2.lower()} day! I got to see {an2_art} {an2.lower()} ─ wait, no, it was a... {an1_art} {an1.upper()}! ─ {vb1.lower()} down a hall, that\'s so cool! ... Right? Cool? Cool.')