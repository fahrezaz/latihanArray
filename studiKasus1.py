"""
Nama    : Fahreza Zulfaqi
NIM     : 2601407
Kelas   : 1A
"""

import numpy as np

suhu_celcius = np.array([28.5, 29.0, 31.2, 30.1, 27.8, 29.5, 32.0, 30.5, 28.9, 29.8])

suhu_fahrenheit = (suhu_celcius * 9/5) + 32

print("Suhu Celcius    :", suhu_celcius)
print("Suhu Fahrenheit :", np.round(suhu_fahrenheit, 2))