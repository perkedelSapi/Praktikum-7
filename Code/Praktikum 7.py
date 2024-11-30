# Daftar nilai mahasiswa
MH = {}

# Fungsi untuk menambah data
def tambah(nama, nilai):
    MH[nama] = nilai
    print(f"Data mahasiswa {nama} dengan nilai {nilai} telah ditambahkan.")

# Fungsi untuk menampilkan data
def lihat():
    if MH:
        print("Daftar Mahasiswa dan Nilai:")
        for nama, nilai in MH.items():
            print(f"Nama: {nama}, Nilai: {nilai}")
    else:
        print("Tidak ada data mahasiswa.")

# Fungsi untuk menghapus data berdasarkan nama
def hapus(nama):
    if nama in MH:
        del MH[nama]
        print(f"Data mahasiswa {nama} telah dihapus.")
    else:
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

# Fungsi untuk mengubah data berdasarkan nama
def ubah(nama, nilai_baru):
    if nama in MH:
        MH[nama] = nilai_baru
        print(f"Data mahasiswa {nama} telah diubah menjadi nilai {nilai_baru}.")
    else:
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

# Menu untuk pilihan
def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Lihat Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        pilihan = input("(T)ambah, (L)ihat, (H)apus, (U)bah, (K)eluar: ")

        if pilihan == 't':
            nama = input("Masukkan nama mahasiswa: ")
            nilai = input("Masukkan nilai mahasiswa: ")
            tambah(nama, nilai)
        elif pilihan == 'l':
            lihat()
        elif pilihan == 'h':
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            hapus(nama)
        elif pilihan == 'u':
            nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
            nilai_baru = input("Masukkan nilai baru: ")
            ubah(nama, nilai_baru)
        elif pilihan == 'k':
            break
        else:
            print("coba lagi.")

menu()