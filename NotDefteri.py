class Not:
    def __init__(self, icerik, tarih):
        self.icerik = icerik
        self.tarih = tarih

class NotDefteri:
    def __init__(self):
        self.notlar = []

    def not_ekle(self, icerik, tarih):
        yeni_not = Not(icerik, tarih)
        self.notlar.append(yeni_not)
        print("Not başarıyla eklendi.")

    def notlari_listele(self):
        if not self.notlar:
            print("Henüz bir not eklenmedi.")
        else:
            self.notlar.sort(key=lambda x: x.tarih)
            for i, not_ in enumerate(self.notlar, 1):
                print(f"{i}. Tarih: {not_.tarih}, Not: {not_.icerik}")

    def not_sil(self, index):
        if 0 <= index < len(self.notlar):
            silinen = self.notlar.pop(index)
            print(f"Not silindi: Tarih: {silinen.tarih}, Not: {silinen.icerik}")
        else:
            print("Geçersiz indeks.")

    def notlari_kaydet(self, dosya_adi):
        with open(dosya_adi, "w", encoding="utf-8") as dosya:
            for not_ in self.notlar:
                dosya.write(f"{not_.tarih}: {not_.icerik}\n")
        print(f"Notlar {dosya_adi} dosyasına kaydedildi.")

    def notlari_yukle(self, dosya_adi):
        try:
            with open(dosya_adi, "r", encoding="utf-8") as dosya:
                self.notlar = []
                for satir in dosya:
                    tarih, icerik = satir.strip().split(": ", 1)
                    self.notlar.append(Not(icerik, tarih))
            print(f"Notlar {dosya_adi} dosyasından yüklendi.")
        except FileNotFoundError:
            print(f"{dosya_adi} dosyası bulunamadı.")

not_defteri = NotDefteri()

not_defteri.not_ekle("Python ödevi tamamlandı.", "2024-12-08")
not_defteri.not_ekle("Alışveriş listesi hazırlandı.", "2024-12-07")

not_defteri.notlari_listele()

not_defteri.not_sil(0)
not_defteri.notlari_listele()

not_defteri.notlari_kaydet("notlar.txt")

not_defteri.notlari_yukle("notlar.txt")
not_defteri.notlari_listele()
