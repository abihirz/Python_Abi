print("===========Input Nilai Tugas===========")
print()
nilai = int(input("Masukkan Nilai = "))

if nilai > 100 :
    print("Tidak Masuk Akal Dan Di Luar Nalar")
elif nilai >= 80 :
    print("Output Nilai Tugas = A")
elif nilai >= 70 :
    print("Output Nilai Tugas = B")
elif nilai >= 60 :
    print("Output Nilai Tugas = C")
else :
    print("Output Nilai Tugas = D")