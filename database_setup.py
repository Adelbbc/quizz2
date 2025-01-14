import sqlite3

def create_database():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # Création de la table quiz pour les questions
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS quiz (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        theme TEXT,
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        correct_option INTEGER
    )
    ''')


    cursor.executemany('''
    INSERT INTO quiz (theme, question, option1, option2, option3, option4, correct_option)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', questions)

    conn.commit()
    conn.close()
    print("Base de données créée et questions insérées avec succès !")

if __name__ == "__main__":
    create_database()

import sqlite3  # Import de sqlite3

def show_leaderboard():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT player_name, score FROM scores ORDER BY score DESC LIMIT 10")
    leaders = cursor.fetchall()

    print("\n🏆 Classement des Meilleurs Scores :")
    for rank, (name, score) in enumerate(leaders, start=1):
        print(f"{rank}. {name} - {score} points")

    conn.close()

if __name__ == "__main__":
    show_leaderboard()
