#!/usr/bin/env python3

import dominate
from dominate.tags import *
import pandas as pd
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
        books = section(cls="books_list")
        footer = section(cls="footer")

    with books:
        h2("Key:", cls="books_key_title")
        key = div(cls="books_key")    

    with key:
        green = div(cls="green_square")
        yellow = div(cls="yellow_square")
        red = div(cls="red_square") 

    with green:
        p("TEXT")

    with yellow:
        p("TEXT")

    with red:
        p("TEXT")            

    #books += h1(row)

    df = pd.read_sql_query("SELECT * FROM books", conn)

    print(doc)

if __name__ == "__main__":
    build()
