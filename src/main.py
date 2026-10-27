import os
import lib.output as out
import lib.input as inp
import lib.file as fl

try:
    with open("./data/data.txt", "r") as file:
        data = file.readlines()
except FileNotFoundError:   
    if not os.path.exists("./data"):
        os.makedirs("./data")
    with open("./data/data.txt", "w") as file:
        file.write("Nama Barang\t\tHarga Satuan\t\tVolume\t\tTotal Harga\n")


while True:
    out.main_menu()
    choice = inp.choose_menu()
    if choice == "1":
        fl.create(inp.create_input())
    elif choice == "2":
        fl.read()
    elif choice == "3":
        fl.delete()
    elif choice == "4":
        fl.edit()
    elif choice == "5":
        print("Terima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
        continue
