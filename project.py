"""
PROJECT SCHOOL GRADES
"""
def cari_minimum(daftar_nilai):
    minimum = daftar_nilai[0]

    for nilai in daftar_nilai:
        if nilai < minimum:
            minimum = nilai

        return minimum

def cari_maksimum(daftar_nilai):
    maksimum = daftar_nilai[0]

    for nilai in daftar_nilai:
        if nilai > maksimum:
            maksimum = nilai

    return maksimum

def hitung_rata_rata(daftar_nilai):
    total = 0

    for nilai in daftar_nilai:
        total += nilai

    return total / len(daftar_nilai)

nilai = []

while True:
    data = float(input("masukkkan nilai (1-10), ketik -1 untuk selesai:"))

    if data == -1:
        break

    if 0 <= data <= 10:
        nilai.append(data)
    else:
        print("nilai harus antara 0 sampai 10")

if len(nilai) == 0:
    print("tidak ada nilai yang dimasukkan")
else:
    minimum = cari_minimum(nilai)
    maksimum = cari_maksimum(nilai)
    rata_rata = hitung_rata_rata(nilai)

    print("\n ==== HASIL ===")
    print("jumlah nilai: ", len(nilai))
    print("nilai minimum: ", minimum)
    print("nilai maksimum: ", maksimum)
    print("nilai rata-rata:", round(rata_rata, 2))