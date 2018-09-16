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

age_label = Label(window, text="Age")
age_label.grid(row=1, column=2)

stable_label = Label(window, text="Stable")
stable_label.grid(row=2, column=0)

height_label = Label(window, text="Height")
height_label.grid(row=0, column=4)

weight_label = Label(window, text="Weight")
weight_label.grid(row=1, column=4)

name_text = StringVar()
name_entry = Entry(window, textvariable=name_text)
name_entry.grid(row=0, column=1)

nick_name_text = StringVar()
nick_name_entry = Entry(window, textvariable=nick_name_text)
nick_name_entry.grid(row=0, column=3)

rank_text = StringVar()
rank_entry = Entry(window, textvariable=rank_text)
rank_entry.grid(row=1, column=1)

stable_text = StringVar()
stable_entry = Entry(window, textvariable=stable_text)
stable_entry.grid(row=2, column=1)

age_text = StringVar()
age_entry = Entry(window, textvariable=age_text)
age_entry.grid(row=1, column=3)

height_text = StringVar()
height_entry = Entry(window, textvariable=height_text)
height_entry.grid(row=0, column=5)

weight_text = StringVar()
weight_entry = Entry(window, textvariable=weight_text)
weight_entry.grid(row=1, column=5)


window.mainloop()
