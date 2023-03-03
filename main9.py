import csv
from datetime import datetime

#kütüphaneleri ekliyoruz



#üst sınıf oluşturuyoruz.
class pizza:
    def __init__(self, pizzaAdi,fiyat,boyut): #pizzanın adının boyutunun ve fiyatının olduğunu  tanımlıyorum
        self.pizzaAdi = pizzaAdi
        self.fiyat = fiyat
        self.boyut = boyut

    def get_aciklama(self): #method tanımlıyoruz. pizza nesnesindeki pizza adını döndürmesini istiyoruz.
        return self.pizzaAdi

    def get_fiyat(self): #aynı şekil busefer fiyat tanımlıyoruz.
        return self.fiyat

class sucukPizza(pizza):#alt sınıf oluşturuyoruz
    def __init__(self,boyut): #pizza üst sınıfnıda oluşturduğumuz ad fiyat boyut bölümlerini yazıyoruz.
        super().__init__("Sucuklu Pizza", 30, boyut) #boyut değerini bırakıyoruz çünkü bunu kullanıcıdan atayacağız.


class vejeteryan(pizza):
    def __init__(self,boyut):
        super().__init__("Vejeteryan Pizza", 35, boyut)

class queen(pizza):
    def __init__(self,boyut):
        super().__init__("Queen Pizza", 40,boyut)



class ekstra:
    def __init__(self,sosAdi,fiyat): #pizzanın ekstra seçeneklerinin üst sınıfını oluşturuyoruz. pizza sınıfına yaptığımız uygulamayı burada da gerçekleştiriyoruz.
        self.sosAdi = sosAdi
        self.fiyat = fiyat

    def get_aciklama(self):
        return self.sosAdi

    def get_fiyat(self):
        return self.fiyat


class zeytin(ekstra):
    def __init__(self):
        super().__init__("Ekstra Zeytin", 4.0)


class mantar(ekstra):
    def __init__(self):
        super().__init__("Ekstra Mantar", 8.50)

class ekstraSecimYok(ekstra):
    def __init__(self):
        super().__init__("Ekstra İstemiyorum", 0.0)


class decorator: #pizzaları tanımlarken kod karşmaşası yaşadığım için tekrar tekrar yaptıktan sonra bu decorator bölümünü ayırmaya karar verdim.
    def __init__(self,pizza): #burada pizza sınıfına bağlı olarak boyut ve fiyat bilgilerini pizza'nın içerisine eklemek için kullanacağım.
        self.pizza = pizza

    def get_aciklama(self): #pizza üst sınıfından pizza ismini çağıracak.
        return self.pizza.get_aciklama()

    def get_fiyat(self): #pizza üst sınıfından fiyatını çağıracak.
        return self.pizza.get_fiyat()


class boyutDecorator(decorator):
    def __init__(self,pizza,boyut):#pizzanın boyutunu pizzanın isminine seçilen boyut eklenecek ve fiyat değerini atayacak.
        super().__init__(pizza)
        self.boyut = boyut

    def get_aciklama(self):
        return self.pizza.get_aciklama() + " ("+ self.boyut + ")" #ekleme kodu burada.

    def get_fiyat(self):
        if self.boyut == "küçük":
            return self.pizza.get_fiyat() + 15
        elif self.boyut == "orta":
            return self.pizza.get_fiyat() + 40
        elif self.boyut == "büyük":
            return self.pizza.get_fiyat() + 80 #pizzaların sabit boy fiyatları var pizzaların ise kendi fiyatları var.


class ekstraDecorator(decorator):
    def __init__(self,pizza,ekstra):#pizzanın ekstra özelliklerini ekleyecek ve sipariş sonunda fiyatı ekleyecek ve ilavesini yazacak.
        super().__init__(pizza)
        self.ekstra = ekstra

    def get_aciklama(self):
        return self.pizza.get_aciklama() + " ilave " + self.ekstra.get_aciklama()

    def get_fiyat(self):
        return self.pizza.get_fiyat() + self.ekstra.get_fiyat()



#geldik menüye :D
def main():
    print("KOPERNİK PİZZASI KAİNATIN EN SICAK PİİZZAASIIII")
    print("Lütfen Aşağıdan pizzanızı seçiniz (1-3): ")
    print("1. Sucuklu Pizza")
    print("2. Vejeteryan Pizza")
    print("3. Özel Queen Pizza")
    secilenPizza_secilebilir = [1,2,3]        #listedeki seçenekler dışında seçenek yapıldığında sonsuz bir şekilde izin verilen sayıyı girene kadar soruyu tekrar soran bir while döngüsü.
    while True:
        secilenPizza = int(input("Pizza seçimi: "))
        if secilenPizza in secilenPizza_secilebilir:
            print("\n\n\nBoyut önemli :) ")
            print("1. Küçük")
            print("2. Orta")
            print("3. Büyük")
            break
        else:
            print("Lütfen listeden doğru seçim yapınız.")

    pizzaBoyu_secilebilir = [1,2,3]           #aynı şekilde yine seçenek kısıtlaması
    while True:
        pizzaBoyu = int(input("boyutu seçin(1-3): "))
        if pizzaBoyu in pizzaBoyu_secilebilir:
            print("Ekstranızı Seçiniz:")
            print("1. Zeytin")
            print("2. Mantar")
            print("3. Ekstra İstemiyorum.")
            break
        else:
            print("Lütfen listeden doğru seçim yapınız: ")

    verilebilir_cevap = [1,2,3]
    while True:
        ekstraSecimi = int(input("Ekstra Seçiniz: "))
        if ekstraSecimi in verilebilir_cevap:
            break
        else:
            print("Lütfen listeden doğru seçimi yapınız: ")

    if secilenPizza == 1:
        pizza = sucukPizza(pizzaBoyu)
    elif secilenPizza == 2:
        pizza = vejeteryan(pizzaBoyu)
    elif secilenPizza == 3:
        pizza = queen(pizzaBoyu)
    else:
        return

          #burada boyutDecorator'da tanımladığımız küçük orta büyük int değerlerini döndürecek değerler yazmakta. biraz karışık oldu ama okunaklılık açısından çok iyi. pizza boyunu 1 nolu menü seçilirse "küçük" stringidir decorator'a göre "küçük" stringi pizza fiyatı + 15 değerinde.
    if pizzaBoyu == 1:
        pizzaBoyu = "küçük"
    elif pizzaBoyu == 2:
        pizzaBoyu = "orta"
    elif pizzaBoyu == 3:
        pizzaBoyu = "büyük"
    else:
        return

    if ekstraSecimi == 1:
        pizza = ekstraDecorator(pizza, zeytin())
    elif ekstraSecimi == 2:
        pizza = ekstraDecorator(pizza, mantar())
    elif ekstraSecimi == 3:
        pizza = ekstraDecorator(pizza, ekstraSecimYok())

    pizza = boyutDecorator(pizza, pizzaBoyu)

    print("Siparişiniz: " + pizza.get_aciklama()) #artık sürekli güncellediğimiz fiyat ve açıklamayı siparişin sonunda kullanıcıya bildiriyoruz.
    print("Ödemeniz gereken tutar: "+ str(pizza.get_fiyat()) + "₺" )

    adiSoyadi = input("Adınız ve Soyadınız: ")    #kimlik bilgilerini ve kart bilgilerini alıyoruz.
    tc = input("TC Kimlik Numaranız: ")
    krediKartiNo = input("Kredi Kartı Numarası: ")
    KrediKartiCVC = input("CVC giriniz: ")
    siparisSaati = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #sipariş saatini sistemden alıyoruz.

    with open("Orders_Database.csv", mode="a") as file:     #siparişleri Orders_Database.csv adında bir veritabanımıza kaydediyoruz.
        writer = csv.writer(file)
        writer.writerow([siparisSaati,adiSoyadi,tc,krediKartiNo,KrediKartiCVC,pizza.get_aciklama(),pizza.get_fiyat()])


if __name__ == "__main__":
    main()