print("Konversi suhu Celsius")

celcius = int(input("Masukkan suhu dalam Celcius: "))
fahrenheit = (celcius * 9 / 5) + 32
kelvin = (fahrenheit - 32) * 5 / 9 + 273.15

print(f"Suhu dalam Fahrenheit: {fahrenheit} ℉")
print(f"Suhu dalam Kelvin: {kelvin} K")