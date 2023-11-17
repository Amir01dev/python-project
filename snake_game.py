from tkinter import *

# ----------variables game-------------
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_WIDTH = 30
SNAKE_COLOR = "yellow"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"
score = 0

# ----------GUI Game-------------
window = Tk()

window.title("Snake Game")

window.resizable(False, False)

label = Label(window, text=f"Score: {score}", font=("Courier", 30))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

window.mainloop()
