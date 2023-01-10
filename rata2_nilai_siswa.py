print("================ PROGRAM NILAI KELAS X-PPLG ================")   # JUDUL
print("input berapa nilai?")

print("No. 1:")   # SISWA 1
namSis1 = input("Nama Siswa: ")   # INPUT NAMA SISWA 1
nTug1 = float(input("Nilai Tugas: "))   # INPUT NILAI TUGAS SISWA 1
nHar1 = float(input("Nilai Harian: "))   # INPUT NILAI HARIAN SISWA 1
nPTS1 = float(input("Nilai PTS: "))   # INPUT NILAI PTS SISWA 1
nPAS1 = float(input("Nilai PAS: "))  # INPUT NILAI PAS SISWA 1
print("---------------------")
nJum1 = nTug1+nHar1+nPTS1+nPAS1   # OPERASI JUMLAH SELURUH NILAI SISWA 1
nRata1 = nJum1/4   # OPERASI RATA-RATA SELURUH NILAI SISWA 1
print(f"Nama Siswa : {namSis1} \nJumlah Nilai : {nJum1} \nRata-rata Nilai : {nRata1}")   # OUTPUT SELURUHNYA
# STEP YANG SEBELUMNYA DI-ULANG UNTUK SISWA KE-2
print("No. 2:")
namSis2 = input("Nama Siswa: ")
nTug2 = float(input("Nilai Tugas: "))
nHar2 = float(input("Nilai Harian: "))
nPTS2 = float(input("Nilai PTS: "))
nPAS2 = float(input("Nilai PAS: "))
print("---------------------")
nJum2 = nTug2+nHar2+nPTS2+nPAS2
nRata2 = nJum2/4
print(f"Nama Siswa : {namSis2} \nJumlah Nilai : {nJum2} \nRata-rata Nilai : {nRata2}")

print("\n=========================")
print(f"Rata-rata kelas : {(nRata1+nRata2)/2}")   # OUTPUT RATA-RATA NILAI SELURUH KELAS
