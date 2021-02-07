import sqlite3


class tdb_lookup:

    def __init__(self):
        self.conn = sqlite3.connect("tdb.db")
        self.c = self.conn.cursor()

    def get_answer(self, question_str):
        self.c.execute("select correct_answer from trivia where question=(?)", (question_str,))
        answer = self.c.fetchone()

        if answer is None:  # Seems kinda redundant, but is needed due to how cursor works
            return None

        return answer[0]


