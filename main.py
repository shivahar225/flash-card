from tkinter import *
import random
import pandas


BACKGROUND_GROUND = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data  = pandas.read_csv("data.txt")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="telugu",fill="black")
    canvas.itemconfig(card_word,text=current_card["telugu"],fill="black")
   # canvas.itemconfig(card_background,image=card_front_img)
    flip_timer=window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="english",fill="white")
    canvas.itemconfig(card_word, text=current_card["english"],fill="white")
    #canvas.itemconfig(card_background,image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)

    next_card()

window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_GROUND)

flip_timer=window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)


#card_front_img = PhotoImage(file="image/card_front.png")
#card_back_img = PhotoImage(file="images/card_back.png")
#card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("ariel",40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("ariel",40, "italic"))
canvas.config(bg=BACKGROUND_GROUND, highlightthickness=0)
canvas.grid(row=0, column=0)

#cross_image = PhotoImage(file="image/wrong.png")
unknown_button = Button(highlightthickness=0,command=next_card,text="√",font=30)
unknown_button.grid(row=1, column=0)

#check_image = PhotoImage(file="image/right.png")
known_button = Button(highlightthickness=0,command=is_known,text="*",font=30)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
