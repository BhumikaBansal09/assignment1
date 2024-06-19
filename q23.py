def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp = float(input("Enter the temperature: "))
conversion_type = input("Convert to (F)ahrenheit or (C)elsius? ").strip().upper()

if conversion_type == "F":
    converted_temp = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is equal to {converted_temp}°F")
elif conversion_type == "C":
    converted_temp = fahrenheit_to_celsius(temp)
    print(f"{temp}°F is equal to {converted_temp}°C")
else:
    print("Invalid conversion type. Please enter 'F' or 'C'.")
