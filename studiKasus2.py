"""
Nama    : Fahreza Zulfaqi
NIM     : 2601407
Kelas   : 1A
"""

import numpy as np

np.random.seed(42)
nilai_ujian = np.random.randint(50, 101, size=30)

nilai_terurut = np.sort(nilai_ujian)[::-1]

lima_nilai_terbesar = nilai_terurut[:5]

print("Data Nilai Awal (30 Siswa):")
print(nilai_ujian)

print("\nData Nilai Setelah Diurutkan (Terbesar ke Terkecil):")
print(nilai_terurut)

print("\n5 Nilai Terbesar:")
print(lima_nilai_terbesar)