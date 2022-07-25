#!/usr/bin/env python3

import sqlite3
import sys

def main():
    conn = sqlite3.connect('local.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO books(title, author) VALUES(?, ?)", (sys.argv[1], sys.argv[2]))
if __name__ == "__main__":
    main()
