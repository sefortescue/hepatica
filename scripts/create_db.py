#!/usr/bin/env python3

import sqlite3

def create():
    conn = sqlite3.connect('local.db')
    curs = conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, status INTEGER, count INTEGER)")
    curs.execute("CREATE TABLE IF NOT EXISTS apus (id INTEGER, date TEXT)")
    conn.commit()
    conn.close()
if __name__ == "__main__":
    create()
