def print_instruksi():
    print("===KALKULATOR SEDERHANA===")
    print("masukka 2 angka dan pilih operasi")
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")

def tambah_2_angka(angka_1, angka_2):
    return angka_1 + angka_2

def kurang_2_angka(angka_1, angka_2):
    return angka_1 - angka_2

def kali_2_angka(angka_1, angka_2):
    return angka_1 * angka_2

def bagi_2_angka(angka_1, angka_2):
    return angka_1 / angka_2

print_instruksi()

angka_1 = float(input("masukkan angka pertama: "))
angka_2 = float(input("masukkan angka kedua: "))

operasi = int(input("pilih operasi (1-4): "))

if operasi == 1:
    hasil = tambah_2_angka(angka_1, angka_2)
    print("Hasil penjumlahan:", hasil)

elif operasi == 2:
    hasil = kurang_2_angka(angka_1, angka_2)
    print("Hasil pengurangan:", hasil)

elif operasi == 3:
    hasil = kali_2_angka(angka_1, angka_2)
    print("Hasil perkalian:", hasil)

elif operasi == 4:
    if angka_2 != 0:
        hasil = bagi_2_angka(angka_1, angka_2)
        print("Hasil pembagian:", hasil)
    else:
        print("pembagi tidak boleh nol")
        exit()

else:
    print("pilihan operasi tidak valid")
    exit()

print("hasil =", hasil)
