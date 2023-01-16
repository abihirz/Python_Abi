array = []
total = 0
n = int(input("Masukkan Jumlah Elemen Array : "))
for a in range (n) :
    nilai = float(input("Masukkan Nilai ke- {} : ".format(a+1)))
    array.append(nilai)
    print("\nHasil nilai total adalah : {}",format(sum(array)))
    print("Hasil Rata-Rata Adalah : {}",format(sum(array)/n))
