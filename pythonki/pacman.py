from random import choice
from turtle import *
from freegames import floor, vector

class Pacman():    
    __state = {"score": 0}      #  wynik
    __path = None
    __writer = None
    __aim = vector(0, 0) # w którą strone ma iść pacman
    __pacman = vector(-40, -0) # położenie startowe pacmana
    __ghosts = [  # duszki ::::: w którą strone ma iść ,, położenie startowe
        [vector(-180, 160), vector(5, 0)],
        [vector(-180, -160), vector(0, 5)],
        [vector(100, 160), vector(0, -5)],
        [vector(100, -160), vector(-5, 0)],
    ]
    __Mapa = [ # 0 - czarne pola   1 - niebieski/"path"
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]   


       

    #rysuje kwadracik 20x20
    def __square(self,x, y):
        self.__path.up() # podniesienie ołówka
        self.__path.goto(x, y) # ustawienie ołówka
        self.__path.down() # opuszcza ołówek

        self.__path.begin_fill() # oznacza początek rosowania figury, która będzie wypełniana.


        for count in range(4):  # liczy do 4
            self.__path.forward(20) # rysuje linię 20px 
            self.__path.left(90) # żółw obraca się w lewo o 90 stopni

        self.__path.end_fill() # koniec rysowania figury wypełnianej


    #  jako że rysowanie jest zepsute to to naprawia
    def __offset(self, point):
        x = (floor(point.x, 20) + 200) / 20 # przemieszcza w osi X
        y = (180 - floor(point.y, 20)) / 20 # przemieszcza w osi Y
        index = int(x + y * 20) # <-ilość pól   <------to ta wartość na mapie
        return index #zwraca 

    #  sprawdzanie czy można po tym chodzić
    def __valid(self,point):
        index = self.__offset(point)   # oblicza index tablicy z mapą 

        if self.__Mapa[index] == 0:    #Sprawdza czy można po tym chodzić
            return False        # :( nie można

        index = self.__offset(point + 19)  # sprawdza, czy dolny prawy punkt duszka/pacmana mieści się w polu

        if self.__Mapa[index] == 0:
            return False            #znowu się nie da :(

        return point.x % 20 == 0 or point.y % 20 == 0   # sprawdza, czy obiekt znajduje się na siatce 20x20


    # rysowanie mapy
    def __world(self):
        bgcolor("black")    #kolor czarny dla wszystkiego innego 
        self.__path.color("blue")  #kolor niebieski dla drogi po której można chodzić

        for index in range(len(self.__Mapa)): # przechodzi po każdej z pól na mapie
            tile = self.__Mapa[index] #i podpisuje pod siebie

            if tile > 0: #jeśli pole na mapie jest większe od 0 to zmienia
                x = (index % 20) * 20 - 200 # odkrycie pól x
                y = 180 - (index // 20) * 20 # odkrycie pól y
                self.__square(x, y) #rysowanie x,y

                if tile == 1: # jeśli pole na mapie = 1 to rysuje kropki białe
                    self.__path.up() # zółw podnosi ołówek.
                    self.__path.goto(x + 10, y + 10)  # przechodzi zółwik do środka pola
                    self.__path.dot(3, "white") #rysuje białą 2pikselową kropke


    # ruch
    def __move(self):
        self.__writer.undo()   # cofa ostatni rysunek żółwia piszącego (wynik)
        self.__writer.write(self.__state["score"]) #rysuje wynik
        clear() #usuwa wszystkie nie wcześniejsze linie

        if self.__valid(self.__pacman + self.__aim):
            self.__pacman.move(self.__aim) 

        index = self.__offset(self.__pacman) # oblicza numer z tablicy mapy

        if self.__Mapa[index] == 1:              # jeżeli pacman jest po raz pierwszy na polu, to...
            self.__Mapa[index] = 2           
            self.__state["score"] += 1           # zwiększ wynik
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            self.__square(x, y)                  # i skasuj kropeczkę

        up()                              # żółw podnosi żółtą kredkę
        goto(self.__pacman.x + 10, self.__pacman.y + 10)
        dot(20, "yellow")

        for point, course in self.__ghosts:
            if self.__valid(point + course):
                point.move(course)
            else:
                options = [
                    vector(5, 0),
                    vector(-5, 0),
                    vector(0, 5),
                    vector(0, -5),
                ]
                plan = choice(options)

                # while not valid(point+plan): # optymalizacja ruchu 
                #     plan = choice(options)

                course.x = plan.x
                course.y = plan.y

            up()
            goto(point.x + 10, point.y + 10)
            dot(20, "red")

        update()           # ?
        for point, course in self.__ghosts:     
            if abs(self.__pacman - point) < 20: #sprawdza czy duszek dotknął pacmana
                return

        ontimer(self.__move, 20)   


    # zmiana Ruch pm
    def __change(self,x, y):
        if self.__valid(self.__pacman + vector(x, y)): # jeżeli wykonywany ruch jest "valid", to 
            self.__aim.x = x   # zmień właściwość X wektora ruchu
            self.__aim.y = y   # zmień właściwość Y wektora ruchu

    def start(self):
        if self.__path == None:
            self.__path = Turtle(visible=False)     # zółw rysujący grafikę
        if self.__writer == None:
            self.__writer = Turtle(visible=False)   # żółw rysujący aktualny wynik

        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        self.__writer.goto(160, 160)
        self.__writer.color("white")
        self.__writer.write(self.__state["score"])
        listen() # uruchamia odczytywanie klawiszy
        onkey(lambda: self.__change(5, 0), "Right")
        onkey(lambda: self.__change(-5, 0), "Left")
        onkey(lambda: self.__change(0, 5), "Up")
        onkey(lambda: self.__change(0, -5), "Down")
        self.__world() #rysuje mapę
        self.__move() 
        done()

print("="*20,"STARTOWANIE GRY","="*20)
pac = Pacman()
pac.start()