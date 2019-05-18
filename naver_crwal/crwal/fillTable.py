import sqlite3

conn = sqlite3.connect("disease2.db")
cur = conn.cursor()


with conn:
    cur.execute("SELECT * FROM disease WHERE organs="가슴")