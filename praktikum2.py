# Mencetak Deret Fibonacci hingga
def fibonacci(n):
    a,b = 0, 1
    hasil = []
    while a <= n:
        hasil.append(a)
        a, b = b, a + b
    return hasil
#input nilai n dari pengguna
n = int(input ("masukan nilai n: "))

#memanggil fungsi fibonacci dab mencetak hasilnya
print(f"deret fibonacci sampai {n}: {fibonacci(n)}")