print("Soal 2a")
my_tup = ('g', 'a', 'n', 't', 'e', 'n', 'g')
print(my_tup)
for huruf in my_tup:
    print(huruf, end="")

print("\n\nSoal 2b")
my_dict = {
    'bilangan_1' : 90,
    'bilangan_2' : -54,
    'bilangan_3' : 0.4
    }
print(f"{my_dict}")
hasil = 0
for k, v in my_dict.items():
    hasil += v
print(hasil)

print("\n\nSoal 2c")
angka = int(input("masukan angka : "))+1
my_dict2 = {}
for i in range(1,angka):
    my_dict2[i] = i*i
print(my_dict2)

print("\n\nSoal 2d")
my_dict3 = {
  'a': 1,
  'b': 2,
  'c': 3,
  'd': 4
  }
print(my_dict3)
my_dict3.pop("a")
print(my_dict3)
