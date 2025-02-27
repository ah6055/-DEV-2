def find_min_max():
    # Boş bir liste oluşturuyoruz
    numbers = []
    
    # Kullanıcıdan 5 adet tam sayı alıyoruz
    for i in range(5):
        number = int(input(f"Lütfen {i+1}. tam sayıyı girin: "))
        numbers.append(number)
    
    # En büyük ve en küçük sayıyı buluyoruz
    max_number = max(numbers)
    min_number = min(numbers)
    
    # Sonuçları ekrana yazdırıyoruz
    print(f"Listede yer alan sayılar: {numbers}")
    print(f"En büyük sayı: {max_number}")
    print(f"En küçük sayı: {min_number}")

# Fonksiyonu çağırıyoruz
find_min_max()
