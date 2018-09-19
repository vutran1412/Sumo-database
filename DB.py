# Sumo database
# Author: Vu Tran
""" The DB class will be used by the Application to interact with the sqlite database.
The class has CRUD functionalityUpon object instantiation the database and table will be created"""
import sqlite3


class DB:
    # Constructor, creates database if none exist, otherwise connects to the existing database.
    # The table is also created if none exists
    def __init__(self):
        # Database connection
        self.conn = sqlite3.connect("stable_db.sqlite")
        # Creates the cursor object to execute SQL statements
        self.cursor = self.conn.cursor()
        # Creates the database table
        self.conn.execute("CREATE TABLE IF NOT EXISTS wrestlers (\
                          id INTEGER PRIMARY KEY, name TEXT, nick_name TEXT, age INTEGER, rank TEXT, stable TEXT, \
                           height REAL, weight REAL, record TEXT)")
        # Commit changes
        self.conn.commit()

    # Closes the connection when the object closes
    def __del__(self):
        self.conn.close()

    # Function to select all rows from the table
    def wrestlers(self):
        # Select * statement fetches all records from the table
        self.cursor.execute("SELECT * FROM wrestlers")
        rows = self.cursor.fetchall()
        # return rows
        return rows

    # Function to insert new values into the table
    def insert(self, name, nick_name, age, rank, stable, height, weight, record):
        # SQL statement to insert values, the id is the primary key and can be a null value
        self.cursor.execute("INSERT INTO wrestlers VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (name, nick_name, age, rank,
                                                                                       stable, height, weight, record))
        # Save all changes
        self.conn.commit()

    # Function to search the database for a specific record
    def search(self, name=""):
        self.cursor.execute("SELECT * FROM wrestler WHERE name=?", name)
        # Fetch all rows
        found_rows = self.cursor.fetchall()
        # Return rows
        return found_rows

    # Function to update values of an existing record in the database
    def update(self, name, nick_name, age, rank, stable, height, weight, record):
        # SQL statement to update
        self.cursor.execute("UPDATE wrestlers SET name=?, nick_name=?, age=?, rank=?,"
                            " stable=?, height=?, weight=?, record=?",
                            (name, nick_name, age, rank, stable, height, weight, record))
        self.conn.commit()

    # Function to delete a record
    def delete(self, id):
        # SQL statement to delete the record by id
        self.cursor.execute("DELETE FROM wrestlers WHERE id=?", (id,))
        # Saves all changes
        self.conn.commit()


