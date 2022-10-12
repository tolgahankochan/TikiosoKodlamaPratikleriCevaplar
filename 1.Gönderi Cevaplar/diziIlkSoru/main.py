sayilar = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sayilar2 = [21, 22, 23, 24, 25]
birlestir = sayilar + sayilar2

#tikioso

for sayi in birlestir:
    if sayi % 4 == 0:
        print(sayi)