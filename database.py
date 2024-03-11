import sqlite3

def create_connection():
    try:
        connection = sqlite3.connect("memory.db")
        return connection
    except sqlite3.Error as e:
        print("Error connecting to SQLite database:", e)
        return None


def get_query_and_answers():
    con = create_connection()
    cur = con.cursor()

    cur.execute("SELECT * from queryAndAnswers")
    
    return cur.fetchall()

print(get_query_and_answers())

# def get_answer_from_memory(question):
#     rows = get_query_and_answers()
#     answer = ""

#     for row in rows:
#         if row[0].lower() in question.lower():
#             answer = row[1]
#             break
#     return answer    


# print(get_answer_from_memory("what is time"))