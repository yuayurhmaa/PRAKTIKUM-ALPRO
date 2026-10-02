bahan_resep = ["tepung", "telur", "gula"]
skor = 0
print ("tebak 3 bahan resep berikut!")

bahan1 = input("bahan 1:")
if bahan1 in bahan_resep:
    print("tebakan benar")
    skor += 1 
else:
    print ("tebakan salah")

bahan2 = input ("bahan 2:")
if bahan2 in bahan_resep:
    print("tebakan benar")
    skor += 1
else:
    print ("tebakan salah")

bahan3= input ("bahan 3:")
if bahan3 in bahan_resep:
    print("tebakan benar")
    skor += 1
else:
    print("tebakan salah")

print("==permainan selesai==")
print("skor =", skor)
print("daftar bahan resep yang benar adalah", bahan_resep)