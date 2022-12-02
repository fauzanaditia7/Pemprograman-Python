from prettytable import PrettyTable

data = {
    "A": {
        "nama_barang": "pensil",
        "harga": 2500
    },
    "B": {
        "nama_barang": "pulpen",
        "harga": 3500
    },
    "C": {
        "nama_barang": "buku",
        "harga": 5000
    },
    "D": {
        "nama_barang": "penggaris",
        "harga": 6000
    }
}

def show_table():
    table = PrettyTable()
    table.field_names = ["No", "Kode Barang", "Nama Barang", "Harga"]
    for i, item in enumerate(data, start=1):
        table.add_row([i, item, data[item]['nama_barang'].capitalize(), data[item]['harga']])
    return table

print(show_table())
list_beli = []
nama = input("Masukkan Nama : ")

while True:
    b = input("Masukkan kode barang yang ingin dibeli : ")
    if b.upper() not in data:
        continue
    list_beli.append(data[b.upper()])
    if input("Lanjutkan membeli ? [Y/N] : ").upper() == "N":
        break

total_harga = 0
text = ""
for i, item in enumerate(list_beli, start=1):
    text += f"\n{i}. {item['nama_barang'].capitalize()} - Rp. {item['harga']}"
    total_harga += item['harga']

print("\nNama Pembeli :", nama)
print(text)
print("\nTotal harga yang harus dibayar RP.", total_harga)