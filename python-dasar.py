# Bab 1: Pengenalan & Instalasi Python
# Program pertama: menampilkan teks ke layar
print("Hello, World!")

# Menampilkan versi Python yang terpasang
import sys
print("Versi Python:", sys.version)





# Bab 3: Tipe Data Dasar
nama = "Budi"          # str (teks)
umur = 17              # int (bilangan bulat)
tinggi = 170.5         # float (bilangan desimal)
siswa = True           # bool (benar/salah)

print(nama, type(nama))
print(umur, type(umur))
print(tinggi, type(tinggi))
print(siswa, type(siswa))

# Konversi tipe data (casting)
angka_teks = "25"
angka = int(angka_teks)
print(angka + 5)
print(str(umur) + " tahun")
print(float(umur))
print(bool(0), bool(1))