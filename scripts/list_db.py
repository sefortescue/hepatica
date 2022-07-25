#!/usr/bin/env python3

import sqlite3

def main():
    conn = sqlite3.connect('local.db')
    curs = conn.cursor()
    curs.execute("SELECT * FROM books")
    dat = curs.fetchall()
    print('\n'.join(str(a) for a in dat))
if __name__ == "__main__":
    main()
