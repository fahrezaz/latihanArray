"""
Nama    : Fahreza Zulfaqi
NIM     : 2601407
Kelas   : 1A
"""

import numpy as np

nilai_ujian = np.array([
    75, 88, 62, 95, 80, 55, 90, 83, 70, 68,
    92, 78, 85, 60, 98, 73, 89, 66, 91, 77,
    84, 58, 96, 71, 86, 79, 64, 100, 82, 69
])

nilai_terurut = np.sort(nilai_ujian)[::-1]

lima_nilai_terbesar = nilai_terurut[:5]

print("Data Nilai Awal (30 Siswa):")
print(nilai_ujian)

print("\nData Nilai Setelah Diurutkan (Terbesar ke Terkecil):")
print(nilai_terurut)

print("\n5 Nilai Terbesar:")
print(lima_nilai_terbesar)