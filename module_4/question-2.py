def angkaTerbalik(num):
  numTemp = num
  reversed = 0
  length = 0

  while num > 0:
    length += 1
    num //= 10

  num = numTemp

  while num > 0:
    reversed = (reversed * 10) + (num % 10)
    num //= 10

  print(f"kebalikan dari {numTemp} merupakan {reversed:0{length}d}")

angkaTerbalik(100)