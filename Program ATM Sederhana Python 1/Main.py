print("Selamat Datang di ATM BRTOD")
print("Pilih Option :")
print("1. Cek Saldo")
print("2. Ambil Uang")
print("3. Tabung")
option=int(input("Silahkan Pilih Option :"))
if option==1:
    print("Saldo Anda Berjumlah RP 100.000")
elif option==2:
    print("Saldo Anda Berjumlah RP 100.000, Ingin Ambil Berapa ?")
    print("1. RP 50.000")
    print("2. RP 100.000")
    uang_kamu=100000
    option2=int(input("Option :"))
    if option2==1:
        hasil=uang_kamu-50000
        print("Sisa Saldo Anda Adalah :", hasil)
    elif option2==2:
        hasil=uang_kamu-100000
        print("Sisa Saldo Anda Adalah :", hasil)
    else:
       print("Keyword Anda Salah")
elif option==3:
    uang_kamu=100000
    print("Uang Berjumlah RP 100.000, Mau Nabung Berapa ?")
    option3=int(input("Masukkan Jumlah Uang :"))
    hasil3=uang_kamu+option3
    print("Jumlah Saldo Anda Sekarang Adalah :", hasil3)
else:
    print("Keyword Anda Salah , Mohon Coba Lagi")

