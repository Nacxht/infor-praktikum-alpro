isMember = input("Status: (member/tidak): ")
totalPrice = int(input("Masukkan total belanja: "))

discount = 0

if isMember == "member":
  discount += 2

if totalPrice > 200000:
  discount += 4
elif totalPrice > 100000:
  discount += 3

discountToIdr = discount / 100 * totalPrice
mustPaid = totalPrice - (totalPrice * discount / 100)

print(f"Total diskon: {discountToIdr}")
print(f"Total yang harus dibayar: {mustPaid}")