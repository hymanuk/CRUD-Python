def choose_menu(): 
    choose = input("Masukkan pilihan menu (1-5): ")
    return choose

def create_input():
    Name = input("Masukkan Nama Barang \t\t: ")
    Price = int(input("Masukkan Harga Satuan\t\t: "))
    Volume = int(input("Masukkan Volume \t\t: "))
    Total_Price = Price * Volume

    Result = [Name, Price, Volume, Total_Price]

    return Result
