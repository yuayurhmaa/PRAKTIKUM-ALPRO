negara = input("masukkan negara:")
umur = int(input("masukka umur:"))

if negara == "south africa":
    if umur >= 16:
        print("anda boleh mengemudi")
    else:
        print("anda tidak boleh mengemudi")

elif negara == "mexico":
    if umur >= 17:
        print("anda boleh mengemudi")
    elif umur == 16:
        print("boleh mengemudi dengan izin orang tua")
    elif umur == 15:
        print("boleh mengemudi dengan pengawasan orangt tua")
    else:
        print("anda belum boleh mengemudi")

elif negara == "india":
    if umur >= 18:
        print("anda boleh mengemudi")
    else:
        print("anda belum boleh mengemudi")

elif negara == "france":
    if umur >= 18:
        print("anda boleh mengemudi")
    elif umur >= 15:
        print("boleh mengemudi dengan pengawasan")
    else:
        print("anda belum boleh mengemudi")

else:
    print("data tidak tersedia untuk negara tersebut")