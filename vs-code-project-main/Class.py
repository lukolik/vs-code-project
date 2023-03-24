# class Human():

#     def __init__(self, fio, birsday, phone, city, country, address):
#         self.fio = fio
#         self.birsday = birsday
#         self.phone = phone
#         self.city = city
#         self.country = country
#         self.address = address
    
#     def setFio(self):
#         self.fio = input("enter FIO - ")
    
#     def setBirsday(self):
#         self.birsday = input("enter birsday - ")
    

#     def setPhone(self):
#         self.phone = input("enter phone - ")
    

#     def setCity(self):
#         self.city = input("enter city - ")
    

#     def setCountry(self):
#         self.country = input("enter country - ")

#     def setAddres(self):
#         self.address = input("enter address - ")
    
#     def setAll(self):
#         self.fio = input("enter FIO - ")
#         self.birsday = input("enter birsday - ")
#         self.phone = input("enter phone - ")
#         self.city = input("enter city - ")
#         self.country = input("enter country - ")
#         self.address = input("enter address - ")

#     def getFio(self):
#         print(self.fio)

#     def getBirsday(self):
#         print(self.birsday)
    
#     def getPhone(self):
#         print(self.phone)
    
#     def getCity(self):
#         print(self.city)
    
#     def getCountry(self):
#         print(self.country)

#     def getAddres(self):
#         print(self.address)

#     def out(self):
#          print("Fio = ", self.fio)
#          print("Brisday = ", self.birsday)
#          print("Phone = ",self.phone)
#          print("City = ", self.city)
#          print("Country = ", self.country)
#          print("Address = ", self.address)

# msiha = Human("misha", "16.10.2000", "+7988865423", "Sochi", "RF", "Mishaon")

# msiha.out()
# msiha.setFio()
# msiha.out()


# class City():

#     def __init__(self, name, rigion, country, index_city, city_phone):
#         self.name = name
#         self.rigion = rigion
#         self.country = country
#         self.index_city = index_city
#         self.city_phone = city_phone
       
    
#     def setName(self):
#         self.name = input("enter FIO - ")
    
#     def setRigion(self):
#         self.rigion = input("enter birsday - ")
    

#     def setCountry(self):
#         self.country = input("enter phone - ")
    

#     def setindex_city(self):
#         self.index_city = input("enter city - ")
    

#     def setCity_phone(self):
#         self.city_phone = input("enter country - ")

   
    
#     def setAll(self):
#         self.name = input("enter name - ")
#         self.rigion = input("enter rigion - ")
#         self.country = input("enter country - ")
#         self.index_city = input("enter index - ")
#         self.city_phone = input("enter phone_city - ")

    
#     def getName(self):
#         print(self.name)

#     def getRigion(self):
#         print(self.rigion)
    
#     def getCountry(self):
#         print(self.country)
    
#     def getIndex_City(self):
#         print(self.index_city)
    
#     def getCity_Phone(self):
#         print(self.city_phone)

    

#     def out(self):
#          print("name = ", self.name)
#          print("rigion = ", self.rigion)
#          print("country = ",self.country)
#          print("index_city = ", self.index_city)
#          print("city_phone = ", self.city_phone)


# class Country:
#     def __init__(self, name, rigion, country, index_city, city_phone):
#         self.name = name
#         self.rigion = rigion
#         self.country = country
#         self.index_city = index_city
#         self.city_phone = city_phone


class Transport():
    def __init__(self, speed, oil):
        self.speed = speed
        self.oil = oil
    
    

    def setSpeed(self, speed):
        self._speed = speed

    def setOil(self, oil):
        self._oil = oil

    def getSpeed(self):
        return self._speed
    
    def getOil(self):
        return self._oil
    
    speed = property(getSpeed, setSpeed)
    oil = property(getOil, setOil)


class LandTr(Transport):
    def __init__(self, speed, oil, model):
        super().__init__(speed, oil)
        self.__model = model
    
    def getModel(self):
        return self.__model
    
    def setModel(self, model):
        self.__model = model

    landTr = property(getModel, setModel)


class AirTr(Transport):
    
    def __init__(self, speed, oil, marka):
        super().__init__(speed, oil)
        self.__marka = marka
    
    def getMarka(self):
        return self.__marka
    
    def setMarka(self, marka):
        self.__marka = marka
    
    airTr = property(getMarka, setMarka)


class WTr(Transport):
    def __init__(self, speed, oil, tonage):
        super().__init__(speed, oil)
        self.__tonage = tonage
    
    def getTonage(self):
        return self.__tonage
    
    def setTonage(self, tonage):
        self.__tonage = tonage
    
    wTr = property(getTonage, setTonage)




class Auto(LandTr):

    def __init__(self, speed, oil, model, color):
        super().__init__(speed, oil, model)
        self.__color = color

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    auto = property(getColor, setColor)

    def Out(self):
        print(self.speed, self.oil, self.__model, self.__color)

class Airplane(AirTr):

    def __init__(self, speed, oil, marka, pas):
        super().__init__(speed, oil, marka)
        self.__pas = pas

    def getPas(self):
        return self.__pas

    def setPas(self, pas):
        self.__pas = pas

    Pas = property(getPas, setPas)

    def Out(self):
        print(self.speed, self.oil, self.__marka, self.__pas)   
    

class Ship(WTr):
    def __init__(self, speed, oil, tonage, type):
        super().__init__(speed, oil, tonage)
        self.__type = type
    
    def getType(self):
        return self.__type
    
    def setType(self, type):
        self.__type = type
    
    Type = property(getType, setType)

    def Out(self):
        print(self.speed, self.oil, self.__tonage, self.__type)

listOut = [ Auto(100, "92", "NIVA", "Red"), 
            Airplane(100, "92", "Boin-120", 100),
            Ship(100, "92", "test", "test")]


def Out(transport):
    for t in transport:
        t.Out()

Out(listOut)

