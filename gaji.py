from prettytable import PrettyTable

data = {
    "a": {
        "gaji_pokok": 1_200_000,
        "gaji_lembur": 5_000,
        "gaji_per_jam": 6_000
    },
    "b": {
        "gaji_pokok": 1_500_000,
        "gaji_lembur": 6_000,
        "gaji_per_jam": 8_000
    },
}

def show_table():
    table = PrettyTable()
    table.field_names = ['Golongan', 'Gaji Pokok', 'Gaji Lembur', 'Gaji Per Jam']
    for i in data:
        row = []
        row.append(i.upper())
        for j in data[i]:
            row.append(data[i][j])
        table.add_row(row)
    return table

print(show_table())

nama = input("Masukkan Nama : ")
golongan = input("Masukkan golongan [A/B] : ")

while (golongan.lower() not in data):
    golongan = input("Mohon masukkan [A/B] : ")
jam_kerja = int(input("Masukkan Jam Kerja : "))

print("\n---------Upah Karyawan PT ABC---------------")
print("Nama Karyawan : ", nama)
print("Jumlah Jam Kerja : ", jam_kerja)

lembur = (jam_kerja - 50) * data[golongan.lower()]['gaji_lembur'] if (50 < jam_kerja) else 0

gaji_pokok = jam_kerja * data[golongan.lower()]['gaji_per_jam']
pajak = 0.05 * gaji_pokok # 5 % x gaji_pokok

print("Lembur : Rp.", lembur)
print("Gaji : Rp.", gaji_pokok)
print("Pajak : Rp.", pajak)
print("Gaji Bersih : Rp.", ((gaji_pokok - pajak) + lembur))
print("-" * 45)
