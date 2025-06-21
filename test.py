#!/usr/bin/env python

import psycopg

# Connect to your PostgreSQL database
conn = psycopg.connect(
    dbname="dvdrental",
    user="postgres",
    password="",
    host="localhost",
    port=5432
)

with conn.cursor() as cur:
    cur.execute("SELECT * FROM customer")
    rows = cur.fetchall()
    for row in rows:
        print(row)

conn.close()