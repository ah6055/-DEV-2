sayi1 = float(input("Birinci sayiyi girin: "))
sayi2 = float(input("İkinci sayiyi girin : "))
toplama = sayi1 + sayi2
print("Toplama: ",toplama)

sayi1 = float(input("Birinci sayiyi girin: "))
sayi2 = float(input("İkinci sayiyi girin : "))
cıkarma = sayi1 - sayi2
print("Cıkarma: ",cıkarma)

sayi1 = float(input("Birinci sayiyi girin: "))
sayi2 = float(input("İkinci sayiyi girin : "))
Carpma = sayi1 * sayi2
print("Carpma: ",Carpma)

sayi1 = float(input("Birinci sayiyi girin: "))
sayi2 = float(input("İkinci sayiyi girin : "))
Bolme = sayi1 / sayi2
print("Bolme: ",Bolme)

sayi1 = float(input("Birinci sayiyi girin: "))
sayi2 = float(input("İkinci sayiyi girin : "))
Ustalma = sayi1 ** sayi2
print("Ustalma: ",Ustalma)

sayi1 = 10
sayi2 = 2

print("Toplam: ", sayi1 + sayi2)
print("Cikarma: ", sayi1 - sayi2)
print("Tam Bolme: ", sayi1 / sayi2)
print("Carpma: ", sayi1 * sayi2)
print("Ust Alma: ", sayi1 ** sayi2)

n = int(input("Bir sayi girin: "))
toplam = 0
for i in range(1, n + 1):
    toplam += i
print(f"1'den {n}'ye kadar olan sayilarin toplami: {toplam}")

for sayi in range(2, 101, 2):
    print(sayi)


metin = input("Bir metin girin: ")
ters_metin = ""
for i in range(len(metin) - 1, -1, -1):
    ters_metin += metin[i]
print("Ters çevrilmiş metin:", ters_metin)
