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

    # Insertion de questions sur l'Afrique et le Sénégal
    questions = [
        ('Culture Générale', 'Quelle est la capitale de la France ?', 'Berlin', 'Madrid', 'Paris', 'Rome', 3),
        ('Sport', 'Quel pays a remporté la dernière Coupe du Monde ?', 'Argentine', 'Brésil', 'Allemagne', 'Italie', 1),
        ('Géographie', 'Quel est le plus grand désert du monde ?', 'Gobi', 'Sahara', 'Antarctique', 'Kalahari', 3),
        ('Afrique', 'Quel est le plus long fleuve d’Afrique ?', 'Congo', 'Niger', 'Nil', 'Zambèze', 3),
        ('Sénégal', 'Quelle est la capitale du Sénégal ?', 'Dakar', 'Thiès', 'Saint-Louis', 'Kaolack', 1),
        ('Histoire', 'En quelle année le Sénégal a-t-il obtenu son indépendance ?', '1958', '1960', '1963', '1975', 2),
        ('Sénégal', 'Quelle est la langue officielle du Sénégal ?', 'Anglais', 'Français', 'Wolof', 'Portugais', 2),
        ('Musique', 'Quel chanteur sénégalais est connu mondialement ?', 'Alpha Blondy', 'Youssou N’Dour', 'Salif Keita', 'Tiken Jah Fakoly', 2),
        ('Culture', 'Quel plat est emblématique du Sénégal ?', 'Couscous', 'Thieboudienne', 'Yassa', 'Ndolé', 2),
        ('Sport', 'Quelle équipe de football a remporté la CAN 2021 ?', 'Égypte', 'Cameroun', 'Sénégal', 'Maroc', 3),
        ('Histoire', 'Qui est le premier président du Sénégal ?', 'Léopold Sédar Senghor', 'Abdoulaye Wade', 'Macky Sall', 'Ousmane Sonko', 1)
    ]

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
