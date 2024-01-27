import csv

def main():
     
     # create compound list with each row in the csv
     all_data= []
     with open("life-expectancy.csv") as csv_file:
          reader = csv.reader(csv_file)
          next(reader)
          for row in reader:
               all_data.append(row)
     
     # extract all of the life expectancies to a new list
     all_le = []
     for row in all_data:
          all_le.append(row[3])

     # get min and max life expectancies
     all_le_max = max(all_le)
     all_le_min = min(all_le)

     print(f'The overall max life expectancy was {all_le_max}.')
     print(f'The overall min life expectancy was {all_le_min}.')

if __name__ == "__main__":
     main()