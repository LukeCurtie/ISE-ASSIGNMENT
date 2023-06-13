def compare_temperature(city, min_temp, max_temp, morning_temp, afternoon_temp, time):
    if time.lower() == "morning":
        average_temp = morning_temp
    elif time.lower() == "evening":
        average_temp = afternoon_temp
    else:
        print("Invalid time specified.")
        return

    if average_temp > max_temp or average_temp < min_temp:
        print("Average temperature is outside the possible min-max range.")
        return

    print(f"The average {time.lower()} temperature in {city} is {average_temp}°C.")

    given_temp = float(input("Enter the temperature to compare (in °C): "))

    temperature_difference = abs(given_temp - average_temp)

    if temperature_difference > 5:
        print("The temperature difference is more than 5°C.")
    else:
        print("The temperature difference is within 5°C.")

# Getting input from the user
city = input("Enter the city name: ")
min_temp, max_temp = map(float, input("Enter the possible min and max temperatures (in °C) separated by a space: ").split())
morning_temp = float(input("Enter the mean morning temperature (9 am) (in °C): "))
afternoon_temp = float(input("Enter the mean afternoon temperature (3 pm) (in °C): "))
time = input("Enter the time (morning or evening): ")

# Calling the compare_temperature function
compare_temperature(city, min_temp, max_temp, morning_temp, afternoon_temp, time)

