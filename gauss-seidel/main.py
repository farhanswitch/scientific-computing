# Buat daftar fungsi persamaan untuk mendapatkan nilai dari setiap variabel secara berurutan. Pastikan matriks koefisien variabelnya merupakan matriks diagonal dominan; Jika tidak, maka setiap variabel nilainya akan menyebar (diverging) pada setiap iterasi.
listEquation = [
    {
        'fn': lambda data: (
            (lambda res: 
            #cetak perhitungan yang diproses
            print(f"1/7 * (6 - {data['x2']} - {data['x3']}) = {res}") or res)(
                # proses perhitungan
                (6 - data['x2'] - data['x3']) / 7
            )
        )
    },
    {
        'fn': lambda data: (
            (lambda res: 
            #cetak perhitungan yang diproses
            print(f"1/7 * (-26 + (3 * {data['x1']}) + {data['x3']}) = {res}") or res)(
                # proses perhitungan
                (-26 + (3 * data['x1']) + data['x3']) / 7
            )
        )
    },
    {
        'fn': lambda data: (
            (lambda res: 
            #cetak perhitungan yang diproses
            print(f"1/9  * (1 + (2 * {data['x1']}) + (-5 * {data['x2']})) = {res}") or res)(
                # proses perhitungan
                (1 + (2 * data['x1']) + (-5 * data['x2'])) / 9
            )
        )
    }
]

# Menyimpan nilai dari setiap variabel
data = {
    'x1': 0,
    'x2': 0,
    'x3': 0
}

# Jumlah iterasi Gauss-Seidel yang akan dilakukan
iteration = 5

# Proses persamaan dengan Gauss-Seidel
for i in range(iteration):
    print(f"Iteration no. {i+1}")
    for j in range(1, len(listEquation) + 1):
        data[f'x{j}'] = listEquation[j-1]['fn'](data)

# Membulatkan data
for key in data:
    data[key] = round(data[key])

# Menampilkan hasil
print(data)
