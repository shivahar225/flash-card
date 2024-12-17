kinter import *
from tkinter import ttk

class app(Tk):


    def __init__(self):
        super().__init__()
        self.title()
        self.front_card_img = PhotoImage(file="image/card_front.png")
        self.card_back_img = PhotoImage(file="images/card_back.png")

        ttk.Label(self, image= self.front_card_img).pack()





mainloop()
