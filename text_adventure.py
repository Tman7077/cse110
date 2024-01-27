def fail(function):
     # This function is called by the default (input not found) case in each following choice function.
     # It will tell the user that their answer did not match any possibility, and then re-call that choice,
     # because each default case contains the name of the function that calls fail().

     print(f'\nThat is not a valid answer.\n')
     eval(function)

'''
Each function ending in "__level_{level}" asks the user a question,
and matches it to one of two possibilities.
If their input does not match any of the given possibilities,
call fail(), which re-tries the input.
If their input does match a given case, execute the respective code,
calling the next function.
'''

def start__level_0():
     
     inp = input(f'It\'s 6:30 a.m. on a Monday morning, and your dreaded alarm goes off. \
Would you like to GET UP or STAY IN BED?\n').lower()

     match inp:
          case "get up":
               get_up__level_1()
          case "stay in bed":
               stay_in_bed__level_1()
          case _:
               fail("start__level_0()")

def get_up__level_1():
     
     inp = input(f'\nYou muster the strength to remove your corpse-like self from the warmth of your covers, \
and stand up. Work starts at 9. Would you like to SHOWER or MAKE BREAKFAST?\n').lower()

     match inp:
          case "shower":
               shower__level_2()
          case "stay in bed":
               make_breakfast__level_2()
          case _:
               fail("get_up__level_1()")

def stay_in_bed__level_1():
     
     inp = input(f'\nThat\'s what I would have done too. You snooze the alarm four times, \
and find yourself waking up to what is now a 7:20 alarm. With no food in your stomach or \
motivation to get ready for the day, you remember you have a 7:45 class. Do you want to \
RUN or SKIP IT?\n').lower()

     match inp:
          case "run":
               run__level_2()
          case "skip it":
               skip_it__level_2()
          case _:
               fail("get_up_stay_in_bed__level_1()")

def shower__level_2():
     
     inp = input(f'\nAs much work as going from a warm bed to a shower may have seemed, \
you feel refreshed after waking yourself up with it. Tonight is date night, \
but should you spruce up NOW for everyone who sees you today, \
or LATER for your special someone?\n').lower()

     match inp:
          case "now":
               now__final()
          case "stay in bed":
               later__final()
          case _:
               fail("shower__level_2()")

def make_breakfast__level_2():
     
     inp = input(f'\nPancakes sound delicious, but you realize you are unfortunately out of flour. \
Do you want to make EGGS, FRENCH TOAST, or SKIP BREAKFAST instead?\n').lower()

     match inp:
          case "eggs":
               eggs__final()
          case "french toast":
               french_toast__final()
          case "skip breakfast":
               skip_breakfast__final()
          case _:
               fail("make_breakfast__level_2()")

def run__level_2():
     
     inp = input(f'\nIn your hurry to get out the door, you throw on some mismatched \
shoes, so you both clonk your steel-toed boot and slide on your sister\'s \
ice skate all the way to your life management class. Isn\'t that an unfortunate \
coincidence? People ask why you\'re dressed the way you are, should you \
TELL THE TRUTH or DODGE THEIR QUESTIONS?\n').lower()

     match inp:
          case "tell the truth":
               tell_the_truth__final()
          case "dodge their questions":
               dodge_their_questions__final()
          case _:
               fail("run__level_2()")

def skip_it__level_2():
     
     inp = input(f'\nSkipping class sounds very enticing, and it feels very worth it. \
With your now-free time, would you like to GO BACK TO SLEEP or WATCH YOUTUBE?\n').lower()

     match inp:
          case "go back to sleep":
               go_back_to_sleep__final()
          case "watch youtube":
               watch_youtube__final()
          case _:
               fail("skip_it__level_2()")

'''
Each function ending in "__final" is the end of that particular storyline.
The choices a user has made up until that point have led to an ending,
which that function will print out for the user to see.
'''

def now__final():
     print(f'\nYou spray on that expensive cologne you bought a few weeks ago, \
and head on with your day. Good luck with your evening.')

def later__final():
     print(f'\nAfter refusing to expend your limited supply of fancy cologne for \
a simple day job, you head to work. Everyone gives you funny looks, \
and you finally realize it\'s because you never put on deodorant at all. Nice one.')

def eggs__final():
     print(f'\nYou crack those unborn chickens into a small frying pan \
just like Rapunzel\'s, daydreaming of whacking an unsuspecting intruder \
over the head with it. After a while you realize that you have been distracted \
for far too long and your eggs are burnt. Pay a little more attention.')

def french_toast__final():
     print(f'\nYou whip up some dipping batter, chuck a loaf in, and make some extra \
for leftovers. That was a good start to your morning, and now it\'s time \
to head to class. Have a good rest of your day!')

def skip_breakfast__final():
     print(f'\nHardcore. You\'re going to regreat that later when you have to \
go to the gym... Good luck!')

def tell_the_truth__final():
     print(f'\nYour professor overhears the sob story about your morning, \
and decides you are absolutely not ready for his class. \
He flunks you immediately. I guess you should wake up to your alarm next time.')

def dodge_their_questions__final():
     print(f'\nYour professor overhears your sketchy avoidance of a simple question, \
and decides you are absolutely not ready for his class. \
He flunks you immediately. I guess you should wake up to your alarm next time.')

     # It was inevitable, you were always going to fail his class. Muahaha.

def go_back_to_sleep__final():
     print(f'\nSleep is good. You may never wak up from this self-induced laziness coma, \
it is incredibly comfortable and re-entering the real world is a lot more work than it\'s worth.')

def watch_youtube__final():
     import webbrowser
     webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
     print(f'\nGotcha!')

if __name__ == "__main__":
     start__level_0()