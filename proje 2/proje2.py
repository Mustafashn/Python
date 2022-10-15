def taslari_olustur(dikey_sutunlar, yatay_sutunlar, sozluk):
    for sayi in yatay_sutunlar:
        for harf in dikey_sutunlar:
            sozluk[sayi + harf] = " "


def dikey_sutun_ciz(dikey_sutunlar, dikey):
    for i in dikey_sutunlar[:dikey]:
        print(f"  {i:3}", end="")
    print()


def harf_buyut(konum):
    konum_bas = konum[0]
    konum_son = konum[1]
    konum_son = konum_son.upper()
    konum = konum_bas + konum_son
    return konum


def liste_duzenle(yatay_sutunlar, dikey_sutunlar, sozluk, cizgiler):
    liste = []
    for i in yatay_sutunlar:
        liste.append(" ")
        liste[int(i) - 1] += yatay_sutunlar[int(i) - 1]
        for x in dikey_sutunlar:
            if x != dikey_sutunlar[-1]:
                ekle = " {}{}".format(sozluk.get(i + x), cizgiler)
            else:  # satırın sonuna satır numarasını eklemek
                ekle = "{}  {}".format(sozluk.get(i + x), int(i))
            liste[int(i) - 1] += ekle
    return liste


def yatay_sutun_ciz(liste, yatay, yatay_sutunlar):
    CIZIK = "|"
    for i in range(yatay):
        print(liste[i])
        if i + 1 != int(yatay_sutunlar[-1]):
            print(f"  {CIZIK:3}" * (yatay + 1))


def tablo_ciz(dikey_sutunlar, liste, yatay, yatay_sutunlar):
    dikey_sutun_ciz(dikey_sutunlar, yatay + 1)
    yatay_sutun_ciz(liste, yatay, yatay_sutunlar)
    dikey_sutun_ciz(dikey_sutunlar, yatay + 1)


def siyah_tas_oyna(sozluk, yatay_sutunlar, dikey_sutunlar, cizgiler, yatay):
    hata = True
    while hata:
        try:
            yer = input("Siyah taşın oynanacağı yeri giriniz: ")
            while len(yer) >= 3:
                yer = input("Siyah taşın oynanacağı yeri giriniz: ")
            yer = harf_buyut(yer)
            while sozluk[yer] == "S" or sozluk[yer] == "B":
                yer = input("Siyah taşın oynanacağı yeri giriniz: ")
                yer = harf_buyut(yer)
            hata = False
        except (KeyError, IndexError):
            continue
    sozluk[yer] = "S"
    print("\n")
    liste = liste_duzenle(yatay_sutunlar, dikey_sutunlar, sozluk, cizgiler)
    tablo_ciz(dikey_sutunlar, liste, yatay, yatay_sutunlar)


def beyaz_tas_oyna(sozluk, yatay_sutunlar, dikey_sutunlar, cizgiler, yatay):
    hata = True
    while hata:
        try:
            yer = input("Beyaz taşın oynanacağı yeri giriniz: ")
            while len(yer) >= 3:
                yer = input("Beyaz taşın oynanacağı yeri giriniz: ")
            yer = harf_buyut(yer)
            while sozluk[yer] == "S" or sozluk[yer] == "B":
                yer = input("Beyaz taşın oynanacağı yeri giriniz: ")
                yer = harf_buyut(yer)
            hata = False
        except (KeyError, IndexError):
            continue
    sozluk[yer] = "B"
    print("\n")
    liste = liste_duzenle(yatay_sutunlar, dikey_sutunlar, sozluk, cizgiler)
    tablo_ciz(dikey_sutunlar, liste, yatay, yatay_sutunlar)


def sayi_al():
    sayi = -1  # döngüye başlamak için
    alt_sinir = 3
    ust_sinir = 7
    hata = True
    while sayi < alt_sinir or sayi > ust_sinir or hata:
        try:
            sayi = int(input("Lütfen 3-7 arasında yatay çizgi sayısını giriniz: "))
            hata = False
        except ValueError:
            hata = True

    return sayi


def kare_sayisi_hesapla(sozluk, dikey_sutun, siyah_kare_liste, beyaz_kare_liste):
    liste = []
    siyah = []
    beyaz = []
    siyah_kare_sayisi = 0
    beyaz_kare_sayisi = 0
    sayac = 0
    for k, v in sozluk.items():  # sozluk parçalanıp iki boyutlu listeye atanıyor
        liste.append([k])
        liste[sayac].append(v)
        sayac += 1
    for i in range(len(liste)):  # siyah listesi oluşturuluyor
        if liste[i][1] == "S":
            siyah.append(liste[i][0])
        elif liste[i][1] == "B":  # beyaz listesi oluşturuluyor
            beyaz.append(liste[i][0])
    for i in siyah:  # siyahların kare oluşturma kontrolü yapılıyor
        index = dikey_sutun.index(i[1])
        degisken1 = str(int(i[0]) + 1)
        if degisken1 + i[1] in siyah:
            if len(dikey_sutun) > index + 1:
                if i[0] + dikey_sutun[index + 1] in siyah and degisken1 + dikey_sutun[index + 1] in siyah:
                    degisken_liste = []
                    degisken_liste.append(i)
                    degisken_liste.append(degisken1 + i[1])
                    degisken_liste.append(i[0] + dikey_sutun[index + 1])
                    degisken_liste.append(degisken1 + dikey_sutun[index + 1])
                    if degisken_liste not in siyah_kare_liste:
                        siyah_kare_liste.append(degisken_liste)
                        siyah_kare_sayisi += 1

    for i in beyaz:  # beyazların kare oluşturma kontrolü yapılıyor
        index = dikey_sutun.index(i[1])
        degisken1 = str(int(i[0]) + 1)
        if degisken1 + i[1] in beyaz:
            if len(dikey_sutun) > index + 1:
                if i[0] + dikey_sutun[index + 1] in beyaz and degisken1 + dikey_sutun[index + 1] in beyaz:
                    degisken_liste = []
                    degisken_liste.append(i)
                    degisken_liste.append(degisken1 + i[1])
                    degisken_liste.append(i[0] + dikey_sutun[index + 1])
                    degisken_liste.append(degisken1 + dikey_sutun[index + 1])
                    if degisken_liste not in beyaz_kare_liste:
                        beyaz_kare_liste.append(degisken_liste)
                        beyaz_kare_sayisi += 1
    return siyah_kare_sayisi, siyah_kare_liste, siyah, beyaz_kare_sayisi, beyaz_kare_liste, beyaz


def siyah_tas_cikar(sozluk, cik_tas_sayisi, yatay_sutunlar, dikey_sutunlar, cizgiler, yatay, siyah_kare_liste,
                    siyah_liste, siyah_tas_sayisi):
    tekli_liste = []
    for siyah_kare_kumesi in siyah_kare_liste:  # 2 boyutlu listeden tek boyutlu listeye geçilip işlem yapılıyor
        for i in siyah_kare_kumesi:
            tekli_liste.append(i)
    for i in range(cik_tas_sayisi):
        hata = True
        print("Kare oluşturuldu.Siyah taş çıkartılacaktır.")
        while hata:
            try:
                yer = input("Siyah taşın çıkartılacağı yeri giriniz: ")
                yer = harf_buyut(yer)
                while sozluk[yer] == " " or sozluk[yer] == "B" or yer in tekli_liste:
                    yer = input("Siyah taşın çıkartılacağı yeri giriniz: ")
                    yer = harf_buyut(yer)
                hata = False
            except (KeyError, IndexError):
                continue
        sozluk[yer] = " "
        siyah_liste.remove(yer)
        print("\n")
        liste = liste_duzenle(yatay_sutunlar, dikey_sutunlar, sozluk, cizgiler)
        tablo_ciz(dikey_sutunlar, liste, yatay, yatay_sutunlar)
    siyah_tas_sayisi -= cik_tas_sayisi  # siyah taş sayisi hesaplanıyor
    return siyah_tas_sayisi


def beyaz_tas_cikar(sozluk, cik_tas_sayisi, yatay_sutunlar, dikey_sutunlar, cizgiler, yatay, beyaz_kare_liste,
                    beyaz_liste, beyaz_tas_sayisi):
    tekli_liste = []  # 2 boyutlu listeden tek boyutlu listeye geçilip işlem yapılıyor
    for beyaz_kare_kumesi in beyaz_kare_liste:
        for i in beyaz_kare_kumesi:
            tekli_liste.append(i)
    for i in range(cik_tas_sayisi):
        print("Kare oluşturuldu.Beyaz taş çıkartılacaktır.")
        hata = True
        while hata:
            try:
                yer = input("Beyaz taşın çıkartılacağı yeri giriniz: ")
                yer = harf_buyut(yer)
                while sozluk[yer] == " " or sozluk[yer] == "S" or yer in tekli_liste:
                    yer = input("Beyaz taşın çıkartılacağı yeri giriniz: ")
                    yer = harf_buyut(yer)
                hata = False
            except (KeyError, IndexError):
                continue
        sozluk[yer] = " "
        beyaz_liste.remove(yer)
        print("\n")
        liste = liste_duzenle(yatay_sutunlar, dikey_sutunlar, sozluk, cizgiler)
        tablo_ciz(dikey_sutunlar, liste, yatay, yatay_sutunlar)
    beyaz_tas_sayisi -= cik_tas_sayisi  # beyaz taş sayisi hesaplanıyor
    return beyaz_tas_sayisi


def beyaz_tas_hareket_ettir(sozluk, yatay_sutunlar, dikey_sutunlar, cizgiler, yatay, beyaz_kare_liste):
    tekli_liste = []
    for beyaz_kare_kumesi in beyaz_kare_liste:  # 2 boyutlu listeden tek boyutlu listeye geçilip işlem yapılıyor
        for i in beyaz_kare_kumesi:
            tekli_liste.append(i)
    konumlar = input("Beyaz taşın ilk konumunu ve son konumunu giriniz: ")
    while len(konumlar) != 5 or konumlar[2] != " ":
        konumlar = input("Beyaz taşın ilk konumunu ve son konumunu giriniz: ")
    hata = True
    while hata:
        try:
            son_yer = konumlar[3:]
            son_yer = harf_buyut(son_yer)
            ilk_yer = konumlar[:2]
            ilk_yer = harf_buyut(ilk_yer)
            while sozluk[son_yer] == "S" or sozluk[son_yer] == "B" or sozluk[ilk_yer] == "S" or sozluk[ilk_yer] == " ":
                konumlar = input("Beyaz taşın ilk konumunu ve son konumunu giriniz: ")
                son_yer = konumlar[3:]
                son_yer = harf_buyut(son_yer)
                ilk_yer = konumlar[:2]
                ilk_yer = harf_buyut(ilk_yer)
            degisken_liste = []
            sayac = 0
            if son_yer[0] > ilk_yer[0]:  # örneğin 1. 2. tarzında mı diye kontrol ediliyor
                if son_yer[1] != ilk_yer[1]:  # örneğin 1A 2A tarzında değil mi diye kontrol ediliyor
                    sayac = 1
                else:
                    for i in sozluk:
                        if i[1] == son_yer[1] and i[0] < son_yer[0] and i[0] > ilk_yer[0]:  # sozlukte aranıyor
                            if i != ilk_yer:
                                degisken_liste.append(i)  # kullanılmak için listeye atanıyor
                    for i in degisken_liste:
                        if sozluk[i] == "S" or sozluk[
                            i] == "B":  # yer doluysa sayac artıyor ve karşılaştırma bitiyor
                            sayac += 1
            elif son_yer[0] == ilk_yer[0]:  # örneğin 2. 2. tarzında mı diye kontrol ediliyor
                for i in sozluk:
                    if ilk_yer[1] > son_yer[1]:  # örneğin 2D 2A tarzında mı diye kontrol ediliyor
                        if i[0] == son_yer[0] and i[1] < son_yer[1] and i[0] > ilk_yer[0]:  # sozlukte aranıyor
                            if i != ilk_yer:
                                degisken_liste.append(i)  # kullanılmak için listeye atanıyor
                    else:
                        if i[0] == son_yer[0] and i[1] < son_yer[1] and i[1] > ilk_yer[1]:
                            if i != ilk_yer:
                                degisken_liste.append(i)  # kullanılmak için listeye atanıyor
                for i in degisken_liste:
                    if sozluk[i] == "S" or sozluk[i] == "B":  # yer doluysa sayac artıyor ve karşılaştırma bitiyor
                        sayac += 1
            else:  # örneğin 1. 2. tarzında mı diye kontrol ediliyor
                for i in sozluk:
                    if i[1] == son_yer[1] and i[0] < ilk_yer[0] and i[0] > son_yer[0]:  # sozlukte aranıyor
                        if i != ilk_yer:  # kullanılmak için listeye atanıyor
                            degisken_liste.append(i)
                for i in degisken_liste:
                    if sozluk[i] == "S" or sozluk[i] == "B":  # yer doluysa sayac artıyor ve karşılaştırma bitiyor
                        sayac += 1
            if sayac == 0:  # sayacta islem yapılmadıysa yer değiştirme gerçekleşiyor
                sozluk[son_yer] = "B"
                sozluk[ilk_yer] = " "
                for beyaz_kare_kumesi in beyaz_kare_liste:  # kare olan bir alanda değişim yapıldıysa
                    for i in beyaz_kare_kumesi:  # kare listesinden yerler çıkartılıyor
                        if i == ilk_yer:
                            for x in i:
                                try:
                                    tekli_liste.remove(x)
                                except ValueError:
                                    break
                            beyaz_kare_liste.remove(beyaz_kare_kumesi)
                hata = False
            else:
                konumlar = input("Beyaz taşın ilk konumunu ve son konumunu giriniz: ")
                continue
        except (KeyError, IndexError):
            konumlar = input("Beyaz taşın ilk konumunu ve son konumunu giriniz: ")
            continue
    if ilk_yer != " ":
        sozluk[son_yer] = "B"
        sozluk[ilk_yer] = " "
        for beyaz_kare_kumesi in beyaz_kare_liste:  # kare olan bir alanda değişim yapıldıysa
            for i in beyaz_kare_kumesi:  # kare listesinden yerler çıkartılıyor
                if i == ilk_yer:
                    for x in i:
                        try:
                            tekli_liste.remove(x)
                        except ValueError:
                            break
                    beyaz_kare_liste.remove(beyaz_kare_kumesi)
    print("\n")
    liste = liste_duzenle(yatay_sutunlar, dikey_sutunlar, sozluk, cizgiler)
    tablo_ciz(dikey_sutunlar, liste, yatay, yatay_sutunlar)


def siyah_tas_hareket_ettir(sozluk, yatay_sutunlar, dikey_sutunlar, cizgiler, yatay, siyah_kare_liste):
    tekli_liste = []
    for siyah_kare_kumesi in siyah_kare_liste:  # 2 boyutlu listeden tek boyutlu listeye geçilip işlem yapılıyor
        for i in siyah_kare_kumesi:
            tekli_liste.append(i)
    konumlar = input("Siyah taşın ilk konumunu ve son konumunu giriniz: ")
    while len(konumlar) != 5 or konumlar[2] != " ":
        konumlar = input("Siyah taşın ilk konumunu ve son konumunu giriniz: ")
    hata = True
    while hata:
        try:
            son_yer = konumlar[3:]
            son_yer = harf_buyut(son_yer)
            ilk_yer = konumlar[:2]
            ilk_yer = harf_buyut(ilk_yer)
            while sozluk[son_yer] == "S" or sozluk[son_yer] == "B" or sozluk[ilk_yer] == "B" or sozluk[ilk_yer] == " ":
                konumlar = input("Siyah taşın ilk konumunu ve son konumunu giriniz: ")
                son_yer = konumlar[3:]
                son_yer = harf_buyut(son_yer)
                ilk_yer = konumlar[:2]
                ilk_yer = harf_buyut(ilk_yer)
            degisken_liste = []
            sayac = 0
            if son_yer[0] > ilk_yer[0]:  # örneğin 1. 2. tarzında mı diye kontrol ediliyor
                if son_yer[1] != ilk_yer[1]:  # örneğin 1A 2A tarzında değil mi diye kontrol ediliyor
                    sayac = 1
                else:
                    for i in sozluk:
                        if i[1] == son_yer[1] and i[0] < son_yer[0] and i[0] > ilk_yer[0]:  # sozlukte aranıyor
                            if i != ilk_yer:
                                degisken_liste.append(i)  # kullanılmak için listeye atanıyor
                    for i in degisken_liste:
                        if sozluk[i] == "S" or sozluk[
                            i] == "B":  # yer doluysa sayac artıyor ve karşılaştırma bitiyor
                            sayac += 1
            elif son_yer[0] == ilk_yer[0]:  # örneğin 2. 2. tarzında mı diye kontrol ediliyor
                for i in sozluk:
                    if ilk_yer[1] > son_yer[1]:  # örneğin 2D 2A tarzında mı diye kontrol ediliyor
                        if i[0] == son_yer[0] and i[1] < son_yer[1] and i[0] > ilk_yer[0]:  # sozlukte aranıyor
                            if i != ilk_yer:
                                degisken_liste.append(i)  # kullanılmak için listeye atanıyor
                    else:
                        if i[0] == son_yer[0] and i[1] < son_yer[1] and i[1] > ilk_yer[1]:
                            if i != ilk_yer:
                                degisken_liste.append(i)  # kullanılmak için listeye atanıyor
                for i in degisken_liste:
                    if sozluk[i] == "S" or sozluk[i] == "B":  # yer doluysa sayac artıyor ve karşılaştırma bitiyor
                        sayac += 1
            else:  # örneğin 1. 2. tarzında mı diye kontrol ediliyor
                for i in sozluk:
                    if i[1] == son_yer[1] and i[0] < ilk_yer[0] and i[0] > son_yer[0]:  # sozlukte aranıyor
                        if i != ilk_yer:  # kullanılmak için listeye atanıyor
                            degisken_liste.append(i)
                for i in degisken_liste:
                    if sozluk[i] == "S" or sozluk[i] == "B":  # yer doluysa sayac artıyor ve karşılaştırma bitiyor
                        sayac += 1
            if sayac == 0:  # sayacta islem yapılmadıysa yer değiştirme gerçekleşiyor
                sozluk[son_yer] = "B"
                sozluk[ilk_yer] = " "
                for siyah_kare_kumesi in siyah_kare_liste:  # kare olan bir alanda değişim yapıldıysa
                    for i in siyah_kare_kumesi:  # kare listesinden yerler çıkartılıyor
                        if i == ilk_yer:
                            for x in i:
                                try:
                                    tekli_liste.remove(x)
                                except ValueError:
                                    break
                            siyah_kare_liste.remove(siyah_kare_kumesi)
                hata = False
            else:
                konumlar = input("Siyah taşın ilk konumunu ve son konumunu giriniz: ")
                continue
        except (KeyError, IndexError):
            konumlar = input("Siyah taşın ilk konumunu ve son konumunu giriniz: ")
            continue
    if ilk_yer != " ":
        sozluk[son_yer] = "S"
        sozluk[ilk_yer] = " "
        for siyah_kare_kumesi in siyah_kare_liste:  # kare olan bir alanda değişim yapıldıysa
            for i in siyah_kare_kumesi:  # kare listesinden yerler çıkartılıyor
                if i == ilk_yer:
                    for x in i:
                        try:
                            tekli_liste.remove(x)
                        except ValueError:
                            break
                    siyah_kare_liste.remove(siyah_kare_kumesi)

    print("\n")
    liste = liste_duzenle(yatay_sutunlar, dikey_sutunlar, sozluk, cizgiler)
    tablo_ciz(dikey_sutunlar, liste, yatay, yatay_sutunlar)


def main():
    OYUN_BASI_KONTROL = -1  # oyun başında kimse kare oluşturamadıysa beyazın başlaması için
    yatay = sayi_al()
    dikey = yatay + 1
    DIKEY_SUTUNLAR = ["A", "B", "C", "D", "E", "F", "G", "H"]
    DIKEY_SUTUNLAR = DIKEY_SUTUNLAR[:dikey]
    YATAY_SUTUNLAR = ["1", "2", "3", "4", "5", "6", "7"]
    YATAY_SUTUNLAR = YATAY_SUTUNLAR[:yatay]
    CIZGILER = "---"
    taslar = {}
    siyah_kare_liste = [[]]
    beyaz_kare_liste = [[]]
    tas_sayisi = dikey * yatay
    beyaz_tas_sayisi = tas_sayisi // 2
    siyah_tas_sayisi = tas_sayisi // 2

    taslari_olustur(DIKEY_SUTUNLAR, YATAY_SUTUNLAR, taslar)
    print("\n")
    liste = liste_duzenle(YATAY_SUTUNLAR, DIKEY_SUTUNLAR, taslar, CIZGILER)
    tablo_ciz(DIKEY_SUTUNLAR, liste, yatay, YATAY_SUTUNLAR)
    for i in range(beyaz_tas_sayisi):
        beyaz_tas_oyna(taslar, YATAY_SUTUNLAR, DIKEY_SUTUNLAR, CIZGILER, yatay)
        siyah_tas_oyna(taslar, YATAY_SUTUNLAR, DIKEY_SUTUNLAR, CIZGILER, yatay)

    while beyaz_tas_sayisi != 3 and siyah_tas_sayisi != 3:
        beyaz_cik, siyah_kare_liste, siyah_liste, siyah_cik, beyaz_kare_liste, beyaz_liste = kare_sayisi_hesapla(taslar,
                                                                                                                 DIKEY_SUTUNLAR,
                                                                                                                 siyah_kare_liste,
                                                                                                                 beyaz_kare_liste)
        if siyah_cik == 0 and beyaz_cik == 0 and OYUN_BASI_KONTROL == -1:  # oyun başı beyaz başlıyor
            print("Beyaz kare oluşturmuş gibi beyaz başlayacaktır.")
            siyah_tas_sayisi = siyah_tas_cikar(taslar, 1, YATAY_SUTUNLAR, DIKEY_SUTUNLAR, CIZGILER, yatay,
                                               siyah_kare_liste, siyah_liste, siyah_tas_sayisi)
        OYUN_BASI_KONTROL = 1
        if siyah_cik != 0 and OYUN_BASI_KONTROL == 1:  # siyah taş çıkartma gerçekleşiyor
            siyah_tas_sayisi = siyah_tas_cikar(taslar, 1, YATAY_SUTUNLAR, DIKEY_SUTUNLAR, CIZGILER, yatay,
                                               siyah_kare_liste, siyah_liste, siyah_tas_sayisi)
        if beyaz_cik != 0 and OYUN_BASI_KONTROL == 1:  # beyaz taş çıkartma gerçekleşiyor
            beyaz_tas_sayisi = beyaz_tas_cikar(taslar, 1, YATAY_SUTUNLAR, DIKEY_SUTUNLAR, CIZGILER, yatay,
                                               beyaz_kare_liste, beyaz_liste, beyaz_tas_sayisi)
        beyaz_tas_hareket_ettir(taslar, YATAY_SUTUNLAR, DIKEY_SUTUNLAR, CIZGILER, yatay, beyaz_kare_liste)
        beyaz_cik, siyah_kare_liste, siyah_liste, siyah_cik, beyaz_kare_liste, beyaz_liste = kare_sayisi_hesapla(taslar,
                                                                                                                 DIKEY_SUTUNLAR,
                                                                                                                 siyah_kare_liste,
                                                                                                                 beyaz_kare_liste)
        if siyah_cik != 0 and OYUN_BASI_KONTROL == 1:  # siyah taş çıkartma gerçekleşiyor
            siyah_tas_sayisi = siyah_tas_cikar(taslar, 1, YATAY_SUTUNLAR, DIKEY_SUTUNLAR, CIZGILER, yatay,
                                               siyah_kare_liste, siyah_liste, siyah_tas_sayisi)
        if siyah_tas_sayisi <= 3 or beyaz_tas_sayisi <= 3:  # oyun bitti mi kontrolü yapılıyor
            break
        siyah_tas_hareket_ettir(taslar, YATAY_SUTUNLAR, DIKEY_SUTUNLAR, CIZGILER, yatay, siyah_kare_liste)
    if siyah_tas_sayisi <= 3:
        print("Beyaz oyuncu oyunu kazandı.")
    else:  # beyaz taş sayısı 4'ten küçük ise
        print("Siyah oyuncu oyunu kazandı.")


main()
