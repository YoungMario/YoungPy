import random

# Lista postaci zawierająca [HP, Atak, Mana, Złoto]
postacie = [[200, 60, 0, 15], [150, 30, 150, 20], [120, 40, 30, 35], [9999999, 9999999, 9999999, 9999999]]
# Lista nazw postaci
nazwyPostaci = ["Wojownik", "Mag", "Bandyta", "BÓG"]
# Zmienne globalne dla gracza
poziom = 0
hp = 0
attack = 0
mana = 0
gold = 0
# Zmienne globalne dla potwora
mhp = 0
mattack = 0
mmana = 0
mgold = 0
# Nazwa gracza
name = ""
# Nazwa potwora
mname = ""

# Funkcja wyświetlająca komunikat z aktualnymi statystykami
def komunikat(x):
    staty()
    print("\n◄►─────────────────────────────────────────────────────────────────────◄►")
    print(f"{x}  ")
    print("◄►─────────────────────────────────────────────────────────────────────◄►")
    input()
    staty()

# Funkcja wyświetlająca aktualne statystyki gracza i potwora
def staty():
    if name == "":
        return
    print("◄►───────────────────────────────◄►")
    print(f"    KLASA    ────► {name}")
    print(f"    HP       ────► {hp} ")
    print(f"    ATTACK   ────► {attack} ")
    print(f"    MANA     ────► {mana} ")
    print(f"    GOLD     ────► {gold} ")
    print("◄►───────────────────────────────◄►")
    if mhp > 0:
        print("◄►───────────────────────────────◄►")
        print(f"    NAZWA    ────► {mname} ")
        print(f"    HP       ────► {mhp} ")
        print(f"    ATTACK   ────► {mattack} ")
        print(f"    MANA     ────► {mmana} ")
        print(f"    GOLD     ────► {mgold} ")
        print("◄►───────────────────────────────◄►")

# Funkcja pobierająca liczbę całkowitą od użytkownika zabezpieczona przed błędami
def getIntFromConsole():
    x = -1
    while x == -1:
        try:
            x = int(input())
        except Exception:
            print("Wpisz cyfrę.")
    return x

# Funkcja wybierająca poziom trudności
def poziomTrudnosci():
    print("\n◄►───────────WYBIERZ─POZIOM─TRUDNOŚCI─────────────◄►")
    print("        1 ────► Łatwy")
    print("        2 ────► Średni")
    print("        3 ────► Trudny")
    print("        4 ────► Imposible")
    print("◄►──────────────────────────────────────────────────◄►")
    global poziom
    while poziom == 0:
        poziom = getIntFromConsole()
        if poziom > 4 or poziom < 1:
            print("Podaj poziom pomiędzy 1 a 4")
            poziom = 0

# Funkcja wybierająca postać gracza
def wyborPostac():
    global hp, attack, mana, gold, name
    hp = 0
    print("\n◄►─────────────────WYBIERZ─POSTAĆ─────────────────◄►")
    print("        1 ────► Wojownik")
    print("        2 ────► Mag")
    print("        3 ────► Bandyta")
    print("◄►──────────────────────────────────────────────────◄►")
    while hp == 0:
        input = getIntFromConsole()
        if input != 1 and input != 2 and input != 3 and input != 4:
            print("zły numer")
        else:
            x = input - 1
            hp = postacie[x][0]
            attack = postacie[x][1]
            mana = postacie[x][2]
            gold = postacie[x][3]
            name = nazwyPostaci[x]
    staty()

# Funkcja generująca statystyki potwora na podstawie wybranego poziomu trudności
def generowanieStatowPotwora():
    global mhp, mattack, mmana, mgold
    rnd = random.Random()
    if poziom == 1:
        mhp = rnd.randint(20, 50)
        mattack = rnd.randint(15, 50)
        mmana = rnd.randint(5, 20)
        mgold = rnd.randint(3, 40)
    elif poziom == 2:
        mhp = rnd.randint(40, 70)
        mattack = rnd.randint(20, 55)
        mmana = rnd.randint(10, 30)
        mgold = rnd.randint(3, 40)
    elif poziom == 3:
        mhp = rnd.randint(60, 100)
        mattack = rnd.randint(40, 65)
        mmana = rnd.randint(20, 50)
        mgold = rnd.randint(12, 45)
    elif poziom == 4:
        mhp = rnd.randint(60, 100)
        mattack = rnd.randint(50, 70)
        mmana = rnd.randint(30, 50)
        mgold = rnd.randint(20, 50)
    danePotwora()

# Funkcja przypisująca nazwę potwora na podstawie jego zdrowia
def danePotwora():
    global mname, mhp
    if mhp <= 30:
        mname = "SZCZĄTKI"
    elif mhp > 30 and mhp <= 80:
        mname = "SZKIELET"
    elif mhp > 80 and mhp <= 100:
        mname = "ZOMBIE"
    elif mhp > 100 and mhp <= 130:
        mname = "MINOTAUR"
    elif mhp > 120 and mhp <= 180:
        mname = "SMOK"
    elif mhp > 180:
        mname = "ŻNIWIARZ"

# Funkcja do uzdrowienia gracza
def heal():
    global hp, mana
    if mana >= 20:
        hp += 15
        mana -= 20
        komunikat("Użyłeś Heala (+15 hp  -20 many)")
    else:
        komunikat("Brak many")

# Funkcja do silnego uzdrowienia gracza
def megaHeal():
    global hp, mana
    if mana >= 100:
        hp += 90
        mana -= 100
        komunikat("Użyłeś Mega Heala (+90 hp  -100 many)")
    else:
        komunikat("Brak many")

# Funkcja do wzmocnienia gracza
def boost():
    global hp, attack, mana
    if mana >= 30:
        hp += 10
        attack += 30
        mana -= 30
        komunikat("Użyłeś Boosta (+10 hp   +30 dmg   -30 many)")
    else:
        komunikat("Brak many")

# Funkcja do bardzo silnego uzdrowienia gracza
def superBoost():
    global hp, attack, mana
    if mana >= 30:
        hp += 100
        attack += 1000
        mana -= 400
        komunikat("Użyłeś Super Sayanina (+100 hp   +1000 dmg   -400 many)")
    else:
        komunikat("Brak many")

# Funkcja reprezentująca sklep, gdzie gracz może kupić przedmioty
def sklep():
    staty()
    print("\n◄►───────────────────────────────────────────────◄►")
    print("    1 ────► heal (+25 hp)            5 złota")
    print("    2 ────► lepsza broń (+20 ataku) 13 złota")
    print("    3 ────► relaks w spa (+50 many)  8 złota")
    print("    * ────► wyjdz z sklepu")
    print("◄►───────────────────────────────────────────────◄►")
    input = getIntFromConsole()
    if input == 1:
        sklepHeal()
    elif input == 2:
        sklepBron()
    elif input == 3:
        sklepRelaksSpa()
    else:
        komunikat("Wychodzisz ze sklepu")

# Funkcja relaksująca w spa, zwiększająca ilość many gracza
def sklepRelaksSpa():
    global gold, mana
    CENA_SPA = 8
    if gold - CENA_SPA < 0:
        komunikat(f"Nie masz wystarczająco pieniędzy\n Potrzebujesz jeszcze {CENA_SPA - gold} złota")
    else:
        gold -= CENA_SPA
        mana += 50

# Funkcja sprzedająca lepszą broń, zwiększającą atak gracza
def sklepBron():
    global gold, attack
    CENA_BRON = 15
    if gold - CENA_BRON < 0:
        komunikat(f"Nie masz wystarczająco pieniędzy\n Potrzebujesz jeszcze {CENA_BRON - gold} złota")
    else:
        gold -= CENA_BRON
        attack += 20

# Funkcja sprzedająca uzdrowienie, zwiększającą punkty życia gracza
def sklepHeal():
    global gold, hp
    CENA_HEAL = 5
    if gold - CENA_HEAL < 0:
        komunikat(f"Nie masz wystarczająco pieniędzy\n Potrzebujesz jeszcze {CENA_HEAL - gold} złota")
    else:
        gold -= CENA_HEAL
        hp += 25

# Główna funkcja, sterująca przebiegiem gry
def main():
    round = 0
    poziomTrudnosci()
    wyborPostac()
    global mhp, mmana, mattack, mgold
    while hp > 0:
        staty()
        print("\n◄►────────────────CO─CHCESZ─ZROBIĆ────────────────◄►")
        print("    1 ────► Idz do sklepu")
        print("    2 ────► Idz na wyprawe")
        print("◄►────────────────────────────────────────────────◄►")
        inp = getIntFromConsole()
        if inp == 1:
            sklep()
        elif inp == 2:
            generowanieStatowPotwora()
            staty()
            rnn = random.Random()
            r = rnn.randint(8, 16)
            r = 2
            if round == r:
                mhp = mhp * 4 + 50
                mattack = mattack * 3
                mmana = mmana * 3 + 100
                mgold = mgold * 3
                bossSpotkanie()
                round = 0
            else:
                normalSpotkanie()
                round += 1

# Funkcja reprezentująca normalną walkę z potworem
def normalwalka():
    global hp, mhp, gold, mgold, mana, mmana
    staty()
    runda = 1
    print("Walka")
    hp -= mattack
    if hp < 0:
        hp = 0
    mhp -= attack
    if mhp < 0:
        mhp = 0
    komunikat(f"Potwór zadaje ci {mattack}\nTy zadajesz mu {attack}")
    if hp == 0:
        komunikat("UMARŁEŚ!!!!")
        return
    runda += 1
    if mhp == 0:
        komunikat(f"zabierasz potworowi {mgold} złota i pobierasz kawałki many z jego duszy")
        gold += mgold
        mana += mmana

# Funkcja reprezentująca zaklęcia w normalnej walce
def normalZaklecia():
    global hp, mana
    staty()
    print("\n◄►───────────────────────────────────────────────────────────────────────◄►")
    print("    1 ────► heal                           +15 hp      -20 many")
    print("    2 ────► Mega Heal                      +90 hp     -100 many)")
    print("    3 ────► Boost              +30 dmg     +10 hp      -30 many)")
    print("◄►───────────────────────────────────────────────────────────────────────◄►")
    x = getIntFromConsole()
    if x == 1:
        heal()
    elif x == 2:
        megaHeal()
    elif x == 3:
        boost()
    else:
        komunikat("zły numer")
    return x

# Funkcja reprezentująca ucieczkę w normalnej walce
def normalUcieczka():
    global hp
    rnd = random.Random()
    ucieczka = rnd.randint(1, 6)
    if ucieczka == 2 or ucieczka == 5:
        komunikat("Udaje ci się uciec")
    else:
        hp -= (mattack * 2)
        komunikat("Nie udaje ci się uciec potwór zadaje ci podwójne obrażenia")

# Funkcja reprezentująca normalne spotkanie z potworem
def normalSpotkanie():
    while mhp > 0:
        print("\n◄►────────────────SPOTYKASZ─POTWORA────────────────◄►")
        print("    1 ────► Walczysz")
        print("    2 ────► Używasz Zaklęć")
        print("    3 ────► Spróbuj ucieczki")
        print("◄►────────────────────────────────────────────────◄►")
        input = getIntFromConsole()
        if input == 1:
            normalwalka()
        if input == 2:
            normalZaklecia()
        if input == 3:
            normalUcieczka()

# Funkcja reprezentująca spotkanie z bossem
def bossSpotkanie():
    print("\n◄►────────────────SPOTYKASZ─BOSSA────────────────◄►")
    print("    1 ────► Walczysz")
    print("    2 ────► Używasz Zaklęć")
    print("    3 ────► Spróbuj ucieczki")
    print("◄►───────────────────────────────────────────────◄►")
    i = getIntFromConsole()
    if i == 1:
        bossWalka()
    if i == 2:
        bossZaklecia()

# Funkcja reprezentująca walkę z bossem
def bossWalka():
    global hp, mhp, gold, mgold, mana, mmana
    runda = 1
    komunikat("Walka!!!")
    while mhp > 0:
        komunikat(f"Boss zadaje ci {mattack}")
        hp -= mattack
        komunikat(f"Ty zadajesz mu {attack}")
        mhp -= attack
        if hp <= 0:
            raise Exception("Umarłeś")
        komunikat(f"zabierasz Bossowi {mgold} złota i pobierasz kawałki manny z jego duszy")
        gold += mgold
        mana += mmana
        runda += 1

# Funkcja reprezentująca zaklęcia w walce z bossem
def bossZaklecia():
    z = 0
    staty()
    print("\n◄►───────────────────────────────────────────────────────────────────────◄►")
    print("    1 ────► heal                           +15 hp      -20 many")
    print("    2 ────► Mega Heal                      +90 hp     -100 many)")
    print("    3 ────► Boost              +30 dmg     +10 hp      -30 many)")
    print("    4 ────► Super Sayanin    +1000 dmg    +100 hp     -400 many)")
    print("◄►───────────────────────────────────────────────────────────────────────◄►")
    z = getIntFromConsole()
    if z == 1:
        heal()
    if z == 2:
        megaHeal()
    if z == 3:
        boost()
    if z == 4:
        superBoost()
    else:
        komunikat("zły numer")

# Główna pętla gry
if __name__ == "__main__":
    main()i
    
    
    
    
    
    
