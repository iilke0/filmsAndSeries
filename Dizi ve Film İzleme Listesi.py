# Rastgele seçim yapabilmek için Python'un random modülünü dahil ediyoruz.
import random
class Icerik:
    """İçerik Sınıfı"""
    def __init__(self, ad, tur, yil, dil, yas_siniri):
        # İçeriğin adı, türü, yılı, dili ve yaş sınırı bilgilerini alır ve saklar.
        self.ad = ad
        self.tur = tur
        self.yil = yil
        self.dil = dil
        self.yas_siniri = yas_siniri
        self.puan = None  # Varsayılan olarak içeriğin bir puanı yoktur.

class Node:
    """Bağlı liste düğümü"""
    def __init__(self, veri):
         # Bağlı listede saklanacak veriyi ve bir sonraki düğüme işaretçi oluşturur.
        self.veri = veri
        self.next = None

class BagliListe:
    """Bağlı liste sınıfı (İzleme Listesi)"""
    def __init__(self):
        # Bağlı listenin başlangıç noktasıdır.
        self.head = None

    def ekle(self, veri):
        # Yeni bir düğüm oluşturur ve bağlı listeye ekler.
        yeni_dugum = Node(veri)
        if not self.head:  # Liste boşsa
            self.head = yeni_dugum
        else:
            # Listenin sonuna eklemek için mevcut düğümleri gezer.
            temp = self.head
            while temp.next: # temp değişkeninin işaret ettiği düğümün next değeri None olana kadar çalışacak bir while döngüsüdür.
                temp = temp.next 
            temp.next = yeni_dugum

    def listele(self):
        # Bağlı listeyi sırasıyla yazdırır.
        if not self.head:
            print("İzleme listesi boş!")
            return
        print("İzleme Listesi:")
        temp = self.head
        while temp:
            print(f"- {temp.veri}")
            temp = temp.next

    def listeleFavori(self):
        # Favori listesini sırasıyla yazdırır.
        if not self.head:
            print("Favori listesi boş!")
            return
        print("Favori Listesi: ")
        temp = self.head
        while temp:
            print(f"- {temp.veri}")
            temp = temp.next

    def kaldir(self, veri):
        # Bağlı listenin ilk elemanını kontrol et
        if not self.head:
            print("İzleme listesi zaten boş!")
            return

        # İlk düğümde aranan veriyi bulursak, onu kaldırıyoruz
        if self.head.veri == veri:
            print(f"{self.head.veri} izleme listesinden çıkarıldı!")
            self.head = self.head.next
            return

        # İlk düğümden sonraki düğümlerde arama yapıyoruz
        current = self.head
        while current.next:
            if current.next.veri == veri:
                print(f"{current.next.veri} izleme listesinden çıkarıldı!")
                current.next = current.next.next  # current.next'i kaldırıyoruz
                return
            current = current.next

        # Eğer veri listede yoksa
        print(f"{veri} izleme listesinde bulunamadı!")
    

class IzlemeUygulamasi:
    # İzleme uygulamasını temsil eden ana sınıf.
    def __init__(self):
        # İçerik türlerini tutan bir HashMap, izlenenleri tutan bir yığın,
        # izleme ve favori listeleri için bağlı listeler oluşturur.
        self.turler = {}  # HashMap: Kategorilere göre içerik tutar
        self.izlenenler = []  # Yığın: Geçmişte izlenen içerikler
        self.izleme_listesi = BagliListe()  # Bağlı liste: İzleme listesi
        self.favori_listesi = BagliListe()  # Bağlı liste: Favori listesi
        self.icerikler = [] # Tüm içerikleri saklayan bir liste.

    def icerik_ekle(self, ad, tur, yil, dil, yas_siniri):
        # Yeni içerik oluşturup uygun kategoriye ekler.
        icerik = Icerik(ad, tur, yil, dil, yas_siniri)
        if tur not in self.turler:
            # Eğer tür yoksa yeni bir kategori oluşturur.
            self.turler[tur] = []
        self.turler[tur].append(icerik)
        self.icerikler.append(icerik) # Genel listeye ekler.
        print(f"'{tur}' türüne '{ad}' içeriği eklendi!")

    def izleme_listesine_ekle(self, ad):
        # İçerik listesinden belirtilen ada sahip bir içerik olup olmadığını kontrol eder.
        if not any (icerik.ad == ad for icerik in self.icerikler):
            print(f"{ad} içerik listesinde bulunamadı!")
            return
        # İzleme listesine bir içerik ekler.
        self.izleme_listesi.ekle(ad)
        print(f"'{ad}' izleme listesine eklendi!")

    def izleme_listesini_gor(self):
        # İzleme listesini görüntüle
        self.izleme_listesi.listele()

    def izlenen_olarak_isaretle(self, ad):
        # Bir içeriği izlenmiş olarak işaretler ve puan verir.
        for tur_listesi in self.turler.values():
            for icerik in tur_listesi:
                if icerik.ad == ad:
                    while True:
                        try:
                            # Kullanıcıdan 1-10 arasında bir puan ister.
                            puan = int(input(f"'{ad}' için 1-10 arasında bir puan verin: "))
                            if 1 <= puan <= 10:
                                icerik.puan = puan
                                break
                            else:
                                print("Lütfen 1 ile 10 arasında bir puan girin!")
                        except ValueError:
                            print("Lütfen geçerli bir sayı girin!")
                    self.izlenenler.append(icerik) # İçeriği yığına ekler.
                    print(f"'{ad}' izlenmiş olarak işaretlendi, puan: {puan}")
                    self.izleme_listesi.kaldir(ad) # İzleme listesinden kaldırır.
                    return
        print(f"'{ad}' izleme listesinde bulunamadı!")

    def izlenenleri_gor(self):
        # İzlenen içerikleri yazdırır.(Yığın)
        if not self.izlenenler:
            print("Henüz izlenen içerik yok!")
            return
        print("\nGeçmişte İzlenenler:")
        for icerik in reversed(self.izlenenler): # Yığından son gireni önce yazdırır.
            print(f"- Film İsmi: {icerik.ad}, Türü: {icerik.tur}, Yılı: {icerik.yil}, Dili: {icerik.dil}, Yaş Sınırı: {icerik.yas_siniri}, Puan: {icerik.puan}")

    def ture_gore_arama(self, tur):
        # HashMap'ten bir tür altında içerikleri listelemek için kullanılır.
        if tur not in self.turler or not self.turler[tur]:
            # Eğer tür yoksa veya bu türde içerik yoksa mesaj gösterilir.
            print(f"'{tur}' türünde içerik bulunamadı!")
            return
        print(f"\nTür: {tur}")
        # Türün altındaki tüm içerikleri listeler.
        for icerik in self.turler[tur]:
            print(f"- Film İsmi: {icerik.ad}, Yılı: {icerik.yil}, Dili: {icerik.dil}, Yaş Sınırı: {icerik.yas_siniri}, Puan: {icerik.puan}")
            
    def yil_gore_arama(self, yil):
        # Belirli bir yıl için içerik arar.
        bulunanlar = []
        for tur in self.turler.values():
            # Tüm türlerin içeriklerini kontrol eder.
            for icerik in tur:
                if icerik.yil == yil:
                    bulunanlar.append(icerik)
        if not bulunanlar:
            # Hiç içerik bulunamazsa bir mesaj gösterilir.
            print(f"{yil} yılına ait içerik bulunamadı!")
        else:
            print(f"{yil} yılına ait içerikler:")
            for icerik in bulunanlar:
                # Bulunan içerikler sıralanır.
                print(f"- Film İsmi: {icerik.ad}, Türü: {icerik.tur}, Dili: {icerik.dil}, Yaş Sınırı: {icerik.yas_siniri}, Puan: {icerik.puan}")

    def dil_gore_arama(self, dil):
        # Belirli bir dildeki içerikleri arar.
        bulunanlar = []
        for tur in self.turler.values():
            for icerik in tur:
                if icerik.dil.lower() == dil.lower():
                    # Kullanıcıdan gelen dil girdisi büyük/küçük harfe duyarsız karşılaştırılır.
                    bulunanlar.append(icerik)
        if not bulunanlar:
            print(f"'{dil}' dilinde içerik bulunamadı!")
        else:
            print(f"'{dil}' dilindeki içerikler:")
            for icerik in bulunanlar:
                # Bulunan içerikler sıralanır.
                print(f"- Film İsmi: {icerik.ad}, Türü: {icerik.tur}, Yılı: {icerik.yil}, Yaş Sınırı: {icerik.yas_siniri}, Puan: {icerik.puan}")


    def yas_siniri_gore_arama(self, yas_siniri):
        # Belirli bir yaş sınırına kadar içerikleri arar.
        bulunanlar = []
        for tur in self.turler.values():
            for icerik in tur:
                if icerik.yas_siniri <= yas_siniri:
                    # Kullanıcının yaş sınırına uygun içerikler eklenir.
                    bulunanlar.append(icerik)
        if not bulunanlar:
            print(f"{yas_siniri}+ yaş sınırına uygun içerik bulunamadı!")
        else:
            print(f"{yas_siniri}+ yaş sınırına uygun içerikler:")
            for icerik in bulunanlar:
                # Uygun içerikler listelenir.
                print(f"- Film İsmi: {icerik.ad}, Türü: {icerik.tur}, Dili: {icerik.dil}, Yılı: {icerik.yil}, Puan: {icerik.puan}")

    def random_icerik_sec(self):
        # Mevcut içerikler arasından rastgele bir tanesini seçer.
        if not self.icerikler:
            # İçerik yoksa hata mesajı gösterir.
            print("İçerik bulunmamaktadır!")
            return
        secilen_icerik = random.choice(self.icerikler) # Rastgele seçim.
        print(f"Rastgele seçilen içerik: {secilen_icerik.ad}")

    def favori_listesine_ekle(self, ad):
        # Favori listesine bir içerik ekler.
        self.favori_listesi.ekle(ad)
        print(f"'{ad}' favori listesine eklendi!")

    def favori_listesini_gor(self):
        # Favori listesini sırasıyla yazdırır.
        self.favori_listesi.listeleFavori()

    def izlenen_sayisi(self):
         # İzlenen film sayısını döndürür.
        return len(self.izlenenler)

# İzleme Uygulaması çalıştırma
uygulama = IzlemeUygulamasi()  # İzleme uygulaması nesnesi oluşturulur.

while True:
    print("\n--- İzleme Uygulaması ---")
    print("1. İçerik Ekle")
    print("2. İçerik Arama")
    print("3. İzleme Listesine Ekle")
    print("4. İzleme Listesini Görüntüle")
    print("5. İzlendi Olarak İşaretle")
    print("6. İzlenenleri Görüntüle")
    print("7. Rastegele İçerik Seç")
    print("8. Favori Listesine Ekle")
    print("9. Favori Listesini Görüntüle")
    print("10. Toplam İzlenen Film Sayısı")
    print("11. Çıkış")
    secim = input("Bir işlem seçin (1-11): ")

    if secim == "1":
        ad = input("İçeriğin adı: ")
        tur = input("Tür: ")
        yil = int(input("Yıl: "))
        dil = input("Dil: ")
        yas_siniri = int(input("Yaş sınırı: "))
        uygulama.icerik_ekle(ad, tur, yil, dil, yas_siniri)
    elif secim == "2":
        print("1. Türe Göre Ara")
        print("2. Yıla Göre Ara")
        print("3. Dile Göre Ara")
        print("4. Yaş Sınırına Göre Ara")
        secim = input("Arama Şeklini Seçiniz: ")
        if secim == "1":
            tur = input("Listelemek istediğiniz tür: ")
            uygulama.ture_gore_arama(tur)
        elif secim == "2":
            yil = int(input("Aramak istediğiniz yıl: "))
            uygulama.yil_gore_arama(yil)
        elif secim == "3":
            dil = input("Aramak istediğiniz dil: ")
            uygulama.dil_gore_arama(dil)
        elif secim == "4":
            yas_siniri = int(input("Aramak istediğiniz yaş sınırı: "))
            uygulama.yas_siniri_gore_arama(yas_siniri)
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")
    elif secim == "3":
        ad = input("İzleme listesine eklemek istediğiniz içerik: ")
        uygulama.izleme_listesine_ekle(ad)
    elif secim == "4":
        uygulama.izleme_listesini_gor()
    elif secim == "5":
        ad = input("İzlenen olarak işaretlemek istediğiniz içerik: ")
        uygulama.izlenen_olarak_isaretle(ad)
    elif secim == "6":
        uygulama.izlenenleri_gor()
    elif secim == "7":
        uygulama.random_icerik_sec()
    elif secim == "8":
        ad = input("Favori listesine eklemek istediğiniz içerik: ")
        uygulama.favori_listesine_ekle(ad)
    elif secim == "9":
        uygulama.favori_listesini_gor()
    elif secim == "10":
        print(f"İzlenen film sayısı: {uygulama.izlenen_sayisi()}")
    elif secim == "11":
        print("Çıkış yapılıyor. Görüşmek üzere!")
        break
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")