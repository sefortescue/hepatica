#!/usr/bin/env python3

import dominate
from dominate.tags import *
import pandas as pd
import sqlite3

def build():
    # create document object and do stuff to it
    doc = dominate.document(title="hepatica")

    with doc.head:
        link(rel="stylesheet", href="css/style.css")
        link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Ubuntu\&display=swap")

    with doc:
        books = section(cls="books_list")
        footer = section(cls="footer")

    with books:
        h2("Key:", cls="books_key_title")
        key = div(cls="books_key")    
        with key:
            green = div(cls="green_square")
            yellow = div(cls="yellow_square")
            black = div(cls="black_square") 
            with green:
                p("This book is currently being read.")
            with yellow:
                p("This book is on hold to be read.")
            with black:
                p("This book has been finished and/or is used as a reference.")

    # setup local database connection
    conn = sqlite3.connect('local.db')
    books_df = pd.read_sql_query("SELECT * FROM books", conn)
    prog_df = pd.read_sql_query("SELECT * FROM apus", conn)
   
    for i in range(len(books_df.index)):
        book_auth = "{}, {}".format(books_df.iat[i,1], books_df.iat[i,2])
        curr_div = books.add(div(cls="books_item"))
        curr_div.add(h2(book_auth))

        # ADD SUBSET OF PROG_DF FOR EACH BOOK ID 

        for j in range(len(prog_df.index)):
            curr_div.add(div(title=prog_df
        curr_stat = books_df.iat[i,3]
        if curr_stat == 0:
            
        elif curr_stat == 1:

        elif curr_stat == 2:

    print(doc)

if __name__ == "__main__":
    build()
