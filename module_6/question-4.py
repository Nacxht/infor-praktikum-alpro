data_list = [1, 1, 1, 2, 3, 4, 4, 7]

def delete_duplicates(data):
  new_list = []

  for data in data:
    if data not in new_list:
      new_list.append(data)

  return new_list

print(f"Data List: {data_list}")

data_list = delete_duplicates(data_list)
print(f"Data List sesudah di seleksi: {data_list}")