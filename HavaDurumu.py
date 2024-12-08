class Sehir:
    def __init__(self, ad, sicaklik):
        self.ad = ad
        self.sicaklik = sicaklik

class HavaDurumu:
    def __init__(self):
        self.sehirler = {}

    def sehir_ekle(self, ad, sicaklik):
        if ad in self.sehirler:
            print(f"{ad} zaten listede.")
        else:
            self.sehirler[ad] = Sehir(ad, sicaklik)
            print(f"{ad} başarıyla eklendi.")

    def sicaklik_guncelle(self, ad, sicaklik):
        if ad in self.sehirler:
            self.sehirler[ad].sicaklik = sicaklik
            print(f"{ad} şehrinin sıcaklığı güncellendi.")
        else:
            print(f"{ad} listede bulunamadı.")

    def hava_durumu_sorgula(self, ad):
        if ad in self.sehirler:
            sehir = self.sehirler[ad]
            print(f"{ad} için sıcaklık: {sehir.sicaklik}°C")
            print(f"Tavsiye: {self.tavsiye_ver(sehir.sicaklik)}")
        else:
            print(f"{ad} listede bulunamadı.")

    def tavsiye_ver(self, sicaklik):
        if sicaklik < 0:
            return "Soğuk, sıkı giyinin."
        elif 0 <= sicaklik <= 15:
            return "Serin, mont almayı unutmayın."
        else:
            return "Hava güzel, rahat giyin."

hava_durumu = HavaDurumu()

hava_durumu.sehir_ekle("İstanbul", 12)
hava_durumu.sehir_ekle("Ankara", -2)

hava_durumu.sicaklik_guncelle("İstanbul", 18)

hava_durumu.hava_durumu_sorgula("İstanbul")
hava_durumu.hava_durumu_sorgula("Ankara")
hava_durumu.hava_durumu_sorgula("İzmir")
