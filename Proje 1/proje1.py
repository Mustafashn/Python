TON_BASI_UCRET = 2.5
SAAT_0_1_UCRET = 3
SAAT_1_3_UCRET = 5
SAAT_3_5_UCRET = 7
SAAT_5_10_UCRET = 10
SAAT_10_24_UCRET = 14
SAAT_24_UCRET = 15

KOD_1_KATSAYI = 1  # Motosiklet
KOD_2_KATSAYI = 2  # Binek
KOD_3_KATSAYI = 3  # Minibüs
KOD_4_KATSAYI = 3  # Otobüs
KOD_5_KATSAYI = 4  # Kamyon
KOD_6_KATSAYI = 4  # Tır

KOD_1_2_GAZI_INDIRIM = 100  # Motosiklet ve binek araçların sürücüsünün gazi olması durumunda uygulanacak indirim oranı
KOD_1_2_ENG_INDIRIM = 50  # Motosiklet ve binek araçların sürücüsünün engelli olması durumunda uygulanacak indirim oranı

arac_sayisi = 0
kod_1_arac_sayisi = 0
kod_2_arac_sayisi = 0
kod_3_arac_sayisi = 0
kod_4_arac_sayisi = 0
kod_5_arac_sayisi = 0
kod_6_arac_sayisi = 0

kod_1_arac_geliri = 0
kod_2_arac_geliri = 0
kod_3_arac_geliri = 0
kod_4_arac_geliri = 0
kod_5_arac_geliri = 0
kod_6_arac_geliri = 0

kod_1_arac_suresi = 0
kod_2_arac_suresi = 0
kod_3_arac_suresi = 0
kod_4_arac_suresi = 0
kod_5_arac_suresi = 0
kod_6_arac_suresi = 0

agirlik_1_ton_alti_binek_say = 0
agirlik_10_ton_fazla_otobus_kamyon_tir_say = 0
agirlik_10_ton_fazla_kamyon_say = 0
agirlik_10_ton_fazla_tir_say = 0

otopark_30_az_binek_motor_say = 0
otopark_1_gun_fazla_mini_oto_say = 0
otopark_30_gun_fazla_veya_1000_tl_uzeri_ucret_say = 0
otopark_3_saat_fazla_indirimli_arac_say = 0
en_uzun_sure_kalan_arac_suresi = 0
en_uzun_sure_kalan_arac_geliri = 0
en_cok_gelir_elde_edilen_binek_arac_suresi = 0
en_cok_gelir_elde_edilen_binek_arac_geliri = -1

surucusu_gazi_olan_arac_say = 0
surucusu_gazi_olan_arac_top_sure = 0
surucusu_eng_olan_arac_say = 0
surucusu_eng_olan_arac_top_sure = 0

baska_arac_var_mi = "e"
otopark_top_gelir = 0

while baska_arac_var_mi in ["E", "e"]:
    indirim_carpani = 1
    ozel_durum = ""
    arac_sayisi += 1
    arac_plakasi = input("Lütfen araç plakasını giriniz: ")
    arac_kod = int(input("Lütfen araç sınıf kodunu giriniz (1-6) : "))
    while arac_kod < 1 or arac_kod > 6:  # Araç kodu geçersiz veri kontrolü
        arac_kod = int(input("Lütfen araç sınıf kodunu giriniz (1-6) : "))

    arac_agirlik = float(input("Lütfen aracın ağırlığını giriniz (kg): "))
    while arac_agirlik <= 0:  # Araç ağırlığı geçersiz veri kontrolü
        arac_agirlik = float(input("Lütfen aracın ağırlığını giriniz (kg): "))
    arac_agirlik_ton = arac_agirlik/1000
    agirlik_ucret = arac_agirlik_ton*TON_BASI_UCRET

    arac_sure_dakika = int(input("Aracın kaç dakika otoparkta kaldığını giriniz: "))
    while arac_sure_dakika <= 0:  # Araç otoparkta kalma süresi geçersiz veri kontrolü
        arac_sure_dakika = int(input("Aracın kaç dakika otoparkta kaldığını giriniz: "))
    ad_soyad = input("Sürücünün adını soyadını giriniz: ")
    arac_sure_saat = arac_sure_dakika/60
    arac_sure_gun = arac_sure_saat / 24

    saat_ucret = 0
    saat_devam = "e"
    arac_sure_saat_degisken = arac_sure_saat
    while saat_devam == "e":  # Saatlere göre ücretin hesaplanması
        saat_devam = "h"
        if arac_sure_saat_degisken < 1:
            saat_ucret += SAAT_0_1_UCRET
        elif arac_sure_saat_degisken < 3:
            saat_ucret += SAAT_1_3_UCRET
        elif arac_sure_saat_degisken < 5:
            saat_ucret += SAAT_3_5_UCRET
        elif arac_sure_saat_degisken < 10:
            saat_ucret += SAAT_5_10_UCRET
        elif arac_sure_saat_degisken < 24:
            saat_ucret += SAAT_10_24_UCRET
        else:  # Saat süresi 24 saat üzeri olanlar için
            saat_ucret += arac_sure_saat_degisken // 24 * SAAT_24_UCRET
            arac_sure_saat_degisken = arac_sure_saat_degisken % 24
            if arac_sure_saat_degisken != 0:  # Artan değerler için döngüye dönüşün olacağını belirtir.
                saat_devam = "e"

    if arac_kod == 1 or arac_kod == 2:
        ozel_durum = input("Lütfen sürücünün özel durumunu giriniz / Yok (Y,y) / Gazi (G,g) / Engelli (E,e): ")
        while ozel_durum not in ["Y", "y", "E", "e", "G", "g"]:  # Hatalı girdi girilirse tekrar girdi alınacaktır.
            ozel_durum = input("Lütfen sürücünün özel durumunu giriniz / Yok (Y,y) / Gazi (G,g) / Engelli (E,e): ")
        if ozel_durum == "G" or ozel_durum == "g":
            ozel_durum = "Gazi"
            indirim_carpani = 0  # %100 indirim için
            indirim_orani = KOD_1_2_GAZI_INDIRIM
            surucusu_gazi_olan_arac_say += 1
            surucusu_gazi_olan_arac_top_sure += arac_sure_dakika

        elif ozel_durum == "E" or ozel_durum == "e":
            ozel_durum = "Engelli"
            indirim_carpani = 1/2  # %50 indirim için
            indirim_orani = KOD_1_2_ENG_INDIRIM
            surucusu_eng_olan_arac_say += 1
            surucusu_eng_olan_arac_top_sure += arac_sure_dakika
        if arac_kod == 1:
            katsayi = KOD_1_KATSAYI
            arac_sinif_adi = "Motosiklet"
            kod_1_arac_sayisi += 1
            kod_1_arac_suresi += arac_sure_dakika
            if arac_sure_dakika <= 30:
                otopark_30_az_binek_motor_say += 1
        else:
            katsayi = KOD_2_KATSAYI
            arac_sinif_adi = "Binek"
            kod_2_arac_sayisi += 1
            kod_2_arac_suresi += arac_sure_dakika
            if arac_agirlik_ton < 1:
                agirlik_1_ton_alti_binek_say += 1
            if arac_sure_dakika <= 30:
                otopark_30_az_binek_motor_say += 1

    elif arac_kod == 3:
        katsayi = KOD_3_KATSAYI
        arac_sinif_adi = "Minibüs"
        kod_3_arac_sayisi += 1
        kod_3_arac_suresi += arac_sure_dakika
        if arac_sure_saat > 24:
            otopark_1_gun_fazla_mini_oto_say += 1
    elif arac_kod == 4:
        katsayi = KOD_4_KATSAYI
        arac_sinif_adi = "Otobüs"
        kod_4_arac_sayisi += 1
        kod_4_arac_suresi += arac_sure_dakika
        if arac_agirlik_ton > 10:
            agirlik_10_ton_fazla_otobus_kamyon_tir_say += 1
        if arac_sure_saat > 24:
            otopark_1_gun_fazla_mini_oto_say += 1
    elif arac_kod == 5:
        katsayi = KOD_5_KATSAYI
        arac_sinif_adi = "Kamyon"
        kod_5_arac_sayisi += 1
        kod_5_arac_suresi += arac_sure_dakika
        if arac_agirlik_ton > 10:
            agirlik_10_ton_fazla_otobus_kamyon_tir_say += 1
    else:
        katsayi = KOD_6_KATSAYI
        arac_sinif_adi = "Tır"
        kod_6_arac_sayisi += 1
        kod_6_arac_suresi += arac_sure_dakika
        if arac_agirlik_ton > 10:
            agirlik_10_ton_fazla_otobus_kamyon_tir_say += 1
    arac_top_ucret = ((saat_ucret*katsayi)+agirlik_ucret)*indirim_carpani
    otopark_top_gelir += arac_top_ucret

    if arac_kod == 1:
        kod_1_arac_geliri += arac_top_ucret
    elif arac_kod == 2:
        kod_2_arac_geliri += arac_top_ucret
        if arac_top_ucret > en_cok_gelir_elde_edilen_binek_arac_geliri:
            en_cok_gelir_elde_edilen_binek_arac_geliri = arac_top_ucret
            en_cok_gelir_elde_edilen_binek_arac_suresi = arac_sure_dakika
    elif arac_kod == 3:
        kod_3_arac_geliri += arac_top_ucret
    elif arac_kod == 4:
        kod_4_arac_geliri += arac_top_ucret
    elif arac_kod == 5:
        kod_5_arac_geliri += arac_top_ucret
    else:  # arac_kod=6 için
        kod_6_arac_geliri += arac_top_ucret

    if arac_sure_gun > 30 or arac_top_ucret > 1000:
        otopark_30_gun_fazla_veya_1000_tl_uzeri_ucret_say += 1

    if arac_sure_dakika > en_uzun_sure_kalan_arac_suresi:
        en_uzun_sure_kalan_arac_suresi = arac_sure_dakika
        en_uzun_sure_kalan_arac_geliri = arac_top_ucret

    print("Arabanın plakası : ", arac_plakasi)
    print("Arabanın sınıf adı : ", arac_sinif_adi)
    print("Arabanın ağırlığı (kg): ", round(arac_agirlik, 2))
    print("Otoparkta kaldığı süre: {} gün {} saat {} dakika "
          .format(arac_sure_saat//24, arac_sure_dakika//60 % 24, arac_sure_dakika % 60))
    print("Sürücünün adı soyadı : ", ad_soyad)

    if ozel_durum == "Gazi" or ozel_durum == "Engelli":
        print("Sürücünün özel durumu : ", ozel_durum)
        print("Uygulanan indirim oranı : %", indirim_orani)
        if arac_sure_saat > 3:
            otopark_3_saat_fazla_indirimli_arac_say += 1
    print("Sürücünün ödemesi gereken otopark ücreti = {} TL".format(round(arac_top_ucret, 2)))

    baska_arac_var_mi = input("Başka araç var mı (e/E/h/H): \n *************************************************")
    while baska_arac_var_mi not in ["e", "E", "H", "h"]:  # Hatali girdi girilirse tekrar girdi alınacaktır.
        baska_arac_var_mi = input("Başka araç var mı (e/E/h/H): \n *************************************************")

kod1_arac_ortalama_sure = kod_1_arac_suresi//kod_1_arac_sayisi
kod2_arac_ortalama_sure = kod_2_arac_suresi//kod_2_arac_sayisi
kod3_arac_ortalama_sure = kod_3_arac_suresi//kod_3_arac_sayisi
kod4_arac_ortalama_sure = kod_4_arac_suresi//kod_4_arac_sayisi
kod5_arac_ortalama_sure = kod_5_arac_suresi//kod_5_arac_sayisi
kod6_arac_ortalama_sure = kod_6_arac_suresi//kod_6_arac_sayisi
surucusu_gazi_olan_arac_ort_sure = surucusu_gazi_olan_arac_top_sure // surucusu_gazi_olan_arac_say
surucusu_eng_olan_arac_ort_sure = surucusu_eng_olan_arac_top_sure // surucusu_eng_olan_arac_say

print("Otoparkta kullanılan toplam araç sayısı :", arac_sayisi)
print("Motosiklet sınıfı araç için toplam araç sayısı : {} / Oranı : % {}"
      .format(kod_1_arac_sayisi, round(kod_1_arac_sayisi/arac_sayisi*100, 2)))
print("Binek sınıfı araç için toplam araç sayısı : {} / Oranı : % {}"
      .format(kod_2_arac_sayisi, round(kod_2_arac_sayisi/arac_sayisi*100, 2)))
print("Minibüs sınıfı araç için toplam araç sayısı : {} / Oranı : % {}"
      .format(kod_3_arac_sayisi, round(kod_3_arac_sayisi / arac_sayisi*100, 2)))
print("Otobüs sınıfı araç için toplam araç sayısı : {} / Oranı : % {}"
      .format(kod_4_arac_sayisi, round(kod_4_arac_sayisi/arac_sayisi*100, 2)))
print("Kamyon sınıfı araç için toplam araç sayısı : {} / Oranı : % {}"
      .format(kod_5_arac_sayisi, round(kod_5_arac_sayisi/arac_sayisi*100, 2)))
print("Tır sınıfı araç için toplam araç sayısı : {} / Oranı : % {} \n *************************************************"
      .format(kod_6_arac_sayisi, round(kod_6_arac_sayisi/arac_sayisi*100, 2)))

print("Otoparkın toplam geliri: {} TL".format(round(otopark_top_gelir, 2)))
print("Motosiklet sınıfı için toplam gelir: {} TL / Toplam gelir içindeki oranı : % {} "
      .format(round(kod_1_arac_geliri, 2), round(kod_1_arac_geliri/otopark_top_gelir*100, 2)))
print("Binek sınıfı için toplam gelir: {} TL / Toplam gelir içindeki oranı : % {} "
      .format(round(kod_2_arac_geliri, 2), round(kod_2_arac_geliri/otopark_top_gelir*100, 2)))
print("Minibüs sınıfı için toplam gelir: {} TL / Toplam gelir içindeki oranı : % {} "
      .format(round(kod_3_arac_geliri, 2), round(kod_3_arac_geliri/otopark_top_gelir*100, 2)))
print("Otobüs sınıfı için toplam gelir: {} TL / Toplam gelir içindeki oranı : % {} "
      .format(round(kod_4_arac_geliri, 2), round(kod_4_arac_geliri/otopark_top_gelir*100, 2)))
print("Kamyon sınıfı için toplam gelir: {} TL / Toplam gelir içindeki oranı : % {} "
      .format(round(kod_5_arac_geliri, 2), round(kod_5_arac_geliri/otopark_top_gelir*100, 2)))
print("Tır sınıfı için toplam gelir: {} TL / Toplam gelir içindeki oranı : % {} \n ************************************"
      .format(round(kod_6_arac_geliri, 2), round(kod_6_arac_geliri/otopark_top_gelir*100, 2)))

print("Motosiklet sınıfı için araç başına ortalama otoparkta kalma süresi : {} gün {} saat {} dakika / Araç başına ortalama gelir : {} TL"
      .format(kod1_arac_ortalama_sure//60//24, kod1_arac_ortalama_sure//60 % 24, kod1_arac_ortalama_sure % 60, round(kod_1_arac_geliri/kod_1_arac_sayisi, 2)))
print("Binek sınıfı için araç başına ortalama otoparkta kalma süresi : {} gün {} saat {} dakika / Araç başına ortalama gelir : {} TL"
      .format(kod2_arac_ortalama_sure//60//24, kod2_arac_ortalama_sure//60 % 24, kod2_arac_ortalama_sure % 60, round(kod_2_arac_geliri/kod_2_arac_sayisi, 2)))
print("Minibüs sınıfı için araç başına ortalama otoparkta kalma süresi : {} gün {} saat {} dakika / Araç başına ortalama gelir : {} TL"
      .format(kod3_arac_ortalama_sure//60//24, kod3_arac_ortalama_sure//60 % 24, kod3_arac_ortalama_sure % 60, round(kod_3_arac_geliri/kod_3_arac_sayisi, 2)))
print("Otobüs sınıfı için araç başına ortalama otoparkta kalma süresi : {} gün {} saat {} dakika / Araç başına ortalama gelir : {} TL"
      .format(kod4_arac_ortalama_sure//60//24, kod4_arac_ortalama_sure//60 % 24, kod4_arac_ortalama_sure % 60, round(kod_4_arac_geliri/kod_4_arac_sayisi, 2)))
print("Kamyon sınıfı için araç başına ortalama otoparkta kalma süresi : {} gün {} saat {} dakika / Araç başına ortalama gelir : {} TL"
      .format(kod5_arac_ortalama_sure//60//24, kod5_arac_ortalama_sure//60 % 24, kod5_arac_ortalama_sure % 60, round(kod_5_arac_geliri/kod_5_arac_sayisi, 2)))
print("Tır sınıfı için araç başına ortalama otoparkta kalma süresi : {} gün {} saat {} dakika / Araç başına ortalama gelir : {} TL "
      "\n *************************************************"
      .format(kod6_arac_ortalama_sure//60//24, kod6_arac_ortalama_sure//60 % 24, kod6_arac_ortalama_sure % 60, round(kod_6_arac_geliri/kod_6_arac_sayisi, 2)))

print("Ağırlığı 1 tondan az olan binek araçların, tüm binek araçlar içindeki oranı : % {} "
      .format(round(agirlik_1_ton_alti_binek_say/kod_2_arac_sayisi*100, 2)))
print("Ağırlığı 10 tondan fazla olan otobüs, kamyon ve tır sınıfı araçların, tüm otobüs, kamyon ve tır sınıfı araçlar içindeki oranı : % {} "
      "\n ************************************************* "
      .format(round(agirlik_10_ton_fazla_otobus_kamyon_tir_say/(kod_4_arac_sayisi+kod_5_arac_sayisi+kod_6_arac_sayisi)*100, 2)))

print("Otoparkta 30 dakika veya daha kısa süre kalan motosiklet ve binek tipi araçların, tüm motosiklet ve binek tipi araçlar içindeki oranı :  % {} "
      .format(round(otopark_30_az_binek_motor_say/(kod_1_arac_sayisi+kod_2_arac_sayisi)*100, 2)))

print("Otoparkta 1 günden daha uzun süre kalan minibüs ve otobüs tipi araçların, tüm minibüs ve otobüs tipi araçlar içindeki oranı : % {} "
      .format(round(otopark_1_gun_fazla_mini_oto_say/(kod_3_arac_sayisi+kod_4_arac_sayisi)*100, 2)))

print("Otoparkta 30 günden daha fazla kalan veya 1000 TL'den daha yüksek gelir elde edilen araçların tüm araçlar içindeki oranı :  % {} "
      "\n *************************************************"
      .format(round(otopark_30_gun_fazla_veya_1000_tl_uzeri_ucret_say/arac_sayisi*100, 2)))

print("Sürücüsü gazi olan araçların tüm araçlar içindeki oranı : %  {} / Sayısı : {} / Araç başına otoparkta kalma süresi {} gün {} saat {} dakika "
      .format(round(surucusu_gazi_olan_arac_say/arac_sayisi*100, 2), surucusu_gazi_olan_arac_say, surucusu_gazi_olan_arac_ort_sure//24//60, surucusu_gazi_olan_arac_ort_sure // 60 % 24, surucusu_gazi_olan_arac_ort_sure % 60))
print("Sürücüsü engelli olan araçların tüm araçlar içindeki oranı : %  {} / Sayısı : {} / Araç başına otoparkta kalma süresi {} gün {} saat {} dakika "
      .format(round(surucusu_eng_olan_arac_say/arac_sayisi*100, 2), surucusu_eng_olan_arac_say, surucusu_eng_olan_arac_ort_sure//24//60, surucusu_eng_olan_arac_ort_sure // 60 % 24, surucusu_eng_olan_arac_ort_sure % 60))
print("Otoparkta 3 saatten daha fazla kalan ve indirim uygulanan araçların tüm indirim uygulanan araçlar içindeki oranı : % {}"
      .format(round(otopark_3_saat_fazla_indirimli_arac_say/(surucusu_eng_olan_arac_say+surucusu_gazi_olan_arac_say) * 100, 2)))
print("En uzun süre kalan otoparkta kalan aracın otoparkta kalma süresi : {} gün {} saat {} dakika / Elde edilen gelir : {} TL"
      .format(en_uzun_sure_kalan_arac_suresi//24//60, en_uzun_sure_kalan_arac_suresi//60 % 24, en_uzun_sure_kalan_arac_suresi % 60, round(en_uzun_sure_kalan_arac_geliri, 2)))
print("En çok gelir elde edilen binek aracın otoparkta kalma süresi : {} gün {} saat {} dakika / Elde edilen gelir : {} TL "
      "\n *********************************************************"
      .format(en_cok_gelir_elde_edilen_binek_arac_suresi//24//60, en_cok_gelir_elde_edilen_binek_arac_suresi//60 % 24, en_cok_gelir_elde_edilen_binek_arac_suresi % 60, round(en_cok_gelir_elde_edilen_binek_arac_geliri, 2)))
