data_list = [1, 3.5, 12, 2]

def get_minmax(data):
  smallest = 0
  biggest = 0

  for number in data:
    if (not smallest) or (not biggest):
      smallest = number
      biggest = number
      continue

    elif number < smallest:
      smallest = number
      continue

    elif number > biggest:
      biggest = number
      continue

  return [smallest, biggest]

def minmax_remover(data, min_value, max_value):
  data.remove(min_value)
  data.remove(max_value)

  return data

print(f"List sementara: {data_list}")
total_append = int(input("Masukkan jumlah data yang ingin di tambah: "))

for i in range(1, total_append + 1):
  new_data = eval(input(f"Masukkan data ke-{i}: "))
  data_list.append(new_data)

minmax = get_minmax(data_list)

print(f"List setelah di tambah data baru: {data_list}")
print(f"Data terkecil adalah: {minmax[0]}")
print(f"Data terbesar adalah: {minmax[1]}")

data_list = minmax_remover(data_list, minmax[0], minmax[1])
print(f"List setelah dihapus data terbesar dan terkecil: {data_list}")