import os

def create(temp : list):
    with open("./data/data.txt", "a") as file:
        file.write(f"{temp[0]}\t\t\t{temp[1]}\t\t\t{temp[2]}\t\t{temp[3]}\n")
    file.close()
    print("\nData berhasil ditambahkan silahkan menekan tombol enter!")
    input()

def read():
    os.system('cls' if os.name == 'nt' else 'clear')
    no = 1
    with open("./data/data.txt", "r") as file:
        data = file.readlines()
    
    print(f"No.\t{data[0]}", end="")
    while no < len(data):
        print(f"{no}. \t{data[no]}", end="")
        no += 1
    print(f"\nData berhasil ditampilkan silahkan menekan tombol enter!")
    input()
    file.close()

def delete():
    os.system('cls' if os.name == 'nt' else 'clear')
    no = 1
    with open("./data/data.txt", "r") as file:
        data = file.readlines()
        
    print(f"No.\t{data[0]}", end="")
    while no < len(data):
        print(f"{no}. \t{data[no]}", end="")
        no += 1

    file.close()

    try:
        delete_data = int(input("\n Silahkan pilih nomor data yang ingin dihapus : "))
        if delete_data < 1 or delete_data >= len(data):
            print("Data tidak valid!")
            input()
        else:
            del data[delete_data]
            with open("./data/data.txt", "w") as file:
                file.writelines(data)
            print("Data berhasil dihapus silahkan menekan tombol enter!")
            input()
    except ValueError:
        print("Input tidak valid!.")
        input()

def edit():
    os.system('cls' if os.name == 'nt' else 'clear')
    no = 1
    with open("./data/data.txt", "r") as file:
        data = file.readlines()

    print(f"No.\t{data[0]}", end="")
    while no < len(data):
        print(f"{no}. \t{data[no]}", end="")
        no += 1
    file.close()

    try:
        edit_data = int(input("\n Silahkan pilih nomor data yang ingin diubah : "))
        if edit_data < 1 or edit_data >= len(data):
            print("Data tidak valid!")
            input()
        else:
            Name = input("Masukkan Nama Barang \t\t: ")
            Price = int(input("Masukkan Harga Satuan\t\t: "))
            Volume = int(input("Masukkan Volume \t\t: "))
            Total_Price = Price * Volume

            data[edit_data] = f"{Name}\t\t\t{Price}\t\t\t{Volume}\t\t{Total_Price}\n"
            with open("./data/data.txt", "w") as file:
                file.writelines(data)
            print("Data berhasil diubah silahkan menekan tombol enter!")
            input()
    except ValueError:
        print("Input tidak valid!.")
        input()

