def cetakSegitiga(length):
  multiplier = 1
  temp = 0
  i = 0

  while i < length:
    if temp > 9:
      temp = 0

    print(" " * (length - i), end="")
    print(str(temp) * multiplier)

    multiplier += 2
    temp += 1
    i += 1
