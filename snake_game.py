from tkinter import *
# -------------------------------------

class Snake:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []
        for i in range(0, BODY_SIZE):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = Canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)
def restart_button():
    pass
# ----------variables game-------------
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 30
BODY_SIZE = 2
SLOWNESS = 200
SNAKE_COLOR = "yellow"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"
score = 0
direction = "down"

# ----------GUI Game-------------
window = Tk()

window.title("Snake Game")

window.resizable(False, False)

label = Label(window, text=f"Score: {score}", font=("Courier", 30))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

restart = Button(window, text="Restart", fg="red", command=restart_button)
restart.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()
