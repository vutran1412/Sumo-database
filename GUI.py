from tkinter import *
from DB import *
from tkinter import messagebox


wrestler_db = DB()
window = Tk()
window.title("Sumo Wrestler Database")


def on_closing():
    dd = wrestler_db
    if messagebox.askokcancel("Exit", "Do you want to quit?"):
        window.destroy()
        del dd


window.protocol("WM_DELETE_WINDOW", on_closing)


name_label = Label(window, text="Name")
name_label.grid(row=0, column=0)

nick_name_label = Label(window, text="Nick Name")
nick_name_label.grid(row=0, column=2)

rank_label = Label(window, text="Rank")
rank_label.grid(row=1, column=0)



window.mainloop()