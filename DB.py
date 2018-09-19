import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect("stable_db.sqlite")
        self.cursor = self.conn.cursor()
        self.conn.execute("CREATE TABLE IF NOT EXISTS wrestlers (\
                          id INTEGER PRIMARY KEY, name TEXT, nick_name TEXT, age INTEGER, rank TEXT, stable TEXT, \
                           height REAL, weight REAL, record TEXT)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def wrestlers(self):
        self.cursor.execute("SELECT * FROM wrestlers")
        rows = self.cursor.fetchall()
        return rows

    def insert(self, name, nick_name, age, rank, stable, height, weight, record):
        self.cursor.execute("INSERT INTO wrestlers VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (name, nick_name, age, rank,
                                                                                       stable, height, weight, record))
        self.conn.commit()

    def search(self, name="", nick_name="", age="", rank="", stable="", height="", weight="", record=""):
        self.cursor.execute("SELECT * FROM wrestler WHERE name=? OR nick_name=? OR age=? OR rank=? OR stable=? "
                          "OR height=? OR weight=? OR record=?", (name, nick_name, age, rank,
                                                                  stable, height, weight, record))
        found_rows = self.cursor.fetchall()
        return found_rows

    def update(self, name, nick_name, age, rank, stable, height, weight, record):
        self.cursor.execute("UPDATE wrestlers SET name=?, nick_name=?, age=?, rank=?,"
                            " stable=?, height=?, weight=?, record=?",
                            (name, nick_name, rank, age, stable, height, weight, record))

    def delete(self, id):
        self.cursor.execute("DELETE FROM wrestlers WHERE id=?", (id,))
        self.conn.commit()


