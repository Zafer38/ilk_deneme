


def ogrenci():

    ogAd = input("Adinizi Giriniz :")
    adUzunlugu=len(ogAd)



    ogSoyad = input("Soyadinizi Giriniz :")
    soyadUzunlugu=len(ogSoyad)


    uzunluk=adUzunlugu+soyadUzunlugu
    print(uzunluk)

    cumle = input("Cumle Giriniz :")
    


    kelime=0
    kelimesayisi=0

    for k in cumle:
        if k == " ":
            kelime +=1

    kelimesayisi +=1

    print(kelimesayisi)

    while kelimesayisi<uzunluk:

        print("Cumle uzunlugu yetersiz..")
        cumle = input("Cumle Giriniz :")

        for k in cumle:
            if k == " ":
                kelime +=1
        

    print(ogAd)
    print(ogSoyad)
    


ogrenci()