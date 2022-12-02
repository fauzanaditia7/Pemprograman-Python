from prettytable import PrettyTable

def isPrime(n: int):
    if 2 > n:
        return 0
    for i in range(2, n):
        if not n % i:
            return 0
    return n

def show_table(n: int):
    table = PrettyTable()
    table.field_names = ['Bilangan', 'Ganjil / Genap', 'Bilangan Prima']
    for i in range(1, n + 1):
        table.add_row([i, 'Ganjil' if i % 2 else 'Genap', 'Prima' if isPrime(i) else '-'])
    return table

n = (input("Masukkan batas n : "))
while not n.isdigit():  # Mengecek apakah user menginput bilangan atau string
    n = (input("Masukkan batas n : "))

print(show_table(int(n)))