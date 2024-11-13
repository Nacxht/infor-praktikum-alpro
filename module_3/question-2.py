while True:
  print("=== Kalkulator Sederhana ===")
  print("Pilih Operasi:")
  print("1. Tambah (+)")
  print("2. Kurang (-)")
  print("3. Kali (*)")
  print("4. Bagi (/)")
  print("5. Exit")

  menuInput = input("Masukkan pilihan (1/2/3//4/5): ")

  if menuInput == "1":
    angkaPertama = float(input("Masukkan angka pertama: "))
    angkaKedua = float(input("Masukkan angka kedua: "))
    hasil = angkaPertama + angkaKedua

    print(f"\nHasil: {angkaPertama} + {angkaKedua} = {hasil}\n")
  elif menuInput == "2":
    angkaPertama = float(input("Masukkan angka pertama: "))
    angkaKedua = float(input("Masukkan angka kedua: "))
    hasil = angkaPertama - angkaKedua

    print(f"\nHasil: {angkaPertama} - {angkaKedua} = {hasil}\n")
  elif menuInput == "3":
    angkaPertama = float(input("Masukkan angka pertama: "))
    angkaKedua = float(input("Masukkan angka kedua: "))
    hasil = angkaPertama * angkaKedua

    print(f"\nHasil: {angkaPertama} * {angkaKedua} = {hasil}\n")
  elif menuInput == "4":
    angkaPertama = float(input("Masukkan angka pertama: "))
    angkaKedua = float(input("Masukkan angka kedua: "))
    hasil = angkaPertama / angkaKedua

    print(f"\nHasil: {angkaPertama} / {angkaKedua} = {hasil}\n")
  elif menuInput == "5":
    print("Terima kasih telah menggunakan kalkulator. Sampai jumpa!")
    break
  else:
    print("Pilihan tidak valid. Silahkan coba lagi.\n")