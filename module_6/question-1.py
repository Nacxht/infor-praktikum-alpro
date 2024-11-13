num_list = []

def append_sort(number):
  if not num_list:
    num_list.append(number)
    return

  if number > num_list[len(num_list) - 1]:
    num_list.append(number)
    return

  for i in range(len(num_list)):
    if number < num_list[i]:
      num_list.insert(i, number)
      return

total_append = int(input("Masukkan banyak data yang ingin ditambahkan: "))

for i in range(1, total_append + 1):
  number_input = int(input(f"Masukkan angka ke - {i}: "))
  append_sort(number_input)

print(f"Hasil list: {num_list}")