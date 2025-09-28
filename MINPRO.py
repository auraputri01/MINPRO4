# Nama  : Aura Putri Anandita Syarif
# NIM   : 2509116094
# Prodi : Sistem Informasi


users = {
    "manager": {"password": "manager123", "role": "Manager"},
    "karyawan": {"password": "karyawan123", "role": "Karyawan"}
}

produk_db = {}

def login():
    print("=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")
    user = users.get(username)
    if user and user["password"] == password:
        print(f"Login berhasil sebagai {user['role']}\n")
        return user["role"]
    else:
        print("Login gagal Username atau password salah.\n")
        return None

def create_produk():
    try:
        kode = input("Kode Produk: ")
        nama = input("Nama Produk: ")
        kategori = input("Kategori: ")
        harga = float(input("Harga: "))
        stok = int(input("Stok: "))
        produk_db[kode] = {
            "nama": nama,
            "kategori": kategori,
            "harga": harga,
            "stok": stok
        }
        print("Data produk berhasil ditambahkan\n")
    except Exception as e:
        print(f"Terjadi kesalahan input: {e}\n")

def read_produk(role="Karyawan"):
    if not produk_db:
        print("Belum ada data produk.\n")
        return
    for kode, data in produk_db.items():
        print(f"Kode: {kode}, Nama: {data['nama']}, Kategori: {data['kategori']}, Harga: {data['harga']}, Stok: {data['stok']}")
    print()

def update_produk(role="Manager"):
    kode = input("Masukkan kode produk yang ingin diupdate: ")
    if kode in produk_db:
        try:
            if role == "Manager":
                nama = input("Nama baru: ")
                kategori = input("Kategori baru: ")
                harga = float(input("Harga baru: "))
                stok = int(input("Stok baru: "))
                produk_db[kode] = {
                    "nama": nama,
                    "kategori": kategori,
                    "harga": harga,
                    "stok": stok
                }
                print("Data produk berhasil diupdate\n")
            elif role == "Karyawan":
                print(f"Data produk saat ini:")
                print(f"Kode: {kode}")
                print(f"Nama: {produk_db[kode]['nama']}")
                print(f"Kategori: {produk_db[kode]['kategori']}")
                print(f"Harga: {produk_db[kode]['harga']}")
                print(f"Stok saat ini: {produk_db[kode]['stok']}")
                stok = int(input("Masukkan jumlah stok baru: "))
                produk_db[kode]['stok'] = stok
                print("Stok produk berhasil diupdate\n")
        except Exception as e:
            print(f"Terjadi kesalahan input: {e}\n")
    else:
        print("Kode produk tidak ditemukan\n")

def delete_produk():
    kode = input("Masukkan kode produk yang ingin dihapus: ")
    if kode in produk_db:
        del produk_db[kode]
        print("Data produk berhasil dihapus\n")
    else:
        print("Kode produk tidak ditemukan\n")

def main():
    role = None
    while not role:
        role = login()
    while True:
        print("=== MENU ===")
        if role == "Manager":
            print("1. Tambah Produk (Create)")
            print("2. Lihat Data Produk (Read)")
            print("3. Update Data Produk (Update)")
            print("4. Hapus Data Produk (Delete)")
        elif role == "Karyawan":
            print("1. Lihat Data Produk (Read)")
            print("2. Update Stok Produk")
        print("5. Logout")
        print("6. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if role == "Manager":
            if pilihan == "1":
                create_produk()
            elif pilihan == "2":
                read_produk(role)
            elif pilihan == "3":
                update_produk(role)
            elif pilihan == "4":
                delete_produk()
        elif role == "Karyawan":
            if pilihan == "1":
                read_produk(role)
            elif pilihan == "2":
                update_produk(role)
            if pilihan == "1":
                read_produk(role)
                
        if pilihan == "5":
            print("Logout...\n")
            role = None
            while not role:
                role = login()
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        elif pilihan not in ["1", "2", "3", "4", "5", "6"]:
            print("Pilihan tidak valid\n")

if __name__ == "__main__":
    main()