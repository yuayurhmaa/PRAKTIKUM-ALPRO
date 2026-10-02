daftar_buah=["apel", "pisang", "strawberry"]

buah = input("buah apa yang kamu inginkan?")

if buah not in daftar_buah:
    print("saya tidak memiliki", buah)
else:
    print("OK")