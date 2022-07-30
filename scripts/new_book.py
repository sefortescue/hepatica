#!/usr/bin/env python3

import sqlite3
import sys

def new_book():
    conn = sqlite3.connect('local.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO books(title, author, status) VALUES(?, ?, ?)", (sys.argv[1], sys.argv[2], 0))
    conn.commit()
    conn.close()
if __name__ == "__main__":
    new_book()
