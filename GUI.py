# Sumo database
# Author: Vu Tran
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DB import DB


# GUI class sets up the GUI window and components
class GUI:

    # Constructor, sets up the data entry form and the Treeview to display the database
    def __init__(self, window):
        self.window = window
        self.window.title("Sumo Wrestler Database")

        # Sets up the frame to contain all the data entry textboxes and labels
        frame = LabelFrame(self.window, text="Add new wrestler")
        frame.grid(row=0, column=0)

        # Sets up the Treeview frame to contain the treeview
        tree_frame = Frame(self.window)
        tree_frame.grid(row=1, column=0)

        # Sets up the labels and textboxes in their specific spots on the grid inside the frame
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

        Label(frame, text="Stable:").grid(row=1, column=3)
        self.stable = Entry(frame)
        self.stable.grid(row=1, column=4)

        Label(frame, text="Height (cm):").grid(row=2, column=3)
        self.height = Entry(frame)
        self.height.grid(row=2, column=4)

        Label(frame, text="Weight (kg):").grid(row=3, column=3)
        self.weight = Entry(frame)
        self.weight.grid(row=3, column=4)

        Label(frame, text="Record (W-L):").grid(row=4, column=3)
        self.record = Entry(frame)
        self.record.grid(row=4, column=4)

        # Sets up the Treeview's columns and headings
        self.treeview = ttk.Treeview(tree_frame)
        # Column's headings stored as a tuple
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
        self.treeview.column("Rank", stretch=YES, anchor=CENTER, width=80)
        self.treeview.heading("Stable", text="Stable")
        self.treeview.column("Stable", stretch=YES, anchor=CENTER, width=80)
        self.treeview.heading("Height", text="Height")
        self.treeview.column("Height", stretch=NO, anchor=CENTER, width=50)
        self.treeview.heading("Weight", text="Weight")
        self.treeview.column("Weight", stretch=NO, anchor=CENTER, width=50)
        self.treeview.heading("Record", text="Record (W-L)")
        self.treeview.column("Record", stretch=NO, anchor=CENTER, width=80)
        self.treeview.grid(row=2, column=0, columnspan=6, padx=5, pady=5)
        self.treeview = self.treeview

        # Sets up the Treeview's vertical scrollbar
        self.scrollbar_vertical = ttk.Scrollbar(self.treeview, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar_vertical.set)

        # Sets up the Buttons and events, this button will add new data to the database
        btn_add = ttk.Button(frame, text="Add wrestler", command=self.adding)
        # Places the button at the specific location on the grid
        btn_add.grid(row=9, column=2)
        # Sets up the location and color of the text message that will be displayed to user
        self.message = Label(text="", fg="red")
        self.message.grid(row=9, column=0)
        # Button to edit existing record on the database
        btn_edit = ttk.Button(tree_frame, text="Edit wrestler", command=self.editing)
        btn_edit.grid(row=9, column=2)
        self.message = Label(text="", fg="red")
        self.message.grid(row=9, column=0)
        # Button to delete an existing record on the database
        btn_delete = ttk.Button(tree_frame, text="Delete Wrestler", command=self.deleting)
        btn_delete.grid(row=9, column=3)
        self.message = Label(text="", fg="red")
        self.message.grid(row=9, column=0)

        # Displays all the database data in the Treeview
        self.view_all()

    # Function to validate all user inputs
    def validation(self):
        return len(self.name.get()) != 0 and len(self.nick_name.get()) != 0 and \
               len(self.age.get()) != 0 and len(self.rank.get()) != 0 and \
               len(self.stable.get()) != 0 and len(self.height.get()) != 0 and \
               len(self.weight.get()) != 0 and len(self.record.get()) != 0

    # Function populates the Treeview with all the data in the database
    def view_all(self):
        # Create a database object
        db = DB()
        # Retrieves all the current records and delete them. This allows the program to update the records in real time
        records = self.treeview.get_children()
        for i in records:
            self.treeview.delete(i)
        # Query the database and retrieve all the rows from the table
        db_row = db.wrestlers()
        # Loop through the rows and insert the records on each new line at the end of the treeview, there are
        # 8 columns in each record
        for row in db_row:
            self.treeview.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5],
                                                             row[6], row[7], row[8]))

    # Function to add new data
    def adding(self):
        # Create a database object
        db = DB()
        # Validation check for all the textboxes, will not allow user to continue if missing fields or invalid
        # data types
        try:
            if self.validation():
                # Retrieves user input from textboxes
                name = self.name.get()
                nick_name = self.nick_name.get()
                age = self.age.get()
                rank = self.rank.get()
                stable = self.stable.get()
                height = self.height.get()
                weight = self.weight.get()
                record = self.record.get()
                if age.isdigit() is False or height.isdigit() is False or weight.isdigit() is False:
                    raise Exception("age, height, and weight must be numerals")
                # Insert the new data into the database
                db.insert(name, nick_name, age, rank, stable, height, weight, record)
                # Message to confirm the change
                self.message["text"] = "Wrestler {} added".format(name)
                # Clear all the values from the textbox
                self.name.delete(0, END)
                self.nick_name.delete(0, END)
                self.age.delete(0, END)
                self.rank.delete(0, END)
                self.stable.delete(0, END)
                self.height.delete(0, END)
                self.weight.delete(0, END)
                self.record.delete(0, END)
            # Message to show user if validation failed
            else:
                self.message["text"] = "All fields must be filled out!"
        except Exception as e:
            self.message["text"] = e
        self.view_all()

    # Function to delete a row
    def deleting(self):
        # Create a DB object
        db = DB()
        # Initialize an empty message
        self.message["text"] = ""
        # The user must select a row to delete
        try:
            self.treeview.item(self.treeview.selection())["values"][0]
        except IndexError as e:
            # Message to display if user clicks the delete button without selecting a row to delete first
            self.message["text"] = "Select Wrestler to delete"
            return e

        # Since deleting a record from the database is permanent, check with user before deleting
        choice = "Delete"
        confirmed = self.confirm(choice)
        # If user confirms delete row from data base and update the Treeview
        if confirmed:
            self.message["text"] = ""
            id = self.treeview.item(self.treeview.selection())["text"]
            db.delete(id)
        # Show the updated database
        self.view_all()

    # Function used to confirm user inputs that result in lasting changes to the database,
    # This function will probably be reused in the editing window, version 2.0 maybe
    def confirm(self, choice):
        # Messagebox that prompts the user to confirm choice
        ok = messagebox.askyesnocancel("Are you sure you want to {}?".format(choice))
        # If user confirms then return true
        if ok == YES:
            return True

    # Function used to edit selected rows in the database
    def editing(self):
        self.message["text"] = ""
        # Try block to catch index error, user must select a row to edit or warning message will display
        try:
            self.treeview.item(self.treeview.selection())["values"][0]
        except IndexError as e:
            self.message["text"] = "Select Wrestler to edit"
            return e

        # Assign old values to display in the new edit window
        id = self.treeview.item(self.treeview.selection())["text"]
        old_name = self.treeview.item(self.treeview.selection())["values"][0]
        old_nickname = self.treeview.item(self.treeview.selection())["values"][1]
        old_age = self.treeview.item(self.treeview.selection())["values"][2]
        old_rank = self.treeview.item(self.treeview.selection())["values"][3]
        old_stable = self.treeview.item(self.treeview.selection())["values"][4]
        old_height = self.treeview.item(self.treeview.selection())["values"][5]
        old_weight = self.treeview.item(self.treeview.selection())["values"][6]
        old_record = self.treeview.item(self.treeview.selection())["values"][7]

        # Instantiate new edit window
        self.edit_window = Toplevel()
        self.edit_window.title("Edit Wrestler")

        # Set up frames to contain all the widgets
        old_frame = LabelFrame(self.edit_window, text="Old Data")
        old_frame.grid(row=0, column=0)

        new_frame = LabelFrame(self.edit_window, text="New Data")
        new_frame.grid(row=1, column=0)

        button_frame = Label(self.edit_window)
        button_frame.grid(row=2, column=0)

        # Set up the labels in the new edit window
        Label(old_frame, text="Name:").grid(row=0, column=1)
        # Display all the old data in read only text boxes
        Entry(old_frame, textvariable=StringVar(self.edit_window, value=old_name),
              state="readonly").grid(row=0, column=2)
        Label(old_frame, text="Nick Name:").grid(row=1, column=1)
        Entry(old_frame, textvariable=StringVar(self.edit_window, value=old_nickname),
              state="readonly").grid(row=1, column=2)
        Label(old_frame, text="Age:").grid(row=2, column=1)
        Entry(old_frame, textvariable=StringVar(self.edit_window, value=old_age),
              state="readonly").grid(row=2, column=2)
        Label(old_frame, text="Rank:").grid(row=3, column=1)
        Entry(old_frame, textvariable=StringVar(self.edit_window, value=old_rank),
              state="readonly").grid(row=3, column=2)
        Label(old_frame, text="Stable:").grid(row=0, column=3)
        Entry(old_frame, textvariable=StringVar(self.edit_window, value=old_stable),
              state="readonly").grid(row=0, column=4)
        Label(old_frame, text="Height:").grid(row=1, column=3)
        Entry(old_frame, textvariable=StringVar(self.edit_window, value=old_height),
              state="readonly").grid(row=1, column=4)
        Label(old_frame, text="Weight:").grid(row=2, column=3)
        Entry(old_frame, textvariable=StringVar(self.edit_window, value=old_weight),
              state="readonly").grid(row=2, column=4)
        Label(old_frame, text="Record:").grid(row=3, column=3)
        Entry(old_frame, textvariable=StringVar(self.edit_window, value=old_record),
              state="readonly").grid(row=3, column=4)

        # The new frame will display all the textboxes that will take user input
        # Sets up the labels
        Label(new_frame, text="Name:").grid(row=0, column=1)
        # Sets up the textbox
        new_name_txt = Entry(new_frame)
        new_name_txt.grid(row=0, column=2)
        Label(new_frame, text="Nick Name:").grid(row=1, column=1)
        new_nick_name_txt = Entry(new_frame)
        new_nick_name_txt.grid(row=1, column=2)
        Label(new_frame, text="Age:").grid(row=2, column=1)
        new_age_txt = Entry(new_frame)
        new_age_txt.grid(row=2, column=2)
        Label(new_frame, text="Rank:").grid(row=3, column=1)
        new_rank_txt = Entry(new_frame)
        new_rank_txt.grid(row=3, column=2)
        Label(new_frame, text="Stable:").grid(row=0, column=3)
        new_stable_txt = Entry(new_frame)
        new_stable_txt.grid(row=0, column=4)
        Label(new_frame, text="Height:").grid(row=1, column=3)
        new_height_txt = Entry(new_frame)
        new_height_txt.grid(row=1, column=4)
        Label(new_frame, text="Weight:").grid(row=2, column=3)
        new_weight_txt = Entry(new_frame)
        new_weight_txt.grid(row=2, column=4)
        Label(new_frame, text="Record:").grid(row=3, column=3)
        new_record_txt = Entry(new_frame)
        new_record_txt.grid(row=3, column=4)

        # Passing the function object via lambda expression to the button command handler
        # https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/
        btn_save_change = Button(button_frame,
                                 text="Save Wrestler", width=10,
                                 command=lambda: self.update_wrestler(new_name_txt.get(), new_nick_name_txt.get(),
                                                                      new_age_txt.get(), new_rank_txt.get(),
                                                                      new_stable_txt.get(), new_height_txt.get(),
                                                                      new_weight_txt.get(), new_record_txt.get(), id))
        #
        btn_save_change.grid(row=0, column=0, sticky=W)

        # Infinite loop to keep the edit window open
        self.edit_window.mainloop()

    # Function to update the database
    def update_wrestler(self, new_name, new_nick_name, new_age, new_rank, new_stable, new_height, new_weight, new_record, id):
        # Create the database object
        db = DB()
        # Update the database with new values
        db.update(new_name, new_nick_name, new_age, new_rank, new_stable, new_height, new_weight, new_record, id)
        # close the edit window
        self.edit_window.destroy()
        # Confirmation message to display in the main window
        self.message["text"] = "{} record changed".format(new_name)
        # display the database table
        self.view_all()

    # Search function to be implemented
    def search_wrestler(self):
        # TODO // Create a new window called search window
        # TODO // In the window create a combobox to allow user to select a search condiditon
        # TODO // Create a function to display only the items found in the search into the Treeview
        pass
