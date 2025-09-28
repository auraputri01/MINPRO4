# MINPRO4
# MINPRO - Sistem Manajemen Produk

Program Python sederhana buat ngatur data produk dengan sistem login Manager sama Karyawan.

## Apa itu MINPRO?

Ini tuh aplikasi CRUD basic yang bikin kita bisa kelola produk di terminal. Ada dua role:
- **Manager**: Bisa ngapain aja (tambah, edit, hapus produk)
- **Karyawan**: Cuma bisa liat produk sama update stok doang

## Cara Pake

1. Pastiin Python udah install
2. Download file `MINPRO.py`
3. Jalanin di terminal:
```bash
python MINPRO.py
```

## Login Info

**Manager:**
- Username: `manager`
- Password: `manager123`

**Karyawan:**
- Username: `karyawan` 
- Password: `karyawan123`

## Fitur

### Manager bisa:
- ➕ Tambah produk baru
- 👀 Liat semua produk
- ✏️ Edit produk (nama, kategori, harga, stok)
- ❌ Hapus produk

### Karyawan bisa:
- 👀 Liat produk
- 📦 Update stok aja

## Data Produk

Tiap produk punya:
- Kode produk (ID unik)
- Nama
- Kategori  
- Harga
- Stok

## Catatan

- Data disimpen di memory doang, jadi kalau program ditutup data hilang
- Ada error handling buat input yang salah
- Interface masih text-based alias ga ada GUI

## Info

Dibuat sama Aura Putri Anandita Syarif (2509116094) - Sistem Informasi

---

*Program ini dibuat buat tugas kuliah, jadi ya gitu deh simple banget 😅*
