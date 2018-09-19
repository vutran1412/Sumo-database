from tkinter import *
from tkinter import ttk
from DB import *
from GUI import GUI

def main():
    window = Tk()
    application = GUI(window)
    window.mainloop()


if __name__ == "__main__":
    main()