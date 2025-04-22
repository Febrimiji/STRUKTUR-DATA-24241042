def sapa():
    print("Halo, selamat datang!")

sapa()  # Memanggil fungsi
sapa()
sapa()

# function dengan 1 parameter
def sapa_nama(nama):
    print(f"Halo, {nama}!")

# Pemanggilan Function
sapa_nama("Febrimiji")

# function dengan lebih dari 1 parameter
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" % luas)

# Pemanggilan Function
luas_segitiga(4, 6)

# function dengan nilai return(nilai kembali)
def tambah(a, b):
    return a + b

# pemanggilan fungsi
hasil = tambah(3, 5)
print("Hasil:", hasil)

# rumus sisi x sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas


# rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume

# pemanggilan fungsi
vol_persegi = volume_persegi(6)
print(f"Volume Persegi = {vol_persegi}")

def student(firstname, lastname ='Mark', standard ='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Standard')

# pemanggilan function, dengan 1 argumen
student("Wallberg")

# pemanggilan function, dengan 3 argumen
student('John', 'Gates', 'Seventh')  

# pemanggilan function dengan 2 argumen
student('John', 'Gates')               
student('John', 'Seventh')

def kali(a: int, b: int) -> int:
    return a * b

# Pemanggilan function
print("Hasil = " ,kali(3, 4))
print("Tipe Data : ", type(kali(3,4)))