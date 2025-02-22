# Port Checker

## Deskripsi

Script ini digunakan untuk mengecek port kosong pada sistem lokal. Pengguna dapat memilih untuk:

1. Mengecek ketersediaan port dalam rentang tertentu.
2. Mencari port kosong secara acak.

## Fitur

- Mengecek port dalam rentang yang ditentukan.
- Menemukan port kosong secara acak.
- Tampilan banner ASCII art saat script dijalankan.

## Prasyarat

- Python 3.x harus terinstal pada sistem.

## Instalasi

Tidak diperlukan instalasi tambahan. Cukup jalankan script menggunakan Python.

## Cara Penggunaan

1. Jalankan script dengan perintah:
   ```sh
   python port_checker.py
   ```
2. Pilih mode pengecekan:
   - Ketik `1` untuk mengecek rentang port tertentu.
   - Ketik `2` untuk mencari port kosong secara acak.
3. Jika memilih mode `1`, masukkan rentang port yang ingin diperiksa.
4. Jika memilih mode `2`, script akan mencari dan menampilkan satu port kosong.

## Contoh Output

```
Pilih mode pengecekan:
1. Cek rentang port tertentu
2. Cari port kosong secara acak
Masukkan pilihan (1/2): 1
Masukkan port awal: 8000
Masukkan port akhir: 8100

Mengecek port kosong dari 8000 hingga 8100...
Port 8001 tersedia.
Port 8005 tersedia.
...
```

## Lisensi

Proyek ini berlisensi **MIT License**. Bebas digunakan dan dimodifikasi.

## Kontributor

- Eddy Adha Saputra

## Repository

[GitHub Repository](https://github.com/eddyyucca/scan-port)
