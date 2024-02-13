import sqlite3

# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
# cursor.execute('''
# CREATE TABLE Warehouse (
# id INTEGER PRIMARY KEY,
# name of the item TEXT NOT NULL,
# quantity TEXT NOT NULL,
# purchase price TEXT NOT NULL,
# provider TEXT NOT NULL,
# the ability to change the payment status with an indication of the date TEXT NOT NULL
# )
# ''')
# connection.commit()
# connection.close()
# def update_database(set_name, value_name, where_name, table_name = "num", where_who = "id"):
#     cursor.execute(f"UPDATE {table_name} SET {set_name} = (?) WHERE {where_who} = (?)", (value_name, where_name))
#     sqlite3.connection.commit()
# update_database()
# con = sqlite3.connect("tutorial.db")
# cur = con.cursor()
# cur.execute("CREATE TABLE movie(title, year, score)")
# res = cur.execute("SELECT name FROM sqlite_master")
# res.fetchone()
# res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
# res.fetchone() is None
# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)
# con.commit()
# res = cur.execute("SELECT score FROM movie")
# res.fetchall()
# data = [
#     ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
#     ("Monty Python's The Meaning of Life", 1983, 7.5),
#     ("Monty Python's Life of Brian", 1979, 8.0),
# ]
# cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
# con.commit()
# for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
#     print(row)
# con = sqlite3.connect("tutorial.db")
# cur = con.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)
# con.commit()
# con.close()
# print(cur.execute("SELECT * FROM movie").fetchall())

import json
import tkinter as tk

def create_product_table(cur: sqlite3.Cursor, name: str, displayName: str, desc: str) -> None:
    global tables

    try:
        cur.execute("CREATE TABLE %s (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, name TEXT NOT NULL, count INTEGER NOT NULL, cost INTEGER NOT NULL, status TEXT, date DATETIME)".format(name))
        with open("tables.json") as f:
            t = json.load(f)

        with open("tables.json") as f:
            t.append({"name": name, "displayName": displayName, "description": desc})
            json.dump(t)

        tables = t
    except:
        pass
    
def init_tables(cur: sqlite3.Cursor, tables: list) -> None:
    for table in tables:
        cur.execute("CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, name TEXT NOT NULL, count INTEGER NOT NULL, cost INTEGER NOT NULL, status TEXT, date DATETIME)".format(table["name"]))

def fetch_from_product_tables(cur: sqlite3.Cursor, tableName: str, count: int | None = None) -> list:
    if count == None:
        cur.execute("SELECT * FROM %s".format(tableName))
    else:
        cur.execute("SELECT * FROM %s LIMIT %i".format(tableName, count))

    return cur.fetchall()

# ! Connect to database
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

# ! Read settings from JSON:
with open("settings.json", "r") as f:
    settings = json.load(f)

# ! Read database tables from JSON:
with open("tables.json", "r") as f:
    tables = json.load(f)

# ! Initialize tables
init_tables(cur, tables)
con.commit()

# ! Run window
window = tk.Tk("Учет склада")
window.geometry("{}x{}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))

tk.mainloop()

# cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)
# con.commit()
# print(cur.execute("SELECT * FROM movie").fetchall())