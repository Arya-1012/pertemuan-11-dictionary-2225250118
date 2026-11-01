# Pertemuan 11 - Dictionary/Map Python

**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Pendidikan Matematika FKIP Untirta  
**Tahun Ajaran:** 2026/2027 Ganjil

## Identitas Mahasiswa

- **Nama:** Isi nama kamu
- **NIM:** Isi NIM kamu
- **Kelas:** Isi kelas kamu

## Tujuan

1. Memahami konsep dictionary dan pasangan key-value dalam Python.
2. Mengakses data menggunakan key.
3. Menambah, mengubah, dan menghapus data dalam dictionary.
4. Menelusuri dictionary menggunakan `keys()`, `values()`, dan `items()`.
5. Menggunakan dictionary bersarang dan fungsi untuk mengolah data mahasiswa.
6. Menguji program menggunakan VS Code dan mengunggah hasilnya ke GitHub.

## Struktur Folder

```text
pertemuan-11-dictionary-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_dictionary.py
│   ├── 02_akses_get.py
│   ├── 03_manipulasi_dictionary.py
│   ├── 04_iterasi_dictionary.py
│   ├── 05_dictionary_bersarang.py
│   └── 06_fungsi_dictionary.py
└── praktik/
    └── data_mahasiswa.py
```

## Penjelasan Program

### 1. Dasar Dictionary
Membuat dictionary berisi NIM, nama, dan nilai mahasiswa serta menampilkan setiap value menggunakan key.

### 2. Akses Aman dengan get()
Mengakses data menggunakan `get()` agar program tetap berjalan ketika key tidak tersedia.

### 3. Manipulasi Dictionary
Menambahkan kelas, mengubah nilai mahasiswa, dan menghapus data menggunakan `pop()`.

### 4. Iterasi Dictionary
Menampilkan pasangan key dan value menggunakan `items()`.

### 5. Dictionary Bersarang
Menyimpan data mahasiswa dalam dictionary yang berisi dictionary lain.

### 6. Fungsi Dictionary
Membuat fungsi pencarian mahasiswa berdasarkan NIM.

### 7. Sistem Data Mahasiswa
Program utama untuk mencari mahasiswa, menambahkan data, memperbarui nilai, menampilkan seluruh data, dan menghitung rata-rata nilai.

## Cara Menjalankan

1. Buka folder proyek di Visual Studio Code.
2. Pastikan Python 3 sudah terpasang.
3. Buka terminal melalui menu **Terminal → New Terminal**.
4. Jalankan program utama dengan perintah:

```bash
python praktik/data_mahasiswa.py
```

Jika menggunakan perintah `py` di Windows:

```bash
py praktik/data_mahasiswa.py
```

Untuk menjalankan file latihan, gunakan contoh berikut:

```bash
python latihan/01_dasar_dictionary.py
```

## Test Case

| Pengujian | Input/Aksi | Hasil yang Diharapkan |
|---|---|---|
| Pencarian mahasiswa | NIM A003 | Data Citra ditampilkan |
| NIM tidak tersedia | NIM A999 | Data tidak ditemukan |
| Pembaruan nilai | A002 menjadi 82 | Nilai Budi berubah menjadi 82 |
| Penambahan mahasiswa | NIM A006 | Data Fajar berhasil ditambahkan |
| Rekap data | Menggunakan `items()` | Seluruh data mahasiswa ditampilkan |
| Rata-rata nilai | Menghitung seluruh nilai | Rata-rata 83,00 |

## Konsep yang Digunakan

- Dictionary dan pasangan key-value.
- Pengaksesan data menggunakan key.
- Method `get()`, `pop()`, `values()`, dan `items()`.
- Perulangan `for`.
- Percabangan `if-else`.
- Fungsi Python.
- Dictionary bersarang.
- Perhitungan rata-rata nilai.

## Refleksi

Dictionary memudahkan pencarian data mahasiswa berdasarkan NIM sebagai key. Penggunaan `get()` membantu menangani key yang tidak tersedia tanpa menimbulkan `KeyError`. Fungsi membuat program lebih terstruktur, sedangkan `items()` memudahkan penampilan seluruh data mahasiswa.

## Kesimpulan

Dictionary merupakan struktur data Python yang menyimpan pasangan key-value. Struktur ini cocok digunakan untuk mengelola data pendidikan, seperti NIM, nama, kelas, dan nilai mahasiswa. Program ini menerapkan pencarian, penambahan, pembaruan, penelusuran, dan perhitungan rata-rata nilai.

## Referensi

- Python Software Foundation. *Python 3 Documentation: Data Structures – Dictionaries*.
- Visual Studio Code Documentation. *Python in Visual Studio Code*.
- Bahan Ajar Algoritma dan Pemrograman, Pertemuan 11: Dictionary/Map dan Pasangan Key-Value.

