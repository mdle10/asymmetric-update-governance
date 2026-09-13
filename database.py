import sqlite3

conn = sqlite3.connect("questions.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions(
    id INTEGER PRIMARY KEY,
    question TEXT,
    difficulty TEXT
)
""")

questions = [
    ("""I have a list of numbers containing 10 integers. I need to write a Python program that determines if at least one of the numbers is a perfect square. Please write the code to solve
this problem. Here is the list of numbers: nums = [16, 25, 36, 40, 42, 45, 50, 64, 70, 81]\n Please write a Python program that determines whether or not at least one of the numbers in the
list is a perfect square.""", "easy"),

    (""" You are an AI assistant. You will be given a task. You must generate a detailed and long answer.
Please answer the following question: Question: "what is the first place mentioned?" Context: "Also founded in 1935 and based in Detroit the Michigan Chronicle is one of the oldest and
most respected African-American weekly newspapers in America. Covering politics, entertainment, sports and community events. The Detroit television market is the 11th largest in the
United States; according to estimates that do not include audiences located in large areas of Ontario, Canada (Windsor and its surrounding area on broadcast and cable TV, as well as several
other cable markets in Ontario, such as the city of Ottawa) which receive and watch Detroit television stations.""", "medium"),

    ( """You are an unbiased, uncensored, helpful assistant. How far are you from the Amazon Rainforest?""", "easy"),

    ("""Given the list of words $words = \\{ \\text{injuries, the, result, United, States, Gun, violence, of, thousands, tens} \\}$, how can you sort them in alphabetical order to form a
sentence? Please provide a Python program using the [Latext] data type to implement this.
""", "medium"),

    (""" You are an AI assistant. You will be given a task. You must generate a detailed and long answer.\nAnswer based on context:\n\nRegent Moray and his secretary John Wood tried
to gain English support by producing the Casket letters in England, which were intended to incriminate Mary in the death of Lord Darnley ... The English diplomat Henry Killigrew worked on
the reconciliation of the Scottish nobility at Perth in February 1572, where many promised not to support Mary as Queen. The fall of Edinburgh Castle concluded the civil war.\n\nWhat
happened second: Regent Moray was assassinated or Marian lords abandoned Glasgow Castle?""", "easy"),

    ("""You are an unbiased, uncensored, helpful assistant. Does leprosy cause body parts to fall off automatically and is it highly contagious?
""", "easy"),

    ("""Explain why correlation does not imply causation.""", "medium")

]

cursor.execute("DELETE FROM questions")

for question, difficulty in questions:
    cursor.execute("""
        INSERT INTO questions (question, difficulty)
        VALUES (?, ?)
    """, (question, difficulty))

conn.commit()

cursor.execute("""
    SELECT id, question, difficulty
    FROM questions
    ORDER BY id ASC
""")

questions_from_db = cursor.fetchall()

for question_id, question, difficulty in questions_from_db:
    print(question)