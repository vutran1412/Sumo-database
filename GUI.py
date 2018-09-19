from tkinter import *
from tkinter import ttk
from DB import DB
from PIL import *



class GUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Sumo Wrestlers")

        frame = LabelFrame(self.window, text="Add new wrestler")
        frame.grid(row=0, column=0)

        Label(frame, text="Name:").grid(row=1, column=1)
        self.name = Entry(frame)
        self.name.grid(row=1, column=2)

        Label(frame, text="Nick Name:").grid(row=2, column=1)
        self.nick_name = Entry(frame)
        self.nick_name.grid(row=2, column=2)

        Label(frame, text="Age:").grid(row=3, column=1)
        self.age = Entry(frame)
        self.age.grid(row=3, column=2)

        Label(frame, text="Rank:").grid(row=4, column=1)
        self.rank = Entry(frame)
        self.rank.grid(row=4, column=2)

        Label(frame, text="Stable:").grid(row=5, column=1)
        self.stable = Entry(frame)
        self.stable.grid(row=5, column=2)

        Label(frame, text="Height (cm):").grid(row=6, column=1)
        self.height = Entry(frame)
        self.height.grid(row=6, column=2)

        Label(frame, text="Weight (kg):").grid(row=7, column=1)
        self.weight = Entry(frame)
        self.weight.grid(row=7, column=2)

        Label(frame, text="Record (W-L):").grid(row=8, column=1)
        self.record = Entry(frame)
        self.record.grid(row=8, column=2)

        self.treeview = ttk.Treeview(window)
        self.treeview["columns"] = ("Name", "Nick Name", "Age", "Rank", "Stable", "Height", "Weight", "Record")
        self.treeview.heading("#0", text="id", anchor=W)
        self.treeview.column("#0", stretch=NO, anchor=W, width=50)
        self.treeview.heading("Name", text="Name")
        self.treeview.column("Name", stretch=YES, anchor=CENTER, width=80)
        self.treeview.heading("Nick Name", text="Nick Name")
        self.treeview.column("Nick Name", stretch=YES, anchor=CENTER, width=80)
        self.treeview.heading("Age", text="Age")
        self.treeview.column("Age", stretch=NO, anchor=CENTER, width=30)
        self.treeview.heading("Rank", text="Rank")
        self.treeview.column("Rank", stretch=YES, anchor=CENTER, width=50)
        self.treeview.heading("Stable", text="Stable")
        self.treeview.column("Stable", stretch=YES, anchor=CENTER, width=50)
        self.treeview.heading("Height", text="Height")
        self.treeview.column("Height", stretch=NO, anchor=CENTER, width=50)
        self.treeview.heading("Weight", text="Weight")
        self.treeview.column("Weight", stretch=NO, anchor=CENTER, width=50)
        self.treeview.heading("Record", text="Record (W-L)")
        self.treeview.column("Record", stretch=NO, anchor=CENTER, width=80)
        self.treeview.grid(row=1, column=0, columnspan=6, padx=5, pady=5)
        self.treeview = self.treeview

        btn_add = ttk.Button(frame, text="Add wrestler", command=self.adding)
        btn_add.grid(row=9, column=2)
        self.message = Label(text="", fg="red")
        self.message.grid(row=9, column=0)

        btn_edit = ttk.Button(text="Edit wrestler")
        btn_edit.grid(row=9, column=2)
        self.message = Label(text="", fg="red")
        self.message.grid(row=9, column=0)

        btn_delete = ttk.Button(text="Delete Wrestler", command=self.deleting)
        btn_delete.grid(row=9, column=3)
        self.message = Label(text="", fg="red")
        self.message.grid(row=9, column=0)
        self.view_all()

    def validation(self):
        return len(self.name.get()) != 0 and len(self.nick_name.get()) != 0 and \
               len(self.age.get()) != 0 and len(self.rank.get()) != 0 and \
               len(self.stable.get()) != 0 and len(self.height.get()) != 0 and \
               len(self.weight.get()) != 0 and len(self.record.get()) != 0

    def view_all(self):
        db =DB()
        records = self.treeview.get_children()
        for i in records:
            self.treeview.delete(i)
        db_row = db.wrestlers()
        for row in db_row:
            self.treeview.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5],
                                                             row[6], row[7], row[8]))

    def adding(self):
        db = DB()
        if self.validation():
            name = self.name.get()
            nick_name = self.nick_name.get()
            age = self.age.get()
            rank = self.rank.get()
            stable = self.stable.get()
            height = self.height.get()
            weight = self.weight.get()
            record = self.record.get()
            db.insert(name, nick_name, age, rank, stable, height, weight, record)
            self.message["text"] = "Wrestler {} added".format(name)
            self.name.delete(0, END)
            self.nick_name.delete(0, END)
            self.age.delete(0, END)
            self.rank.delete(0, END)
            self.stable.delete(0, END)
            self.height.delete(0, END)
            self.weight.delete(0, END)
            self.record.delete(0, END)
        else:
            self.message["text"] = "All fields must be filled out"
        self.view_all()

    def deleting(self):
        db = DB()
        self.message["text"] = ""
        try:
            self.treeview.item(self.treeview.selection())["values"][0]
        except IndexError as e:
            self.message["text"] = "Select Wrestler to delete"
            return e
        self.message["text"] = ""
        id = self.treeview.item(self.treeview.selection())["text"]
        db.delete(id)
        self.view_all()


