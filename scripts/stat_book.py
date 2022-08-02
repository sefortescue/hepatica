#!/usr/bin/env python3

import sqlite3
import sys

def stat_book():
    conn = sqlite3.connect('local.db')
    curs = conn.cursor()
    if sys.argv[2] == "0":
        curs.execute("UPDATE books SET status=0 WHERE id=?", (sys.argv[1],))
    elif sys.argv[2] == "1":
        curs.execute("UPDATE books SET status=1 WHERE id=?", (sys.argv[1],))
    elif sys.argv[2] == "2":
        curs.execute("UPDATE books SET status=2 WHERE id=?", (sys.argv[1],)) 
    else:
        conn.close()
        exit(1) 
    conn.commit()
    conn.close()
if __name__ == "__main__":
    stat_book()
