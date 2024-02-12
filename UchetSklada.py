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
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()
print(cur.execute("SELECT * FROM movie").fetchall())