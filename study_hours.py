jam_tidur= int(input("jam tidur per hari:   "))
jam_kuliah= int(input("jam kuliah per hari:"))
jam_istirahat_akhir_pekan=int(input("jam istirahat akhir pekan:"))
jam_istirahat_hari_kerja=int (input("jam istirahat hari kerja"))

# menghitung total jam belajar hari kerja
jam_belajar_hari_kerja= (24 - jam_tidur - jam_kuliah - jam_istirahat_hari_kerja - 3)

#menghitung total jam belajar akhir pekan
jam_belajar_akhir_pekan= (24 - jam_tidur - jam_istirahat_akhir_pekan - 3)

# menghitung total jam belajar per minggu
total_jam_belajar = (
    (jam_belajar_hari_kerja * 5) +
    (jam_belajar_akhir_pekan * 2))

print ("===HASIL PERHITUNGAN===")
print("jam belajar hari kerja :", jam_belajar_hari_kerja)
print("jam belajar akhir pekan:", jam_belajar_akhir_pekan)
print("total jam belajar per minggu :", total_jam_belajar)
