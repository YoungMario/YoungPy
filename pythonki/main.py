import math


print("""

 _  _    __    __    _  _  __  __  __      __   ____  _____  ____ 
( )/ )  /__\  (  )  ( )/ )(  )(  )(  )    /__\ (_  _)(  _  )(  _ \
 )  (  /(__)\  )(__  )  (  )(__)(  )(__  /(__)\  )(   )(_)(  )   /
(_)\_)(__)(__)(____)(_)\_)(______)(____)(__)(__)(__) (_____)(_)\_)

""")








print ("pole kwadratu - 1 / pole prostokata - 2 / pole rownolegloboku - 3 / pole trapezu - 4 / pole trojkata - 5 / pole trojkata rownobocznego - 6 / pole kola - 7 / pole rombu - 8 / pole rombu - 9")



    
wybor = float(input("wybierz numer: "))


def kwadrat():
    a = input("bok: ")
    a = int(a)
    pkwadratu = a**2
    print("pole kwadratu to", (pkwadratu))

def prostokat():
    a = input("bok1: ")
    b = input("bok2: ")
    a = int(a)
    b = int(b)
    pprostokata = a*b
    print("pole prostokata to", (pprostokata))

def rownoleglobok():
    a = input("bok1: ")
    h = input("wysokosc: ")
    a = int(a)
    h = int(h)
    prownolegloboku = a*h
    print("pole rownolegloboku to", (prownolegloboku))

def trapez():
    pod1 = input("podstawa1: ")
    pod2 = input("podstawa2: ")
    wysokosc = input("wysokosc: ")

    pod1 = int(pod1)
    pod2 = int(pod2)
    wysokosc = int(wysokosc)

    podst = pod1+pod2
    podh = podst*wysokosc
    ptrapezu = podh/2
    print("pole trapezu to", (ptrapezu))

def trojkat():
    a = input("bok: ")
    h = input("wysokosc: ")

    a = int(a)
    h = int(h)

    x = a*h
    ptrojkata = 1/2*x
    print("pole trojkata to", (ptrojkata))

def trojkatrownoboczny():
    a = input("bok: ")

    a = int(a)

    x = a**2*(math.sqrt(3))
    poletrojkatarown = x/4
    print("pole trojkata rownobocznego to", (poletrojkatarown))

def kolo():
    r = input("promien: ")
    r = int(r)
    pkola = math.pi*r**2
    print("pole koła to", (pkola))

def romb():
    a = input("bok: ")
    h = input("wysokosc: ")

    a = int(a)
    h = int(h)

    prombu = a*h
    print("pole rombu to", (prombu))

def rombek():
    e = input("bok1: ")
    f = input("bok2: ")

    e = int(e)
    f = int(f)

    boki = e+f 
    polerombu = boki/2
    print("pole rombu wynosi", (polerombu))

   
if wybor == "1":
    kwadrat()

if wybor == "2":
    prostokat()

if wybor == "3":
    rownoleglobok()

if wybor == "4":
    trapez()

if wybor == "5":
    trojkat()

if wybor == "6":
    trojkatrownoboczny()

if wybor == "7":
    kolo()

if wybor == "8":
    romb()

if wybor == "9":
    rombek()