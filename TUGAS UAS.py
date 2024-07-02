#CONTOH PERCABANGAN
Nama = input("Masukan nama anda: ")
if Nama == "Ahmad" :
    print("Selamat Datang Ahmad")
else:
    print("Maaf Nama yang anda berikan salah")
    print("program selesai, thanks {Nama}")

    #CONTOH PERULANGAN MENGGUNAKAN LIST
    bil = [0,1,2,3,4,5,6,7,8,9,10]
    print(bil)
    for i in bil:
        print(f"Nilai i adalah -> {i}")
        print("Akhir Program perulang list")

        #CONTOH PERULANGAN MENGGUNAKAN RANGE
        bil2 = range(5)
        for i in bil2:
            print (f"Nilai i adalah -> {i}")

            print ("Akhir program perulangan range")
