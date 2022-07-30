from inspect import ismemberdescriptor


class Talaba:  # Yangi class yaratildi
    def __init__(self,ism,familya,tyil): # class ni xususiyatlari kiritilepti
         self.ism = ism             # shu 3 tasi kiritilepti
         self.familya = familya     # masalan:   ism.ism buleptiku ism so'ralepti keyin o'sha isim o'rniga qo'yilgan qiymat chiqepti
         self.tyil = tyil           #
         
    def get_name(self): # masalan talaba1.get_name so'ralsa ism qiymatini chiqarib beradi 
        return self.ism 
        
    def get_age(self,yil):
        return yil - self.tyil

    def tanishtir(self):
        return f"ismim {self.ism} {self.familya}, tug'ilgan yilim {self.tyil}"  # masalan talaba1.tanishtir() busa Ismim Olim pistonchiyev tug'ilgan yilim 2005 bo'b chiqadi

talaba1 = Talaba("Olim","pistonchiyev",2005)  # masalan: talaba1 yozilib ism so'ralsa Olim chiqadi
talaba2 = Talaba("Mo'min","Gulomivich",2005)  # masalan: talaba2 yozilib familya so'ralsa Gulomivich chiqadi
talaba3 = Talaba("Doston","palonchiyev",2006) # masalan: talaba3 yozilib tyil so'ralsa 2006 chiqadi



talaba1.get_age(2021)

talaba2.get_age(2022)

