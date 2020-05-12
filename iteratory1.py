import datetime as dt

class Figury():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def Ob(self):
        return (2*self.x)+(2*self.y)

class Kwadrat(Figury):
    def __init__(self,x):
        self.x=x
        self.y=x

fig = Figury(5,4)
print(fig.Ob())

kw = Kwadrat(5)
print(kw.Ob())


class Osoba():
    def __init__(self,imie,nazwisko,dzien_ur,miesiac_ur,rok_ur):
        self.imie = imie
        self.nazwisko = nazwisko
        self.dur = dzien_ur
        self.mur = miesiac_ur
        self.rur = rok_ur

    def wiek(self):
        return dt.date.today().year-self.rur

    def ile_ma_lat(self):
        print(self.imie+" ma {} lat".format(self.wiek()))

class Pracownik(Osoba):
    def __init__(self,imie,nazwisko,dzien_ur,miesiac_ur,rok_ur,stanowisko,pensja,firma):
        self.imie = imie
        self.nazwisko = nazwisko
        self.dur = dzien_ur
        self.mur = miesiac_ur
        self.rur = rok_ur
        self.stano = stanowisko
        self.pensja = pensja
        self.firma = firma

    def jakie_stano(self):
        print(self.imie+" pracuje na stanowisku "+self.stano)

Jarek = Pracownik("Jarek","Kowalsky",15,6,1975,"Prezes",2100,"Microsoft")
print(Jarek.wiek())
Jarek.ile_ma_lat()
Jarek.jakie_stano()

