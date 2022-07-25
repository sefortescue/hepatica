#!/usr/bin/env python3

import dominate
import sqlite3
import sys

def main():

    conn = sqlite3.connect('local.db')
    curs = conn.cursor()

    curs.execute('''CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT''')

    book_title = sys.argv[1]
    book_author = sys.argv[2]

if __name__ == "__main__":
    main()
