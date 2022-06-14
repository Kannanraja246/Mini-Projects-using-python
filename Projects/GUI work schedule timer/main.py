import math
import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.3
reps = 0
watch = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_on():
    global tick, watch, reps
    reps = 0
    window.after_cancel(watch)
    timer.config(text="Timer", font=(FONT_NAME, 25, "bold"), fg=RED)
    tick = ""
    tick_mark.config(text=tick)
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_count():
    global reps, tick
    reps += 1
    if reps % 8 == 0:
        timer.config(text="Break")
        count_down(round(LONG_BREAK_MIN * 60))
        # tick = "✔"
        # tick_mark.config(text=tick)
    elif reps % 2 == 0:
        timer.config(text="Short Break", fg="red")
        count_down(round(SHORT_BREAK_MIN * 60))
        # tick += "✔"
        # tick_mark.config(text=tick)
    else:
        timer.config(text="Work", fg="orange")
        count_down(round((WORK_MIN*60)))
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(from_nuber):
    global tick, watch
    minute = math.floor(from_nuber / 60)
    sec = from_nuber % 60
    if minute <= 9:
        minute = "0"+str(minute)
    if sec <= 9:
        sec = "0"+str(sec)
    canvas.itemconfig(timer_text, text=f"{minute}:{sec}")
    if from_nuber > 0:
        watch = window.after(1000, count_down, from_nuber-1)
    else:
        if reps % 2 != 0:
            tick += "✔"
        tick_mark.config(text=tick)
        start_count()

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro an Italian tomato")
window.minsize(500, 500)
window.config(padx=100, pady=100, bg=GREEN)

canvas = tkinter.Canvas(width=250, height=250, bg=GREEN, highlightthickness=0)
photo = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(125, 125, image=photo)
timer_text = canvas.create_text(125, 140, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(column=1, row=1)

timer = tkinter.Label()
timer.config(text="Timer", font=(FONT_NAME, 25, "bold"), fg=RED, bg=GREEN)
timer.grid(column=1, row=0)

start = tkinter.Button()
start.config(text="Start", command=start_count)
start.grid(column=0, row=2)

reset = tkinter.Button()
reset.config(text="Reset",  command=reset_on)
reset.grid(column=2, row=2)

tick = ""
tick_mark = tkinter.Label()
tick_mark.config(text=tick, font=(FONT_NAME, 10, "normal"), bg=GREEN)
tick_mark.grid(column=1, row=3)

window.mainloop()