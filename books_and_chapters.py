with open("books_and_chapters.txt") as swf: # standard works file --> swf
     works = []
     swd = {}
     for line in swf:
          work = line.strip()[line.rindex(":") + 1:]
          if work not in works:
               works.append(work)

     for work in works:
          swd.update({work:[]}) # standard works dictionary --> swd

for i in range(len(works)):
     works[i] = works[i].lower()

queried_work = input("Which work would you like to learn more about? ").lower()
while queried_work not in works:
     print()
     print("That is not a valid work. Please enter:",
     "Old Testament", 
     "New Testament", 
     "Book of Mormon", 
     "Doctrine and Covenants", 
     "Pearl of Great Price", sep='\n')
     print()
     queried_work = input("Which work would you like to learn more about? ").lower()
print()

with open("books_and_chapters.txt") as swf:
     for line in swf:
          work = line.strip()[line.rindex(":") + 1:]
          book = line.strip()[:line.rindex(":")].split(":")
          book[1] = int(book[1])
          swd[work].append(book)

largest = []
max_chap = -1
for work in swd.keys():
     if work.lower() == queried_work:
          for book in swd[work]:
               print(f'Scripture: {work}, Book: {book[0]}, Chapters: {book[1]}')
               if book[1] > max_chap:
                    max_chap = book[1]
                    largest = [work, book[0], book[1]]
          print()
print(f'The largest book in the {largest[0]} is {largest[1]} with {largest[2]} chapters.')