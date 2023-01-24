# Membuat Variabel Global
nama = "Python"
versi = "1.0.0"

def help():
    #variabel lokal
    nama = "c#"
    versi = "1.0.2"
    #akses variabel lokal
    print ("Nama : %s" % nama)
    print("Versi : %s" % versi)

#akses variabel global
print("Nama : %s" % nama)
print("Versi : %s" % versi)

#memanggil fungsi help()
help()