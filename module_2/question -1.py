print("========= KALKULATOR ARITMATIKA =========")

firstNumber = int(input("angka: "))
operator = input("operator (+, -, *, /, //, **, %): ")
secondNumber = int(input("angka: "))

# if operator == "+":
#   print(f"Hasil: {firstNumber + secondNumber}")
# elif operator == "-":
#   print(f"Hasil: {firstNumber - secondNumber}")
# elif operator == "*":
#   print(f"Hasil: {firstNumber * secondNumber}")
# elif operator == "/":
#   print(f"Hasil: {firstNumber / secondNumber}")
# elif operator == "//":
#   print(f"Hasil: {firstNumber // secondNumber}")
# elif operator == "**":
#   print(f"Hasil: {firstNumber ** secondNumber}")
# elif operator == "%":
#   print(f"Hasil: {firstNumber % secondNumber}")
# else:
#   print("Operator tidak ditemukan!")

  # Revision

match operator:
    case "+":
        print(f"Hasil: {firstNumber + secondNumber}")
    case "-":
        print(f"Hasil: {firstNumber - secondNumber}")
    case "*":
        print(f"Hasil: {firstNumber * secondNumber}")
    case "/":
        print(f"Hasil: {firstNumber / secondNumber}")
    case "//":
        print(f"Hasil: {firstNumber // secondNumber}")
    case "**":
        print(f"Hasil: {firstNumber ** secondNumber}")
    case "%":
        print(f"Hasil: {firstNumber % secondNumber}")
    case _:
        print("Maaf, operator yang anda pilih tidak ditemukan!")

print("========= PROGRAM SELESAI =========")