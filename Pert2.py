# Input nama
nama = input("Masukkan nama anda: ")

# Cek nama
if nama == "Kyla":
    print("Jika benar akan lanjut ke program selanjutnya")

    # Input angka
    angka = int(input("Masukkan angka: "))

    # Menampilkan tabel perkalian 1 sampai 10
    for i in range(1, 11):
        print(f"{angka} x {i} = {angka * i}")

else:
    print("Silahkan coba lagi")
