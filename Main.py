# Sumo-database
# Author: Vu Tran
""" This is a GUI database management application to store Sumo wrestlers information """
from tkinter import *
from GUI import GUI

# Main function to run the application
def main():
    window = Tk()
    application = GUI(window)
    window.mainloop()


if __name__ == "__main__":
    main()
