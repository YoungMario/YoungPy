class Zwierze:
    def __init__(self, waga, prędkość, zwierze, imie) -> None:
        self.waga = waga
        self.prędkość = prędkość
        self.zwierze = zwierze
        self.imie = imie
        pass
    def wyświetl_inf_zwierze(self):
        print("=="*25,f"\nZwierze {self.zwierze} \nImie {self.imie} \nWaga {self.waga} \nPrędkość {self.prędkość}\n","=="*25)

kot = Zwierze("6kg","25 kmh","kot","pookie")
kot.wyświetl_inf_zwierze()
pies = Zwierze("17kg","34 kmh","pies","wookie" )
pies.wyświetl_inf_zwierze()
mysz = Zwierze("250g","3 kmh","mysz","dookie")
mysz.wyświetl_inf_zwierze()

class Pierwiastek:
    def __init__(self, pierwiastek, grupa, okres, elektroujemnosc) -> None:
        self.pierwiastek = pierwiastek
        self.grupa = grupa
        self.okres = okres
        self.elektroujemnosc = elektroujemnosc
        pass

    def wyświetl_inf_pierwiastki(self):
        print("=="*25,f"\nPierwiastek {self.pierwiastek} \nGrupa {self.grupa} \nOkres {self.okres} \nelektroujemnosc {self.elektroujemnosc}\n","=="*25)

azot = Pierwiastek("azot","15","2","3,04")
azot.wyświetl_inf_pierwiastki()
magnez = Pierwiastek("magnez","2","3","1,31")
magnez.wyświetl_inf_pierwiastki()
bar = Pierwiastek("bar","2","6","0,89")
bar.wyświetl_inf_pierwiastki()
