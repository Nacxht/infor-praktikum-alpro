sukuAwal = int(input("Masukkan suku awal(a): "))
pembeda = int(input("Masukkan pembeda (b): "))
banyakBilangan = int(input("Masukkan banyak bilangan: "))

jumlahSeluruhBilangan = 0
i = 0

for i in range(banyakBilangan):
  print(sukuAwal, end=" ")

  jumlahSeluruhBilangan += sukuAwal
  sukuAwal += pembeda

print(f"\nJumlah seluruh bilangan: {float(jumlahSeluruhBilangan)}")