import os
import time
import pwinput
from prettytable import PrettyTable

produk = [
    {'nama': 'Kopi Susu', 'modal': 10000, 'harga_jual': 15000},
    {'nama': 'Teh Tarik', 'modal': 8000, 'harga_jual': 12000}
]

#program oleh : Muhammad Ibrahim Kamil - 2509116012 - Sistem Informasi A

pengguna = {
    'marwoto': {'password': 'mgr123', 'role': 'manager'},
    'bastian': {'password': 'kry123', 'role': 'karyawan'}
}

def clear(): #INI BUAT BERSIHIN LAYAR YGY!!!
    os.system('cls')

def read(read1=False):
    if not produk:
        print("> Belum ada produk yang ditambahkan.")
        return False 

    tabel = PrettyTable()
    if read1:
        tabel.field_names = ["no.", "nama produk", "modal", "harga jual"]
        nomor = 1 
        for item in produk: 
            tabel.add_row([nomor, item['nama'], item['modal'], item['harga_jual']]) 
            nomor += 1 
    else:
        tabel.field_names = ["nama produk", "modal", "harga jual"]
        for item in produk:
            tabel.add_row([item['nama'], item['modal'], item['harga_jual']])
    
    print(tabel)
    return True

def add(): 
    clear()
    print("|| Menambah Produk Baru ||")
    nama = input("Input Nama Produk: ")
    while True:
        try:
            modal = int(input("Input Modal (Rp): "))
            harga_jual = int(input("Input Harga Jual (Rp): "))
            break
        except ValueError:
            print("> Input modal dan harga harus berupa angka masbro.")

    produk.append({'nama': nama, 'modal': modal, 'harga_jual': harga_jual})
    print(f"\n> Produk '{nama}' ditambahkan masbro.")

def update():
    clear()
    print("| Mengedit Produk |")
    if not read(read1=True):
        return

    try:
        pilihan = int(input("Masukkan nomor produk: "))
        indeks = pilihan - 1
        produk_lama = produk[indeks] 
        
        print(f"Mengedit: {produk_lama['nama']}")
        nama_baru = input("edit nama (kosong jika tidak diubah): ")
        modal_baru = input("edit modal (kosong jika tidak diubah): ")
        harga_jual_baru = input("edit harga (kosong jika tidak diubah): ")

        if nama_baru:
            produk[indeks]['nama'] = nama_baru
        if modal_baru:
            produk[indeks]['modal'] = int(modal_baru)
        if harga_jual_baru:
            produk[indeks]['harga_jual'] = int(harga_jual_baru)
        
        print("\n> Produk berhasil diupdate masbro!")

    except ValueError:
        print("> Input harus berupa angka kocak")
    except IndexError:
        print("> Nomor produk ga valid woi")

def delete(): 
    clear()
    print("|| Menghapus Produk ||")
    if not read(read1=True):
        return

    try:
        pilihan = int(input("Masukkan nomor produk yang akan dihapus: "))
        indeks = pilihan - 1
        
        nama_produk_hapus = produk[indeks]['nama'] 
        
        konfirm = input(f"Yakinn hapus produk '{nama_produk_hapus}'? (y/n): ")
        if konfirm == 'y':
            produk.pop(indeks)
            print(f"\n> Produk '{nama_produk_hapus}' dihapus.")
        else:
            print("> Penghapusan dibatalkan.")

    except ValueError:
        print("> Input harus berupa angka kocak")
    except IndexError:
        print("> Nomor produk ga valid woi")

def menu_manager(): 

    while True:
        print("\n|| Menu Manager Produksi UMKM ||")
        print("|1. Lihat Produk")
        print("|2. Tambah Produk")
        print("|3. Edit Produk")
        print("|4. Hapus Produk")
        print("|5. Logout")
        menu = input("Pilih menu (1-5): ")

        if menu == "1":
            clear()
            print("| Daftar Produk |")
            read()
        elif menu == "2":
            add()
        elif menu == "3":
            update()
        elif menu == "4":
            delete()
        elif menu == "5":
            time.sleep(1)
            print("logout berhasil masbro")
            break
        else:
            print("> Pilihan ga valid masbro")
        
        input("\nTekan enter untuk kembali ke menu masbro...")
        time.sleep(1)
        clear()

def menu_karyawan(): 
    while True:
        print("\n|| Menu Karyawan Produksi UMKM ||")
        print("|1. Lihat Produk")
        print("|2. Logout")
        menu = input("Pilih menu (1-2): ")

        if menu == "1":
            clear()
            print("| Daftar Produk |")
            read()
        elif menu == "2":
            time.sleep(1)
            print("logout berhasil masbro, mangadd kerjanya >W< -manager tersayang🥰")
            break
        else:
            print("> Pilihan tidak valid masbro.")

        input("\ntekan Enter untuk kembali ke menu masbro...")
        time.sleep(1)
        clear()

def login(): 
    while True:
        clear()
        print("|| Login sistem Manajemen Produksi UMKM ||")
        username = input("Username: ")
        password = pwinput.pwinput("Password: ")

        if username in pengguna and pengguna[username]['password'] == password:
            print("\nLogin berhasil!")
            input("Tekan enter untuk melanjutkan masbro...")
            time.sleep(1)
            clear()
            return pengguna[username]['role'] 
        else:
            print("\n> Username/password salah. Coba lagi masbroo")
            input("Tekan enter untuk mencoba lagi masbro...")
            time.sleep(1)

def main():
    try:
        while True:
            role = login()
            if role == 'manager':
                menu_manager()
            elif role == 'karyawan':
                menu_karyawan()
            
            pilihan_akhir = input("Apakah masbro ingin login lagi? (y/n): ")
            if pilihan_akhir != 'y':
                time.sleep(1)
                break
        print("\nTerima kasih telah menggunakan program.")

    except KeyboardInterrupt:
        print("\nProgram berhenti gara gara si kocak ini teken ctrl+c")

main()