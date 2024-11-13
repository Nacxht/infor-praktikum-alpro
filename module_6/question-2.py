def fpb(number):
  result = [factor for factor in range(1, number + 1) if number % factor == 0]
  return result

def same_element(list1, list2):
  result = []

  for i in list1:
    if i in list2:
      result.append(i)

  return result

number1 = int(input("Masukkan angka ke-1 = "))
number2 = int(input("Masukkan angka ke-2 = "))

fpb1 = fpb(number1)
fpb2 = fpb(number2)
same = same_element(fpb1, fpb2)

print("-in-")
print(f"{number1}\n{number2}")
print("-out-")

print(f"faktor pembagi angka: {fpb1}")
print(f"faktor pembagi angka: {fpb2}")

print(f"angka yang sama: {same}")