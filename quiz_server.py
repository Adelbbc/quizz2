import socket
import threading
import sqlite3

HOST = 'localhost'
PORT = 12345

conn = sqlite3.connect('quiz.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('SELECT * FROM quiz')
questions = cursor.fetchall()

cursor.execute('''
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT,
    score INTEGER
)
''')
conn.commit()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Serveur prêt, en attente de connexion...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connexion établie avec {addr}")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

def handle_client(client_socket):
    score = 0
    for question in questions:
        question_text = f"{question[2]}\n1. {question[3]}\n2. {question[4]}\n3. {question[5]}\n4. {question[6]}"
        client_socket.send(question_text.encode())
        try:
            client_socket.settimeout(15)
            answer = client_socket.recv(1024).decode()
        except socket.timeout:
            answer = "0"
        if int(answer) == question[7]:
            score += 1

    client_socket.send(f"Votre score : {score}/{len(questions)}".encode())
    player_name = client_socket.recv(1024).decode()
    cursor.execute('INSERT INTO scores (player_name, score) VALUES (?, ?)', (player_name, score))
    conn.commit()
    client_socket.close()

if __name__ == "__main__":
    start_server()
