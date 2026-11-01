def cari_mahasiswa(data, nim):
    """Mencari mahasiswa berdasarkan NIM."""
    return data.get(nim)


def rata_rata_nilai(data):
    """Menghitung rata-rata nilai seluruh mahasiswa."""
    if len(data) == 0:
        return 0

    total = 0

    for info in data.values():
        total += info["nilai"]

    return total / len(data)


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# 1. Mencari mahasiswa berdasarkan NIM
print("=== PENCARIAN MAHASISWA ===")

nim = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim)

if hasil is not None:
    print(f"NIM: {nim}")
    print(f"Nama: {hasil['nama']}")
    print(f"Kelas: {hasil['kelas']}")
    print(f"Nilai: {hasil['nilai']}")
else:
    print("Data tidak ditemukan")

# Menguji NIM yang tidak tersedia
print("\n=== PENCARIAN NIM TIDAK TERSEDIA ===")

nim = "A999"
hasil = cari_mahasiswa(data_mahasiswa, nim)

if hasil is not None:
    print(hasil)
else:
    print("Data tidak ditemukan")

# 2. Menambahkan mahasiswa baru
print("\n=== MENAMBAHKAN MAHASISWA ===")

data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

print("Mahasiswa A006 berhasil ditambahkan.")

# 3. Mengubah nilai mahasiswa
print("\n=== MEMPERBARUI NILAI ===")

data_mahasiswa["A002"]["nilai"] = 82

print("Nilai Budi berhasil diubah menjadi 82.")

# 4. Menampilkan seluruh data mahasiswa
print("\n=== SELURUH DATA MAHASISWA ===")

for nim, info in data_mahasiswa.items():
    print(
        f"NIM: {nim} | "
        f"Nama: {info['nama']} | "
        f"Kelas: {info['kelas']} | "
        f"Nilai: {info['nilai']}"
    )

# 5. Menghitung rata-rata nilai
print("\n=== RATA-RATA NILAI ===")

rata_rata = rata_rata_nilai(data_mahasiswa)

print(f"Rata-rata nilai mahasiswa: {rata_rata:.2f}")