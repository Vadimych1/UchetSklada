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
# import tkinter as tk
import http.server as hts

# module for parsing query
import urllib.parse as up

def create_product_table(cur: sqlite3.Cursor, name: str, displayName: str, desc: str) -> None:
    global tables

    try:
        cur.execute(f"""CREATE TABLE {name} (\
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, \
                    name TEXT NOT NULL, \
                    count INTEGER NOT NULL, \
                    cost INTEGER NOT NULL, \
                    status TEXT, \
                    date DATETIME)""")
        with open("tables.json", "r") as f:
            t = json.load(f)

        with open("tables.json", "w") as f:
            t.append({"name": name, "displayName": displayName, "description": desc})
            json.dump(t, f)

        tables = t
    except Exception as e:
        print(e)
    
def init_tables(cur: sqlite3.Cursor, tables: list) -> None:
    for table in tables:
        cur.execute(f"CREATE TABLE IF NOT EXISTS {table["name"]} (id TEXT NOT NULL, name TEXT NOT NULL, count INTEGER NOT NULL, cost INTEGER NOT NULL, status TEXT, date DATETIME)")

def fetch_from_product_tables(cur: sqlite3.Cursor, tableName: str, count: int | None = None) -> list:
    if count == None:
        cur.execute(f"SELECT * FROM {tableName}")
    else:
        cur.execute(f"SELECT * FROM {tableName, count} LIMIT %i")

    return cur.fetchall()

# ! Connect to database
con = sqlite3.connect("database/db.db")
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

# ! Run http server
class Handler(hts.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        
        url = up.urlparse(self.path)

        query = up.parse_qs(url.query)
        path = url.path

        print(path)

        try:
            if path == "/":
                self.wfile.write("<h1>Method not found</h1>".encode())
                return
            elif path == "/get_table_info":
                self.wfile.write(json.dumps(fetch_from_product_tables(cur, query["tableName"])).encode())
                return
            elif path == "/get_tables":
                self.wfile.write(json.dumps(tables).encode())
                return
            elif path == "/delete_table":
                cur.execute(f"DROP TABLE {query['name'][0]}")
                # remove from tables
                for i in tables:
                    if i["name"] == query["name"][0]:
                        tables.remove(i)
                        break

                with open("tables.json", "w") as f:
                    json.dump(tables, f)
                    
                return
            elif path == "/create_table":
                create_product_table(cur, query["name"][0], query["displayName"][0], query["description"][0])
                return
        except:
            self.wfile.write("ERR".encode())
            return
        
        self.wfile.write("<h1>Method not found</h1>".encode())

httpd = hts.HTTPServer(("127.0.0.1", 8000), Handler)
httpd.serve_forever()