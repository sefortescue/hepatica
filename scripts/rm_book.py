#!/usr/bin/env python3

import sqlite3
import sys

def rm_book():
    conn = sqlite3.connect('local.db')
    curs = conn.cursor()
    curs.execute("DELETE FROM books WHERE id=?", (sys.argv[1],))
    curs.execute("DELETE FROM apus WHERE id=?", (sys.argv[1],))
    conn.commit()
    conn.close()
if __name__ == "__main__":
    rm_book()
