# Data list
listData = [
    {
        'x': 0,
        'y': [14.6210]
    },
    {
        'x': 8,
        'y': [11.8430]
    },
    {
        'x': 16,
        'y': [9.8700]
    },
    {
        'x': 24,
        'y': [8.4180]
    },
    {
        'x': 32,
        'y': [7.3050]
    },
    {
        'x': 40,
        'y': [6.4130]
    },
]

def formatNumber(num, precision):
    return round(num, precision)
# Fungsi untuk menghitung nilai
def calculateValue(index, current, base):
    if base is None:
        return None
    return (current['y'][index] - base['y'][index]) / (current['x'] - base['x'])

# Proses perhitungan untuk setiap data di list
for i in range(len(listData)):
    current = listData[i]
    if i >= len(current['y']) - 1:
        for j in range(i):
            base = listData[j] if i > 0 else None
            res = calculateValue(j, listData[i], base)
            if res is not None:
                listData[i]['y'].append(formatNumber(res,4))

# Mengatur padding untuk format output
padding = 5
for x in range(len(listData)):
    current = listData[x]
    padding = max(padding, len(str(current['x'])))
    for y in range(len(current['y'])):
        padding = max(padding, len(str(current['y'][y])))

padding += 1

# Mencetak header
strHeader = "No".rjust(padding, " ")
strHeader += "x".rjust(padding, " ")
strHeader += "y".rjust(padding, " ")
for x in range(1, len(listData)):
    strHeader += f"∇{x}y".rjust(padding, " ")
print(strHeader)

# Mencetak baris data
for x in range(len(listData)):
    current = listData[x]
    strLine = str(x).rjust(padding, " ")
    strLine += str(current['x']).rjust(padding, " ")
    for y in range(len(listData)):
        value = current['y'][y] if y < len(current['y']) else ""
        # Hilangkan tanda minus jika nilainya 0
        if value == 0:
            value = abs(value)
        strLine += str(value).rjust(padding, " ")
    print(strLine)
