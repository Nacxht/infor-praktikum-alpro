num = int(input("Masukkan N: "))
apakahDuaPangkat = False

for i in range(num):
  duaPangkat = 2 ** (i + 1)

  if num == duaPangkat:
    apakahDuaPangkat = True
    break
  elif duaPangkat > num:
    break

if apakahDuaPangkat == True:
  print("ya")
else:
  print("bukan")