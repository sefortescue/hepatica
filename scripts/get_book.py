#!/usr/bin/env python3

import sqlite3
import sys

def get_book():
    conn = sqlite3.connect('local.db')
    curs = conn.cursor()
    curs.execute("SELECT * FROM books WHERE id=?", sys.argv[1])
    print(curs.fetchall())
    conn.close()
if __name__ == "__main__":
    get_book()
