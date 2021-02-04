#!/usr/bin/python3

# unescape_db: Converts numeric references from the database to their corresponding unicode characters.

import sqlite3
from html import unescape

conn = sqlite3.connect('tdb.db')

c = conn.cursor()
c2 = conn.cursor()



c.execute('SELECT * FROM trivia')
for row in c.fetchall():
	ctr = 0
	entry = row
	newentry = unescape(entry[2])
	idd = entry[0]
	print(idd)
	print(newentry)
	c2.execute("UPDATE trivia SET correct_answer = (?) WHERE id = (?)", (newentry, idd) )
	ctr = ctr + 1
	
conn.commit()
