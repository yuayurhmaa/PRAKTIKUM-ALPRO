available_pizzas = ["papperoni", "Cheese", "hawaian", "veggie"]

pizza_order = []
total_harga = 0 

lanjut_pesan = 'ya' 

while lanjut_pesan.lower() == 'ya':

    print("/nDaftar Pizza:")
    for i, pizza in enumerate(available_pizzas, start=1):
        print(i, ".", pizza)

    pilihan = int(input("pilih nomor pizza:"))

    if 1 <= pilihan <= len(available_pizzas):
        pizza_order.append(available_pizzas[pilihan - 1])
        total_harga += 10
        print("pizza ditambahkan ke pesanan Anda.")
    else:
        print("nomor pizza tidak valid. ")

    lanjut_pesan = input("apakah anda ingin tambah pizza lagi? (ya/tidak): ")

tip = int(input("Masukkan tip untuk pengiriman (0-25%): "))

while tip < 0 or tip > 25:
    tip = int(input("tip harus antara 0 dan 25%. Masukkan tip untuk pengiriman (0-25%): "))

total_harga += total_harga * (tip / 100)

print("/n====STRUK PESANAN PIZZA====")
print("pesanan:", pizza_order)
print("total pembayaran: ", total_harga)
print("pesanan sedang diproses. Terima kasih!")