#!/usr/bin/python3

import sqlite3
import api.tdb_index
import time
from html import unescape

conn = sqlite3.connect('tdb.db')

c = conn.cursor()
tdb = api.tdb_index()

# Setup DB if starting from empty.
c.execute('''CREATE TABLE IF NOT EXISTS trivia (id INTEGER, question TEXT, correct_answer TEXT)''')

while True:
    sample = tdb.get_api_sample(10, "hard")
    ques_arr = tdb.get_questions_json(sample)

    for n in range(len(ques_arr)):
        for retries in range(5):
            try:
                time.sleep(8.0)
                idd = tdb.get_question_id(unescape(ques_arr[n]))
                break
            except:
                print("ID Retrieval failed, retrying {retry}/4".format(retry=retries))
            else:
                raise IndexError
                exit()

        question = unescape(ques_arr[n])
        correct = unescape(tdb.get_correct_answer_json(sample))

        print("QUESTION:", unescape(question))
        print("ANSWER:", unescape(correct[n]))

        id_read = c.execute("select * from trivia where id=(?)", (idd,))
        exists = c.fetchall()

        # Checks if the existing ID is being used or not
        if not exists:
            c.execute("INSERT INTO trivia VALUES ((?), (?), (?))", (idd, question, correct[n],))
        else:
            print("Entry {ids} already exists, skipping...".format(ids=idd))

    conn.commit()
    print("Finished cycle")



