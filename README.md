# Python untuk Pemula

Repositori latihan belajar dasar-dasar Python. Semua contoh kode ada di satu file, `python-pemula.py`, dan bukti hasil eksekusinya ada di folder `screenshots/`.

## Materi yang Dipelajari

1. **Pengenalan & Instalasi Python**: cek versi Python dan pip, membuat project dan virtual environment.
2. **Variabel dan Tipe Data**: integer, float, string, dan boolean.
3. **Operator**: aritmatika, perbandingan, dan logika (`and`, `or`, `not`).
4. **Kondisi If Else**: `if`, `elif`, `else`, dan aturan indentasi.
5. **Perulangan**: `for`, `while`, `break`, dan `continue`.
6. **Lists dan Dictionaries**: indexing, menambah, mengubah, dan menghapus item.
7. **Function**: argument, `*args`, `**kwargs`, dan default value.
8. **Class dan Object**: property, constructor, dan method.
9. **PIP dan Virtual Environments**: memasang library `colorama` di dalam venv.
10. **Konfigurasi Environment/IDE**: mengatur VS Code agar memakai interpreter venv.
11. **README.md & Requirements.txt**: dokumentasi proyek dan daftar dependensi.

## Cara Menjalankan

1. Clone repositori:

   ```
   git clone https://github.com/tiopermana496-svg/python-untuk-pemula.git
   cd python-untuk-pemula
   ```

2. Buat dan aktifkan virtual environment:

   ```
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Pasang dependensi:

   ```
   pip install -r requirements.txt
   ```

4. Jalankan program:

   ```
   python python-pemula.py
   ```

## Struktur Folder

```
python-untuk-pemula/
├── .vscode/settings.json   # konfigurasi interpreter VS Code
├── screenshots/            # bukti hasil eksekusi tiap bab
├── python-pemula.py        # kode seluruh materi
├── requirements.txt        # daftar dependensi
└── README.md
```