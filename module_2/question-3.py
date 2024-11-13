username = input("Masukkan Username: ")
email = input("Masukkan Email: ")
password = input("Masukkan Password: ")
bornYear = int(input("Masukkan tahun lahir anda: "))

if not username:
  print("Invalid, Username tidak boleh kosong")
elif "@" not in email:
  print("Invalid, Email tidak valid, gunakan @ pada email")
elif len(password) <= 8:
  print("Invalid, Password harus lebih dari 8 karakter")
elif bornYear >= 2000:
  print("Anda belum cukup umur")
else:
  print("Akun berhasil dibuat")