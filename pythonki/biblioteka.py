import uuid
import os

biblioteka = []

def info_ksiazka(dc:dict):
    for k,v in dc.items():
        print(f"{k} --- {v}")

def info_biblioteka(lst:list):
    for ksizka in lst:
        print("\\\\\\"*20)
        info_ksiazka(ksizka)
        print("\\\\\\"*20)

def czy_ksiazka_istnieje(lst: list, id_inp: str):
    for i in range(len(lst)):
        if str(lst[i]["id"]) == id_inp:
            return True
    return False

def index_instniejacej_kisiazki(lst: list, id_inp: str):
    for i in range(len(lst)):
        if str(lst[i]["id"]) == id_inp:
            return i
    return -1  

def usun_ksiazke(lst: list):
    info_biblioteka(lst)
    print("Enter - zakoncz")
    inp = input("wklej id książki: ")
    if czy_ksiazka_istnieje(lst, inp):
        index = index_instniejacej_kisiazki(lst, inp)
        if index != -1:
            lst.pop(index)
            print("ksiazka usunieta")
        else:
            print("ksiązka nie istnieje.")
    else:
        print("nie ma książki o takim ID")

def tytul():
    print("Text !!!")
    inp = input("podaj tytul: ")
    return inp

def cena():
    print("Liczba !!!")
    inp = float(input("Cena: "))  
    return inp

def liczba_stron():
    print("Liczba calkowita - int !!!")
    inp = int(input("liczba stron: "))
    return inp

def dodawanie(lst: list):
    ksiazka = {
        "id":uuid.uuid4(),
        "tytul":tytul(),
        "cena": cena(),
        "liczba_stron": liczba_stron()
    }
    lst.append(ksiazka)

def edytuj_dane_ksiazki(lst:list):
    info_biblioteka(lst)
    print("Enter - zakoncz")
    inp = input("Wklej ID książki: ")
    if czy_ksiazka_istnieje(lst, inp):
        index_ksiazki = index_instniejacej_kisiazki(lst, inp)
        lst[index_ksiazki]["tytul"] = tytul()
        lst[index_ksiazki]["cena"] = cena()
        lst[index_ksiazki]["liczba_stron"] =liczba_stron()
    else:
        print("nie ma książki o takim ID")
    

def main():
    while True:
        print("\\\\\\"*20)
        print("(1) Wyjdz")
        print("(2) Info o asortymencie")
        print("(3) Usun ksiazke ")
        print("(4) Dodaj ksiazke")
        print("(5) Edytuj ksiazke")
        print("\\\\\\"*20)
        inp = int(input(""))
        os.system("cls") 
        if inp == 1:
            os.system("clear")
            print("\n"*5)
            print("\t WYJŚCIE")
            print("\n"*5)
            break
        elif inp == 2:
            info_biblioteka(biblioteka)
        elif inp == 3:
            usun_ksiazke(biblioteka)
        elif inp == 4:
            dodawanie(biblioteka)
        elif inp == 5:
            edytuj_dane_ksiazki(biblioteka)
        else:
            print("Nie ma takiej operacji") 

if __name__ == "__main__":
    main()
    
