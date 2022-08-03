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
        link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Ubuntu&display=swap")

    with doc:
        books = section(cls="books_list")
        footer = section(cls="footer")

    # setup local database connection
    conn = sqlite3.connect("local.db")
    books_df = pd.read_sql_query("SELECT * FROM books", conn)
    books_df = books_df.sort_values(by="count", ascending=False)
    prog_df = pd.read_sql_query("SELECT * FROM apus", conn)
   
    for i in range(len(books_df.index)):
        curr_book = books.add(div(cls="books_item"))
        curr_book.add(h2(books_df.iat[i,1], cls="book_title"))
        curr_book.add(h3(books_df.iat[i,2], cls="book_auth"))
        curr_prog = curr_book.add(div(cls="prog_list"))
        curr_df = prog_df.loc[prog_df['id'] == books_df.iat[i,0]]
        for j in range(len(curr_df.index)):
            curr_prog.add(div(cls="prog_item",title=curr_df.iat[j,1]))
        curr_stat = books_df.iat[i,3]
        if curr_stat == 0:
            curr_prog.add(div(cls="prog_item stat_on",title="Reading..."))
        elif curr_stat == 1:
            curr_prog.add(div(cls="prog_item stat_hold",title="Reference!"))
        elif curr_stat == 2:
            curr_prog.add(div(cls="prog_item stat_conc",title="Concluded!"))
    print(doc)

if __name__ == "__main__":
    build()
