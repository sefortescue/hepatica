#!/usr/bin/env python3

import dominate
from dominate.tags import *
import sqlite3

def build():
    # setup local database connection
    conn = sqlite3.connect('local.db')
    curs = conn.cursor()
    
    # create document object and do stuff to it
    doc = dominate.document(title="hepatica")

    with doc.head:
        link(rel="stylesheet", href="css/style.css")
        link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Ubuntu&display=swap")

    with doc:
        books = section(cls="books", id="books")
        footer = section(cls="foot", id="foot")
    
    with books:
        h1("TEST")

    print(doc)

if __name__ == "__main__":
    build()
