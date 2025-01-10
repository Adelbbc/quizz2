import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random


class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz sur les jeux vidéo")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Structurer les questions par thème
        self.questions_by_theme = {
            "Action": [
                {"question": "Dans quel jeu d'action célèbre incarne-t-on un tueur à gages nommé Agent 47 ?", "options": ["Hitman", "Uncharted", "Doom", "Far Cry"], "answer": "Hitman"},
                {"question": "Dans “Uncharted 4”, quel est le prénom du frère de Nathan Drake ?", "options": ["Sam Drake", "Victor Sullivan", "Ethan Drake", "Jack Drake"], "answer": "Sam Drake"},
                {"question": "Dans 'The Last of Us', quel est le prénom de la jeune fille que Joel protège tout au long du jeu ?", "options": ["Ellie", "Tess"], "answer": "Ellie"},
            ],
            "RPG": [
                {"question": "Dans quel RPG emblématique incarne-t-on un héros amnésique appelé 'L’Enfant de Bhaal' ?", "options": ["Baldur’s Gate", "Skyrim", "The Witcher", "Final Fantasy"], "answer": "Baldur’s Gate"},
                {"question": "Dans 'The Elder Scrolls V: Skyrim', quel cri du dragon est utilisé pour repousser les ennemis ?", "options": ["Fus Ro Dah", "Yol Toor Shul"], "answer": "Fus Ro Dah"},
            ],
            "Aventure": [
                {"question": "Dans quel jeu d’aventure incarne-t-on un archéologue nommé Nathan Drake ?", "options": ["Uncharted", "Tomb Raider", "Indiana Jones", "Far Cry"], "answer": "Uncharted"},
                {"question": "Dans 'The Legend of Zelda: Breath of the Wild', comment s’appelle la tablette magique que Link utilise pour résoudre des énigmes ?", "options": ["Sheikah Slate", "Hylian Codex"], "answer": "Sheikah Slate"},
            ]
        }

        self.selected_theme = None
        self.questions = []
        self.score = 0
        self.current_question = 0
        self.time_left = 15

        self.start_theme_selection()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

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
            # Mélanger toutes les questions de tous les thèmes
            all_questions = []
            for questions in self.questions_by_theme.values():
                all_questions.extend(questions)
            random.shuffle(all_questions)
            self.questions = all_questions
        else:
            # Charger les questions du thème sélectionné
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

        # Timer pour chaque question
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
            showinfo("Bonne réponse", "Bravo, c'est la bonne réponse !")
            self.score += 10
        else:
            showinfo("Mauvaise réponse", f"Dommage, la bonne réponse était : {question_data['answer']}")
        self.next_question()

    def next_question(self):
        self.current_question += 1
        self.show_question()

    def show_final_score(self):
        self.clear_screen()
        tk.Label(self.root, text=f"Votre score final : {self.score}", font=("Arial", 24), bg="#f0f0f0").pack(pady=50)
        ttk.Button(self.root, text="Rejouer", command=self.start_theme_selection).pack(pady=20)
        ttk.Button(self.root, text="Quitter", command=self.root.quit).pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
