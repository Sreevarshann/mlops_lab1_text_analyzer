def to_celsius(f):
    return (f - 32) * 5/9

def to_fahrenheit(c):
    return (c * 9/5) + 32

def kelvin_to_celsius(k):
    return k - 273.15

def celsius_to_kelvin(c):
    return c + 273.15


# 🟢 This part runs only when you call: python3 src/converter.py
if __name__ == "__main__":
    value = float(input("Enter temperature in Celsius: "))
    print(f"{value}°C in Fahrenheit = {to_fahrenheit(value):.2f}°F")
    print(f"{value}°C in Kelvin = {celsius_to_kelvin(value):.2f}K")
