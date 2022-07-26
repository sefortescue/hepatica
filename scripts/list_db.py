#!/usr/bin/env python3

import sqlite3

def list_books():
    conn = sqlite3.connect('local.db')
    curs = conn.cursor()
    curs.execute("SELECT * FROM books")
    print(curs.fetchall())
    conn.close()
if __name__ == "__main__":
    list_books()
