def main():
     temperature = input("What is the temperature? ")
     while not temperature.replace("-", "").replace(" ", "").isdigit():
          print("Not a valid temperature.")
          temperature = input("What is the temperature? ")
     temperature = int(temperature)

     scale = input('Celsius or Fahrenheit ("C"/"F")? ').strip().upper()
     while scale != "C" and scale != "F":
          print('Please input "C" or "F" (no quotes).')
          scale = input('Celsius or Fahrenheit ("C"/"F")? ').strip().upper()
     

     
     i, speeds = 5, []
     while i <= 60:
          speeds.append(i)
          i += 5
     
     if scale == "F":
          for speed in speeds:
               chill = calc_chill(temperature, speed)
               print(f'At {temperature}F with {speed} mph wind, the wind chill is {chill}F.')
     else:
          for speed in speeds:
               f_temp = c_to_f(temperature)
               chill = calc_chill(f_temp, speed)
               chill = f_to_c(chill)
               print(f'At {temperature}C with {speed} mph wind, the wind chill is {chill}C.')


     
def c_to_f(temp):
     return temp * 9 / 5 + 32

def f_to_c(temp):
     return (temp - 32) * 5 / 9

def calc_chill(temp, wind_speed):
     return round(35.74 + (0.6215 * temp) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temp * (wind_speed ** 0.16)), 2)

if __name__ == "__main__":
     main()