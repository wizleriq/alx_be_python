FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

convert = float(input("Enter the temperature to convert: "))
specify = str(input("Is this temperature in Celsius or Fahrenheit? (C/F):")).strip().lower()

if specify == "celsuis":
    result = convert_to_celsius(convert)
    print(f"{convert}C is equal to {result}F")
elif specify == "fahrenheit":
    result = convert_to_fahrenheit(convert)
    print(f"{convert}F is equal to {result}C")
else:
    print("invalid input")
