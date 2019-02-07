from os import system
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty
from random import randint


def symbol_switch(arg):
    if (arg == 1):
        return "H"
    elif (arg == 2):
        return "C"
    elif (arg == 3):
        return "D"
    else:
        return "S"

class Cards:
    def __init__(self, num, sym):
        self.num = num
        self.sym = sym

class MainScreen(FloatLayout):
    deck = [None] * 52
    sym_num = 0
    for i in range(52):
        if (i % 13 == 0):
            sym_num += 1
        deck[i] = Cards(((i % 13) + 1), symbol_switch(sym_num))
    card_1 = StringProperty("asset/card_background.png")
    card_2 = StringProperty("asset/card_background.png")
    card_3 = StringProperty("asset/card_background.png")
    card_4 = StringProperty("asset/card_background.png")
    cards = [None] * 4

    #Inisialisasi isi list
    for i in range(4):
        cards[i] = Cards(1, "H")

    answer = StringProperty("")
    point = NumericProperty(0)
    cards_remaining = NumericProperty(52)
    first = True

    def reset(self):
        self.ids.deck.size_hint = (0.8, 0.6)
        self.card_1 = "asset/card_background.png"
        self.card_2 = "asset/card_background.png"
        self.card_3 = "asset/card_background.png"
        self.card_4 = "asset/card_background.png"
        self.deck = [None] * 52
        self.sym_num = 0
        self.answer = ""
        self.point = 0
        for i in range(52):
            if (i % 13 == 0):
                self.sym_num += 1
            self.deck[i] = Cards(((i % 13) + 1), symbol_switch(self.sym_num))
        self.cards_remaining = len(self.deck)

    def update(self):
        if (self.cards_remaining == 4):
            self.ids.deck.size_hint = (0, 0)
        if (self.cards_remaining == 0):
            self.reset()
        else:
            #Inisialisasi deck pertama kali
            if (self.first):
                self.reset()
                self.first = False

            #First Number
            self.cards_remaining = len(self.deck)
            idx = randint(0,self.cards_remaining-1)
            self.cards[0].num = self.deck[idx].num
            self.cards[0].sym = self.deck[idx].sym
            del self.deck[idx]

            #Second Number
            self.cards_remaining = len(self.deck)
            idx = randint(0,self.cards_remaining-1)
            self.cards[1].num = self.deck[idx].num
            self.cards[1].sym = self.deck[idx].sym
            del self.deck[idx]

            #Third Number
            self.cards_remaining = len(self.deck)
            idx = randint(0,self.cards_remaining-1)
            self.cards[2].num = self.deck[idx].num
            self.cards[2].sym = self.deck[idx].sym
            del self.deck[idx]

            #Fourth Number
            self.cards_remaining = len(self.deck)
            idx = randint(0,self.cards_remaining-1)
            self.cards[3].num = self.deck[idx].num
            self.cards[3].sym = self.deck[idx].sym
            del self.deck[idx]

            self.cards_remaining = len(self.deck)
            self.card_1 = "asset/" + str(self.cards[0].num) + self.cards[0].sym + ".png"
            self.card_2 = "asset/" + str(self.cards[1].num) + self.cards[1].sym + ".png"
            self.card_3 = "asset/" + str(self.cards[2].num) + self.cards[2].sym + ".png"
            self.card_4 = "asset/" + str(self.cards[3].num) + self.cards[3].sym + ".png"
            self.answer = str(self.cards[0].num) + " + " + str(self.cards[1].num) + " + " + str(self.cards[2].num) + " + " + str(self.cards[3].num)
            self.point = randint(1,15)

class MainApp(App):
    def build(self):
        start = MainScreen()
        #start.RunningProgram()
        #Clock.schedule_interval(start.update, 1.0/60.0)
        return start

if __name__ == '__main__':
    system('cls')
    #Window.fullscreen = 'auto'
    MainApp().run()
