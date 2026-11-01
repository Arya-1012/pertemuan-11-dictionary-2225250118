data = {
    "nama": "Ayu",
    "nilai": 85
}

# Menambahkan data
data["kelas"] = "A"

# Mengubah nilai
data["nilai"] = 90

print("Data setelah ditambahkan dan diubah:")
print(data)

# Menghapus data kelas
data.pop("kelas")

print("Data setelah kelas dihapus:")
print(data)