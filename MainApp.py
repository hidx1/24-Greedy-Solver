from kivy.animation import Animation
from kivy.app import App
#from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from random import randint

Builder.load_string('''
#:kivy 1.0.9
#:import Clock kivy.clock.Clock
<MainScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "asset/background.jpg"

    FloatLayout:

        #UPPER LAYOUT
        FloatLayout:
            size_hint_y: 1/3

            Image:
                id: hide1
                pos_hint: {"right": 0.89, 'top': 2.9}
                size_hint: (0.8, 0.6)
                source: "asset/card_background.png"

            Image:
                id: hide2
                pos_hint: {"right": 0.892, 'top': 2.9}
                size_hint: (0.8, 0.6)
                source: "asset/card_background.png"

            Image:
                id: hide3
                pos_hint: {"right": 0.894, 'top': 2.9}
                size_hint: (0.8, 0.6)
                source: "asset/card_background.png"

            Image:
                id: hide4
                pos_hint: {"right": 0.896, 'top': 2.9}
                size_hint: (0.8, 0.6)
                source: "asset/card_background.png"

            Image:
                id: move1
                pos_hint: {"right": 0.89, 'top': 2.9}
                size_hint: (0.8, 0.6)
                source: "asset/card_background.png"

            Image:
                id: move2
                pos_hint: {"right": 0.892, 'top': 2.9}
                size_hint: (0.8, 0.6)
                source: "asset/card_background.png"

            Image:
                id: move3
                pos_hint: {"right": 0.894, 'top': 2.9}
                size_hint: (0.8, 0.6)
                source: "asset/card_background.png"

            Image:
                id: move4
                pos_hint: {"right": 0.896, 'top': 2.9}
                size_hint: (0.8, 0.6)
                source: "asset/card_background.png"

            Button:
                size_hint: (.24, .2)
                pos_hint: {"right": 0.95, "top": 2.9}
                text: "Randomize"
                font_size: 0.05 * root.height
                background_normal: ''
                background_color: 66/255, 134/255, 244/255, 0.2
                on_release: root.animate_image(), Clock.schedule_once(root.update, .3)

                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    Line:
                        width: 1
                        rectangle: self.x, self.y, self.width, self.height

            Button:
                size_hint: (.15, .2)
                pos_hint: {"right": 0.95, "top": 2.65}
                text: "Reset"
                font_size: 0.05 * root.height
                background_normal: ''
                background_color: 66/255, 134/255, 244/255, 0.2
                on_release: root.reset()
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    Line:
                        width: 1
                        rectangle: self.x, self.y, self.width, self.height

            Button:
                size_hint: (.08, .2)
                pos_hint: {"right": 0.95, "top": 2.4}
                text: "Exit"
                font_size: 0.05 * root.height
                background_normal: ''
                background_color: 66/255, 134/255, 244/255, 0.2
                on_release: app.stop()
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    Line:
                        width: 1
                        rectangle: self.x, self.y, self.width, self.height

        #MIDDLE LAYOUT
        FloatLayout:
            size_hint_y: 1/3

            Image:
                id: field1
                pos_hint: {"right": 0.6, 'top': 1.8}
                size_hint: (0, 0)
                source: root.card_1

            Image:
                id: field2
                pos_hint: {"right": 0.8, 'top': 1.8}
                size_hint: (0, 0)
                source: root.card_2
            Image:
                id: field3
                pos_hint: {"right": 1.0, 'top': 1.8}
                size_hint: (0, 0)
                source: root.card_3
            Image:
                id: field4
                pos_hint: {"right": 1.2, 'top': 1.8}
                size_hint: (0, 0)
                source: root.card_4

        #BOTTOM LAYOUT
        FloatLayout:
            size_hint_y: 1/3
            Label:
                text: "Cards remaining: " + str(root.cards_remaining)
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                font_size: 30
                pos_hint: {"x": 0.04, 'y': 0.35}

            Label:
                text: "Answer                 : " + root.answer
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                font_size: 30
                pos_hint: {"x": 0.038, 'y': 0.175}
            Label:
                text: "Point                     : " + str(root.point)
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                font_size: 30
                pos_hint: {"x": 0.04, 'y': -0.025}

'''
)

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
    def hide_deck(self): #Hide deck (cards on middle top)
        self.ids.hide1.size_hint = (0, 0)
        self.ids.hide2.size_hint = (0, 0)
        self.ids.hide3.size_hint = (0, 0)
        self.ids.hide4.size_hint = (0, 0)
    def hide_card(self): #Hide the 4 cards in the middle
        self.ids.field1.size_hint = (0, 0)
        self.ids.field2.size_hint = (0, 0)
        self.ids.field3.size_hint = (0, 0)
        self.ids.field4.size_hint = (0, 0)
    def show_deck(self): #Show deck (cards on middle top)
        self.ids.hide1.size_hint = (0.8, 0.6)
        self.ids.hide2.size_hint = (0.8, 0.6)
        self.ids.hide3.size_hint = (0.8, 0.6)
        self.ids.hide4.size_hint = (0.8, 0.6)
    def show_card(self): #Show the 4 cards in the middle
        self.ids.field1.size_hint = (0.8, 0.6)
        self.ids.field2.size_hint = (0.8, 0.6)
        self.ids.field3.size_hint = (0.8, 0.6)
        self.ids.field4.size_hint = (0.8, 0.6)
    def animate_image(self): #Cards animation
        self.hide_card()
        anim = Animation(pos_hint={"right": 0.6, 'top': 1.8}, duration = .2)
        anim.start(self.ids["move1"])
        anim = Animation(pos_hint={"right": 0.8, 'top': 1.8}, duration = .2)
        anim.start(self.ids["move2"])
        anim = Animation(pos_hint={"right": 1, 'top': 1.8}, duration = .2)
        anim.start(self.ids["move3"])
        anim = Animation(pos_hint={"right": 1.2, 'top': 1.8}, duration = .2)
        anim.start(self.ids["move4"])
    def reset_moving_cards(self): #Reset position for the moving cards animation
        self.ids.move1.pos_hint = {"right": 0.89, 'top': 2.9}
        self.ids.move2.pos_hint = {"right": 0.892, 'top': 2.9}
        self.ids.move3.pos_hint = {"right": 0.894, 'top': 2.9}
        self.ids.move4.pos_hint = {"right": 0.896, 'top': 2.9}

    deck = [None] * 52 #Initialization of list with size 52

    def reset_deck(self):
        sym_num = 0
        for i in range(52):
            if (i % 13 == 0):
                sym_num += 1
            self.deck[i] = Cards(((i % 13) + 1), symbol_switch(sym_num))

    card_1 = StringProperty("asset/card_background.png")
    card_2 = StringProperty("asset/card_background.png")
    card_3 = StringProperty("asset/card_background.png")
    card_4 = StringProperty("asset/card_background.png")
    cards = [None] * 4
    #List Initialization
    for i in range(4):
        cards[i] = Cards(1, "H")

    answer = StringProperty("")
    point = NumericProperty(0)
    cards_remaining = NumericProperty(52)
    first = True

    def reset(self):
        self.show_deck()
        self.card_1 = "asset/card_background.png"
        self.card_2 = "asset/card_background.png"
        self.card_3 = "asset/card_background.png"
        self.card_4 = "asset/card_background.png"
        self.deck = [None] * 52
        self.reset_deck()
        self.answer = ""
        self.point = 0
        self.cards_remaining = len(self.deck)

    def update(self, instance):
        self.reset_moving_cards()
        if (self.cards_remaining == 0):
            self.reset()
        else:
            #Pemanggilan Inisialisasi deck pertama kali
            if (self.first):
                self.reset()
                self.first = False

            #Hide Cards
            self.show_card()
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
            if (self.cards_remaining == 4):
                self.hide_deck()

class MainApp(App):

    def build(self):
        start = MainScreen()
        return start

if __name__ == '__main__':
    #Window.fullscreen = 'auto'
    MainApp().run()
