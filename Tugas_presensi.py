# Data mahasiswa (Array)
mahasiswa = [
    ["Andi", "Tinggi", "Lengkap"],
    ["Budi", "Rendah", "Tidak Lengkap"],
    ["Citra", "Tinggi", "Tidak Lengkap"],
    ["Deni", "Rendah", "Lengkap"],
    ["Alya", "Tinggi", "Lengkap"]
]

# Warna
PINK = "\033[95m"
HIJAU = "\033[92m"
MERAH = "\033[91m"
RESET = "\033[0m"

# Variabel Rekap
aktif = 0
tidak_aktif = 0
bonus_ya = 0

print(PINK + "=" * 60)
print("SISTEM PRESENSI MAHASISWA - DECISION TREE SEDERHANA")
print("=" * 60 + RESET)

for data in mahasiswa:
    nama = data[0]
    kehadiran = data[1]
    tugas = data[2]

    # Decision Tree
    if kehadiran == "Tinggi":
        status = "Aktif"
        warna_status = HIJAU
        aktif += 1
    else:
        status = "Tidak Aktif"
        warna_status = MERAH
        tidak_aktif += 1

    # Fitur Bonus
    if kehadiran == "Tinggi" and tugas == "Lengkap":
        bonus = "Ya"
        bonus_ya += 1
    else:
        bonus = "Tidak"

    print()
    print(PINK + "Nama       :" + RESET, nama)
    print(PINK + "Kehadiran  :" + RESET, kehadiran)
    print(PINK + "Tugas      :" + RESET, tugas)
    print(PINK + "Status     :" + RESET, warna_status + status + RESET)
    print(PINK + "Bonus      :" + RESET, bonus)
    print(PINK + "-" * 60 + RESET)

# Rekap Data
print()
print(PINK + "=" * 60)
print("REKAP DATA MAHASISWA")
print("=" * 60 + RESET)
print("Jumlah Mahasiswa      :", len(mahasiswa))
print("Mahasiswa Aktif       :", aktif)
print("Mahasiswa Tidak Aktif :", tidak_aktif)
print("Penerima Bonus        :", bonus_ya)
print(PINK + "=" * 60 + RESET)

print("\nProgram selesai.")