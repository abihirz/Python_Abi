#menghitung angka
angka = int(input("Masukkan Angka : "))

#jika habis dibagi nol, maka genap
if (angka % 2) == 0:
    print("{0} adalah bilangan genap",format(angka))

#jika tidak habis di bagi nol, maka ganjil
else:
    print("{0} adalah bilangan ganjil",format(angka))