#!/usr/bin/env python3

import sqlite3
import sys
from datetime import date

def prog_book():
    conn = sqlite3.connect('local.db')
    curs = conn.cursor()
    today = date.today()
    curs.execute("INSERT INTO apus(id, date) VALUES(?, ?)", (sys.argv[1], today.strftime("%B %d, %Y")
))
    curs.execute("UPDATE books SET count = count + 1 WHERE id=?", (sys.argv[1]))
    conn.commit()
    conn.close()
if __name__ == "__main__":
    prog_book()
