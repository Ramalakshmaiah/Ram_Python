# Celsius to Fahrenheit
celsius = float(input("Enter a temperature in celsius: "))

faherheit = (celsius * 9/5) + 32

print(f"{celsius}C = {faherheit}F")

# Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print(f"{fahrenheit}°F = {celsius}°C")

# Celsius to Kalvin

celsius = float(input("Enter a temperature in celsius: "))

Kalvin = celsius + 273.15

print(f"{Kalvin}K = {celsius}C")
