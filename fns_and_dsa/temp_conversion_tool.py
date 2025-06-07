# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# User Interaction
try:
    # Prompt user for temperature
    temperature = float(input("Enter Temperature: "))
    
    # Prompt user for unit
    unit = input("Celsius or Fahrenheit? ").strip().lower()

    if unit == "celsius":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {result:.2f}°F")
    elif unit == "fahrenheit":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {result:.2f}°C")
    else:
        raise ValueError("Invalid unit. Please type 'Celsius' or 'Fahrenheit'.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")


# FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
# CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

# def convert_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5 / 9
#     return celsius

# def convert_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9 / 5) + 32
#     return fahrenheit

# convert = float(input("Enter the temperature to convert: "))
# specify = str(input("Is this temperature in Celsius or Fahrenheit? (C/F):")).strip().lower()

# if specify == "celsuis":
#     result = convert_to_celsius(convert)
#     print(f"{convert}C is equal to {result}F")
# elif specify == "fahrenheit":
#     result = convert_to_fahrenheit(convert)
#     print(f"{convert}F is equal to {result}C")
# else:
#     print("invalid input")
