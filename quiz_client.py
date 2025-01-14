import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import random
import os

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("QUIZ ADVAMOUS 🇸🇳🇫🇷 🌟🙌🎉")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Fichier pour stocker les utilisateurs
        self.user_file = "users.txt"

        # Fichier pour stocker les scores
        self.high_score_file = "high_scores.txt"
        self.high_scores = self.load_high_scores()

        # Structurer les questions par thème
        self.questions_by_theme = {
            "Action": [
                {"question": "Dans quel jeu célèbre incarne-t-on un tueur à gages nommé Agent 47 ?", "options": ["Hitman", "Uncharted", "Doom", "Far Cry"], "answer": "Hitman"},
                {"question": "Dans 'Uncharted 4', quel est le prénom du frère de Nathan Drake ?", "options": ["Sam Drake", "Victor Sullivan", "Ethan Drake", "Jack Drake"], "answer": "Sam Drake"},
                {"question": "Dans 'The Last of Us', quel est le prénom de la jeune fille que Joel protège ?", "options": ["Ellie", "Tess"], "answer": "Ellie"},
                {"question": "Quel studio est à l'origine de la franchise 'Assassin's Creed' ?", "options": ["Naughty Dog", "Ubisoft"], "answer": "Ubisoft"},
                {"question": "Dans 'Doom', quel est le surnom donné au protagoniste principal ?", "options": ["Slayer", "Hunter"], "answer": "Slayer"},
                {"question": "Quel est le nom de l'antagoniste principal dans 'Far Cry 3' ?", "options": ["Vaas Montenegro", "Anton Castillo"], "answer": "Vaas Montenegro"},
                {"question": "Dans 'God of War' (2018), qui est le fils de Kratos ?", "options": ["Atreus", "Loki"], "answer": "Atreus"},
                {"question": "Dans quel jeu d'action explore-t-on un monde ouvert en incarnant Arthur Morgan, membre d’un gang ?", "options": ["Cyberpunk 2077", "Red Dead Redemption 2"], "answer": "Red Dead Redemption 2"},
                {"question": "Dans 'Batman: Arkham City', qui est le principal antagoniste que Batman affronte ?", "options": ["Le Joker", "Hugo Strange"], "answer": "Hugo Strange"},
                {"question": "Dans 'Call of Duty: Modern Warfare', quel personnage est connu sous le nom de Ghost ?", "options": ["Simon Riley", "Price", "Soap", "Roach"], "answer": "Simon Riley"},
                {"question": "Quel jeu de tir populaire propose un mode Battle Royale appelé 'Warzone' ?", "options": ["Call of Duty", "Battlefield", "PUBG", "Apex Legends"], "answer": "Call of Duty"},
                {"question": "Dans 'Metal Gear Solid', quel est le nom de code du protagoniste principal ?", "options": ["Solid Snake", "Big Boss", "Raiden", "Ocelot"], "answer": "Solid Snake"},
            ],
            "RPG": [
                {"question": "Dans quel RPG emblématique incarne-t-on un héros amnésique appelé 'L’Enfant de Bhaal' ?", "options": ["Baldur’s Gate", "Skyrim", "The Witcher", "Final Fantasy"], "answer": "Baldur’s Gate"},
                {"question": "Dans 'The Elder Scrolls V: Skyrim', quel cri du dragon est utilisé pour repousser les ennemis ?", "options": ["Fus Ro Dah", "Yol Toor Shul"], "answer": "Fus Ro Dah"},
                {"question": "Quel studio est derrière la série 'The Witcher' ?", "options": ["BioWare", "CD Projekt Red"], "answer": "CD Projekt Red"},
                {"question": "Dans 'Final Fantasy VII', quel est le nom de l’arme emblématique de Cloud ?", "options": ["Gunblade", "Masamune"], "answer": "Masamune"},
                {"question": "Quel jeu de rôle se déroule dans le monde post-apocalyptique du Wasteland ?", "options": ["Fallout", "Cyberpunk 2077"], "answer": "Fallout"},
                {"question": "Dans 'Mass Effect', quel est le nom de l’intelligence artificielle du vaisseau Normandy ?", "options": ["EDI", "ADA"], "answer": "EDI"},
                {"question": "Dans 'Dark Souls', comment s’appelle l’objet qui permet au joueur de regagner de la santé ?", "options": ["Estus Flask", "Healing Shard"], "answer": "Estus Flask"},
                {"question": "Dans 'The Witcher 3: Wild Hunt', quelle est l’arme principale de Geralt ?", "options": ["Une épée", "Un arc"], "answer": "Une épée"},
                {"question": "Dans 'Persona 5', quel est le surnom du protagoniste principal lorsqu’il est dans le Metaverse ?", "options": ["Joker", "Ace", "Phantom", "Shadow"], "answer": "Joker"},
                {"question": "Dans 'Dragon Age: Inquisition', comment s’appelle l’inquisiteur(e) dans le jeu ?", "options": ["The Herald of Andraste", "The Warden", "The Seeker", "The Champion"], "answer": "The Herald of Andraste"},
                {"question": "Dans 'Chrono Trigger', quel est le nom de l’épée légendaire que Chrono peut obtenir ?", "options": ["Masamune", "Excalibur", "Ragnarok", "Ultima Weapon"], "answer": "Masamune"},
            ],
            "Aventure": [
                {"question": "Dans quel jeu incarne-t-on un archéologue nommé Nathan Drake ?", "options": ["Uncharted", "Tomb Raider", "Indiana Jones", "Far Cry"], "answer": "Uncharted"},
                {"question": "Quel personnage accompagne souvent Lara Croft dans ses aventures dans la trilogie reboot de 'Tomb Raider' ?", "options": ["Jonah Maiava", "Victor Sullivan", "Jack Drake", "Ethan Hunt"], "answer": "Jonah Maiava"},
                {"question": "Dans 'The Legend of Zelda: Breath of the Wild', comment s’appelle la tablette magique que Link utilise pour résoudre des énigmes ?", "options": ["Sheikah Slate", "Hylian Codex"], "answer": "Sheikah Slate"},
                {"question": "Quel studio a développé 'Tomb Raider' (reboot de 2013) ?", "options": ["Crystal Dynamics", "Naughty Dog"], "answer": "Crystal Dynamics"},
                {"question": "Dans 'Life is Strange', quelle est la capacité spéciale de Max Caulfield ?", "options": ["Lire dans les pensées", "Manipuler le temps"], "answer": "Manipuler le temps"},
                {"question": "Quel jeu d’aventure met en scène un jeune garçon en quête de lumière, affrontant des ombres dans un monde monochrome ?", "options": ["Inside", "Limbo"], "answer": "Limbo"},
                {"question": "Dans 'Red Dead Redemption 2', comment s’appelle le meilleur ami et allié de Arthur Morgan ?", "options": ["John Marston", "Hosea Matthews"], "answer": "Hosea Matthews"},
                {"question": "Dans 'Gris', quel est le principal objectif du joueur ?", "options": ["Restaurer les couleurs du monde", "Trouver une clé magique"], "answer": "Restaurer les couleurs du monde"},
                {"question": "Dans 'Shadow of the Colossus', comment s’appelle le cheval du protagoniste ?", "options": ["Argo", "Agro", "Epona", "Shadow"], "answer": "Agro"},
                {"question": "Dans 'Firewatch', où se déroule principalement l’intrigue ?", "options": ["Dans une montagne enneigée", "Dans un parc national", "Dans une grotte mystérieuse", "Sur une île déserte"], "answer": "Dans un parc national"},
                {"question": "Dans 'Monkey Island', comment s’appelle le pirate fantôme antagoniste ?", "options": ["Captain Blackbeard", "LeChuck", "Captain Flint", "Morgan le Pirate"], "answer": "LeChuck"},
                {"question": "Dans 'The Walking Dead' de Telltale, quel est le prénom de la jeune fille que Lee protège ?", "options": ["Sarah", "Ellie", "Clementine", "Molly"], "answer": "Clementine"},
            ]
        }

        self.selected_theme = None
        self.questions = []
        self.score = 0
        self.current_question = 0
        self.time_left = 15

        self.authenticated_user = None  # Stocker l'utilisateur connecté
        self.auth_screen()  # Démarre avec l'écran d'authentification
 # Charger et afficher l'image
        try:
            image = Image.open("iut_logo.png")  # Remplacez par votre fichier image
            image = image.resize((1200, 350), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            tk.Label(self.root, image=photo, bg="#f0f0f0").pack(pady=20)
            self.root.image = photo  # Empêche le garbage collector de supprimer l'image
        except FileNotFoundError:
            tk.Label(self.root, text="Image non trouvée", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)

    def load_high_scores(self):
        if not os.path.exists(self.high_score_file):
            return []
        with open(self.high_score_file, "r") as file:
            scores = [line.strip() for line in file.readlines()]
        return scores

    def save_high_score(self, player_name, score):
        self.high_scores.append(f"{player_name}: {score}")
        self.high_scores.sort(key=lambda x: int(x.split(": ")[1]), reverse=True)
        with open(self.high_score_file, "w") as file:
            file.write("\n".join(self.high_scores))

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def auth_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Connexion", font=("Arial", 24), bg="#f0f0f0").pack(pady=20)

        tk.Label(self.root, text="Nom d'utilisateur :", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
        username = tk.StringVar()
        tk.Entry(self.root, textvariable=username, font=("Arial", 14)).pack(pady=5)

        tk.Label(self.root, text="Mot de passe :", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
        password = tk.StringVar()
        tk.Entry(self.root, textvariable=password, font=("Arial", 14), show="*").pack(pady=5)

        ttk.Button(self.root, text="Se connecter", command=lambda: self.authenticate(username.get(), password.get())).pack(pady=20)
        ttk.Button(self.root, text="S'inscrire", command=self.register_screen).pack(pady=10)

    def authenticate(self, username, password):
        if os.path.exists(self.user_file):
            with open(self.user_file, "r") as file:
                users = file.readlines()
            for user in users:
                stored_username, stored_password = user.strip().split(":")
                if username == stored_username and password == stored_password:
                    self.authenticated_user = username
                    self.start_screen()
                    return
        showinfo("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

    def register_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Inscription", font=("Arial", 24), bg="#f0f0f0").pack(pady=20)

        tk.Label(self.root, text="Nom d'utilisateur :", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
        username = tk.StringVar()
        tk.Entry(self.root, textvariable=username, font=("Arial", 14)).pack(pady=5)

        tk.Label(self.root, text="Mot de passe :", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
        password = tk.StringVar()
        tk.Entry(self.root, textvariable=password, font=("Arial", 14), show="*").pack(pady=5)

        ttk.Button(self.root, text="S'inscrire", command=lambda: self.register(username.get(), password.get())).pack(pady=20)
        ttk.Button(self.root, text="Retour", command=self.auth_screen).pack(pady=10)

    def register(self, username, password):
        if not username or not password:
            showinfo("Erreur", "Veuillez remplir tous les champs.")
            return

        with open(self.user_file, "a") as file:
            file.write(f"{username}:{password}\n")

        showinfo("Succès", "Inscription réussie ! Vous pouvez maintenant vous connecter.")
        self.auth_screen()

    def start_screen(self):
        self.clear_screen()
        tk.Label(self.root, text=f"Bienvenue, {self.authenticated_user} !", font=("Arial", 24), bg="#f0f0f0").pack(pady=20)
        ttk.Button(self.root, text="Commencer le quiz", command=self.start_theme_selection).pack(pady=20)
        ttk.Button(self.root, text="Meilleurs scores", command=self.show_high_scores).pack(pady=10)
        ttk.Button(self.root, text="Déconnexion", command=self.auth_screen).pack(pady=10)

    def show_high_scores(self):
        self.clear_screen()
        tk.Label(self.root, text="Meilleurs scores 🥈🏆🎖", font=("Arial", 24), bg="#f0f0f0").pack(pady=20)
        for score in self.high_scores[:10]:
            tk.Label(self.root, text=score, font=("Arial", 18), bg="#f0f0f0").pack()
        ttk.Button(self.root, text="Retour", command=self.start_screen).pack(pady=20)

    def start_theme_selection(self):
        self.clear_screen()
        tk.Label(self.root, text="Choisissez un Thème", font=("Arial", 24), bg="#f0f0f0").pack(pady=30)

        for theme in list(self.questions_by_theme.keys()) + ["Aléatoire"]:
            ttk.Button(self.root, text=theme, command=lambda t=theme: self.start_quiz(t)).pack(pady=10)

    def start_quiz(self, theme):
        self.selected_theme = theme
        self.score = 0
        self.current_question = 0
        self.time_left = 15

        if theme == "Aléatoire":
            all_questions = [q for theme_questions in self.questions_by_theme.values() for q in theme_questions]
            random.shuffle(all_questions)
            self.questions = all_questions
        else:
            self.questions = self.questions_by_theme[theme]

        self.show_question()

    def show_question(self):
        if self.current_question >= len(self.questions):
            self.show_final_score()
            return

        question_data = self.questions[self.current_question]

        self.clear_screen()
        tk.Label(self.root, text=f"Question {self.current_question + 1}/{len(self.questions)}", font=("Arial", 18), bg="#f0f0f0").pack(pady=10)
        tk.Label(self.root, text=question_data["question"], font=("Arial", 18), wraplength=700, bg="#f0f0f0").pack(pady=20)

        for option in question_data["options"]:
            ttk.Button(self.root, text=option, command=lambda o=option: self.check_answer(o)).pack(pady=5)

        self.time_left = 15
        self.timer_label = tk.Label(self.root, text=f"Temps restant : {self.time_left} s", font=("Arial", 14), bg="#f0f0f0")
        self.timer_label.pack(pady=20)
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Temps restant : {self.time_left} s")
            self.root.after(1000, self.update_timer)
        else:
            showinfo("Temps écoulé", "Le temps est écoulé pour cette question !")
            self.next_question()

    def check_answer(self, selected_option):
        question_data = self.questions[self.current_question]
        if selected_option == question_data["answer"]:
            showinfo("Bonne réponse", "Bravo 👏, c'est la bonne réponse !")
            self.score += 10
        else:
            showinfo("Mauvaise réponse", f"Dommage 😔🤷‍♂️💔, la bonne réponse était : {question_data['answer']}")
        self.next_question()

    def next_question(self):
        self.current_question += 1
        self.show_question()

    def show_final_score(self):
        self.clear_screen()
        tk.Label(self.root, text=f"Votre score final : {self.score}", font=("Arial", 24), bg="#f0f0f0").pack(pady=20)

        player_name = tk.StringVar()
        tk.Label(self.root, text="Entrez votre nom :", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
        tk.Entry(self.root, textvariable=player_name, font=("Arial", 14)).pack(pady=10)
        ttk.Button(self.root, text="Sauvegarder", command=lambda: self.save_high_score(player_name.get(), self.score)).pack(pady=10)

        ttk.Button(self.root, text="Rejouer", command=self.start_theme_selection).pack(pady=10)
        ttk.Button(self.root, text="Retour à l'accueil", command=self.start_screen).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
