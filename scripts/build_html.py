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
    conn = sqlite3.connect('local.db')
    books_df = pd.read_sql_query("SELECT * FROM books", conn)
    prog_df = pd.read_sql_query("SELECT * FROM apus", conn)
   
    for i in range(len(books_df.index)):
        book_auth = "{}, {}".format(books_df.iat[i,1], books_df.iat[i,2])
        curr_div = books.add(div(cls="books_item"))
        curr_div.add(h2(book_auth))
        curr_df = prog_df.loc[prog_df['id'] == books_df.iat[i,0]]
        for j in range(len(curr_df.index)):
            curr_div.add(div(cls="prog_item",title=curr_df.iat[j,1]))
        curr_stat = books_df.iat[i,3]
        if curr_stat == 0:
            curr_div.add(div(cls="stat_on",title="Ongoing!"))
        elif curr_stat == 1:
            curr_div.add(div(cls="stat_hold",title="On Hold!"))
        elif curr_stat == 2:
            curr_div.add(div(cls="stat_conc",title="Concluded!"))
    print(doc)

if __name__ == "__main__":
    build()
