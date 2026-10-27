import os

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f'''
    ===================================================================
    
            Selamat datang di Aplikasi Catatan Penjualan Harian

    ===================================================================
    Silahkan pilih menu yang tersedia:
        1. Tambah Data Penjualan
        2. Lihat Data Penjualan
        3. Hapus Data Penjualan
        4. Edit Data Penjualan
        5. Keluar dari Program

    ''')


