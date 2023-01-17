# menginput nilai Tugas, UTS, dan UAS
tugas = float(input("Masukkan Nilai Tugas : "))
uts = float(input("Masukkan Nilai UTS : "))
uas = float(input("Masukkan Nilai UAS : "))

# menghitung nilai akhir sesuai dengan bobot
nilai = (0.15 * tugas) + (0.35 * uts) + (0.50 * uas)

# mementukan grade berdasarkan nilai akhir
if nilai > 80:
    grade = 'A'
elif nilai > 70:
    grade = 'B'
elif nilai > 60:
    grade = 'C'
elif nilai > 50:
    grade = 'D'
else:
    grade = 'E'
# menentukan status kelulusan berdasarkan nilai akhir
if nilai > 60 :
    status = "lulus"
else :
    status = "tidak lulus"

#menampilkan nilai akhir, grade, dan status kelulusan
print("Nilai Akhir : %0.2f" % nilai)
print("Grade : {}",format(grade))
print("Status {}",format(status))