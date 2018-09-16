import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect("stable_db.sqlite")
        self.cursor = self.conn.cursor()
        self.conn.execute("CREATE TABLE IF NOT EXISTS wrestlers (\
                          id INTEGER PRIMARY KEY, name TEXT, nick_name TEXT, rank TEXT, age INTEGER, stable TEXT, \
                           height REAL, weight REAL)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def wrestlers(self):
        self.cursor.execute("SELECT * FROM wrestlers")
        rows = self.cursor.fetchall()
        return rows

    def insert(self, name, nick_name, rank, age, stable, height, weight):
        self.cursor.execute("INSERT INTO books VALUES (NULL,? ,? ,? , ?, ?, ?, ?)", (name, nick_name, rank, age,
                                                                                   stable, height, weight))
        self.conn.commit()

    def search(self, name="", nick_name="", rank="", age="", stable="", height="", weight=""):
        self.cursor.execute("SELECT * FROM wrestler WHERE name=? OR nick_name=? OR rank=? OR age=? OR stable=? "
                          "OR height=? OR weight=?", (name, nick_name, rank, age, stable, height, weight))
        found_rows = self.cursor.fetchall()
        return found_rows

    def update(self, id, name, nick_name, rank, age, stable, height, weight):
        self.cursor.execute("UPDATE wrestlers SET name=?, nick_name=?, rank=?, age=?, stable=?, height=?, weight=?",
                            (name, nick_name, rank, age, stable, height, weight))

    def delete(self, id):
        self.cursor.execute("DELETE FROM wrestlers WHERE id=?", (id))
        self.conn.commit()
        self.view()

