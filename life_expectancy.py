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

     # extract all years to a new list
     all_yrs = []
     for row in all_data:
          if row[2] not in all_yrs:
               all_yrs.append(int(row[2]))
     all_yrs.sort()
          
     yr = input("Enter the year of interest: ")

     # make sure the year is valid
     while not yr.isdigit():
          print("Not a valid year.")
          yr = input("Enter the year of interest: ")
     
     yr = int(yr)

     # make sure the year is in the list
     while yr not in all_yrs:
          print("No data for that year.")
          yr = input("Enter the year of interest (1534 - 2019, not all years in between): ")
          while not yr.isdigit():
               print("Not a valid year.")
               yr = input("Enter the year of interest: ")
          yr = int(yr)

     print()

     # get min and max life expectancies
     all_le_max = max(all_le)
     all_le_min = min(all_le)

     # find the index (in the original, unsorted list) of the min and max le
     all_index_max = all_le.index(all_le_max)
     all_index_min = all_le.index(all_le_min)

     # based on the index, find the countries with min and max le
     all_who_max = all_data[all_index_max][0]
     all_who_min = all_data[all_index_min][0]

     # based on the index, find the years in which min and max le occurred
     all_when_max = all_data[all_index_max][2]
     all_when_min = all_data[all_index_min][2]

     print(f'The overall max life expectancy was {all_le_max} by {all_who_max} in {all_when_max}.')
     print(f'The overall min life expectancy was {all_le_min} by {all_who_min} in {all_when_min}.')
     print()

     # extract all rows in all_data which are from the year based on user input
     yr_data = []
     for row in all_data:
          if row[2] == str(yr):
               yr_data.append(row)
     
     # extract all of the year's life expectancies to a new list
     yr_le = []
     for row in yr_data:
          yr_le.append(float(row[3]))
     
     # find the average life expectancy from the year
     yr_le_avg = round(sum(yr_le) / len(yr_le), 3)

     # get min and max life expectancies from the year
     yr_le_max = max(yr_le)
     yr_le_min = min(yr_le)

     # find the index of the min and max le
     yr_index_max = yr_le.index(yr_le_max)
     yr_index_min = yr_le.index(yr_le_min)

     # based on the index and year, find the countries with min and max le
     yr_who_max = yr_data[yr_index_max][0]
     yr_who_min = yr_data[yr_index_min][0]

     print(f'The average life expectancy in {yr} was {yr_le_avg}.')
     print(f'The max life expectancy in {yr} was {yr_le_max} by {yr_who_max}.')
     print(f'The min life expectancy in {yr} was {yr_le_min} by {yr_who_min}.')

     print()

     cont = input("Would you like to look at the data for a certain country (y/n)? ")

     # ensure valilidy of input
     while cont != "y" and cont != "n":
          print('Please input "y" or "n" (no quotes).')
          cont = input("Would you like to look at the data for a certain country (y/n)? ")

     #
     if cont == "n":
          pass
     else:
          inp_country = input("What country? ").strip().title()

          # ensure the input country is letters only
          while not inp_country.replace(" ","").isalpha():
               print("Not a valid country.")
               inp_country = input("What country would you like to look at the data for? ").strip().title()

          # make a list of countries
          countries = []
          for row in all_data:
               country = row[0]
               if country not in countries:
                    countries.append(country)

          # ensure the input country is in the list of countries with data
          while inp_country not in countries:
               print("Not a valid country.")
               inp_country = input("What country would you like to look at the data for? ").strip().title()
               while not inp_country.replace(" ","").isalpha():
                    print("Not a valid country.")
                    inp_country = input("What country would you like to look at the data for? ").strip().title()

          print()
          
          # extract all data for input country to new list
          country_data = []
          for row in all_data:
               if row[0] == inp_country:
                    country_data.append(row)
          
          # extract all of the country's life expectancies to a new list
          country_le = []
          for row in country_data:
               country_le.append(float(row[3]))

          # find the average life expectancy from the country
          country_le_avg = round(sum(country_le) / len(country_le), 3)

          # get min and max life expectancies from the country
          country_le_max = max(country_le)
          country_le_min = min(country_le)

          # get the indexes of min and max le for the country
          index_yr_max = country_le.index(country_le_max)
          index_yr_min = country_le.index(country_le_min)

          # get the years of min and max le based on indexes from above
          country_yr_max = country_data[index_yr_max][2]
          country_yr_min = country_data[index_yr_min][2]

          print(f'The average life expectancy in {inp_country} was {country_le_avg}.')
          print(f'The max life expectancy in {inp_country} was {country_le_max} in {country_yr_max}.')
          print(f'The min life expectancy in {inp_country} was {country_le_min} in {country_yr_min}.')


if __name__ == "__main__":
     main()