print("Halo Python")



# Tipe data floating numbers
a = 7.5

print(a)


# Tipe data integers
x = 5
y = 3
z = 5 + 3

print(z)

# Tipe data floating numbers
a = 7.5

print(a)







# Menggunakan single quote
myFirstName = 'Rizqi'

# Menggunakan double quote
myLastName = "Maulana"

# Penulisan Angka sebagai string
myAge = "25"

# Penulisan string multiline
myHobby = """Hobi saya adalah
bersepeda dan bermain game.
"""

# Mencetak 2 variabel string dengan perintah print
print(myFirstName + " " + myLastName)
print("Umur saya " + myAge)




# Contoh penulisan boolean yang benar
a = True
b = False

# Contoh penulisan boolean yang salah
# Jika dijalankan, pada baris ini akan error
# c = true
# print(c)




# Operator aritmatika
a = 4
b = 2
c = a + b    # Penjumlahan
d = a - b    # Pengurangan
e = a * b    # Perkalian
f = a / b    # Pembagian
g = a % b    # Modulus
h = a ** b   # Eksponensial

print(c) # 6
print(d) # 2
print(e) # 8
print(f) # 2.0
print(g) # 0
print(h) # 16


# Operator perbandingan
a = 3
b = 5
c = a == b   # sama dengan
d = a != b   # tidak sama dengan
e = a < b    # lebih kecil
f = a <= b   # lebih kecil sama dengan
g = a > b    # lebih besar
h = a >= b   # lebih besar sama dengan

print(c) # False
print(d) # True
print(e) # True
print(f) # True
print(g) # False
print(h) # False


# Operator logika
a = 3
b = 9

# and
print(a < 5 and b > 6) # True
print(a < 5 and b < 6) # False
print(a > 5 and b < 6) # False

# or
print(a < 5 or b > 6) # True
print(a < 5 or b < 6) # True
print(a > 5 or b < 6) # False

# not
print(not(a < 5 or b > 6)) # False
print(not(a > 5 or b < 6)) # True





"""
Note:
Penulisan kode di dalam blok atau scope pada Python bergantung pada
indentation (spasi di awal baris).
"""

# Penulisan yang benar:
if(True):
    print("Benar.")

x = 5
y = 10

if(x < y):
    print("nilai x lebih kecil dari y.") # dijalankan

if(x > y):
    print("nilai x lebih besar dari y.") # tidak dijalankan


# if - elif
a = 80

if(a > 90):
    print("Dapat nilai A.") # tidak dijalankan
elif(a > 70):
    print("Dapat nilai B.") # dijalankan


# if - elif - else
a = 60

if(a > 90):
    print("Dapat nilai A.") # tidak dijalankan
elif(a > 70):
    print("Dapat nilai B.") # tidak dijalankan
else:
    print("Dapat nilai C.") # dijalankan






# Mencetak kata "Halo Python" sebanyak 5 kali
for x in range(5):
    print("Halo Python.")


# Mencetak semua item pada list fruits
fruits = ['Apple', 'Banana', 'Mango', 'Durian']
for fruit in fruits:
    print(fruit)

# Mencetak semua huruf pada kata "indonesia"
myCountry = "indonesia"
for x in myCountry:
    print(x)


# While loop: mencetak angka selama counter lebih kecil dari 5
counter = 0
while counter < 5:
    print(counter)
    counter += 1


# break: hentikan perulangan jika x adalah 3
for x in range(5):
    print(x)
    if x == 3:
        break


# continue: lewati angka genap, hanya cetak angka ganjil
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)







# Mengakses item (indexing)
animals = ["Ayam", "Bebek", "Cicak"]

print(animals[1])  # Bebek
print(animals[-1]) # Cicak
print(animals[-2]) # Bebek


# Menambah item
animals = ["Ayam", "Bebek", "Cicak"]

animals.append("Domba")
print(animals) # ['Ayam', 'Bebek', 'Cicak', 'Domba']

animals.insert(2, "Buaya")
print(animals) # ['Ayam', 'Bebek', 'Buaya', 'Cicak', 'Domba']


# Menghapus item
animals = ["Ayam", "Bebek", "Cicak"]
animals.remove("Bebek")
print(animals) # ['Ayam', 'Cicak']

animals = ["Ayam", "Bebek", "Cicak"]
animals.pop()
print(animals) # ['Ayam', 'Bebek']

animals = ["Ayam", "Bebek", "Cicak"]
animals.pop(0)
print(animals) # ['Bebek', 'Cicak']

animals = ["Ayam", "Bebek", "Cicak"]
animals.clear()
print(animals) # []


# Menggabungkan list
animals = ["Ayam", "Bebek", "Cicak"]
otherAnimals = ["Domba", "Elang", "Gajah"]
animals.extend(otherAnimals)
print(animals) # ['Ayam', 'Bebek', 'Cicak', 'Domba', 'Elang', 'Gajah']

fruits = ["Apel", "Mangga", "Pisang"]
otherFruits = ["Durian", "Semangka", "Jeruk"]
allFruits = fruits + otherFruits
print(allFruits) # ['Apel', 'Mangga', 'Pisang', 'Durian', 'Semangka', 'Jeruk']