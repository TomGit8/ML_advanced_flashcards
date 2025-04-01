import tkinter as tk
from tkinter import messagebox

# Liste des questions / réponses
questions = [
    {
        "question": "1. Quelle est la fonction du biais dans un neurone artificiel ?",
        "options": ["Multiplier les poids", "Décaler la fonction d’activation", "Supprimer les entrées nulles", "Ajouter du bruit"],
        "answer": 1
    },
    {
        "question": "2. Quelle fonction d’activation peut provoquer des 'neurones morts' ?",
        "options": ["Sigmoïde", "Tanh", "ReLU", "Leaky ReLU"],
        "answer": 2
    },
    {
        "question": "3. Lors de la propagation avant, que calcule-t-on en premier dans une couche ?",
        "options": ["Fonction d’activation", "Sortie", "Somme pondérée (z)", "Erreur"],
        "answer": 2
    },
    {
        "question": "4. À quoi sert la rétropropagation ?",
        "options": ["Calculer la sortie du réseau", "Mettre à jour les poids", "Multiplier les entrées", "Créer un réseau récurrent"],
        "answer": 1
    },
    {
        "question": "5. Quel est l’effet d’un taux d’apprentissage trop élevé ?",
        "options": ["Apprentissage trop lent", "Pas de convergence", "Réseau figé", "Aucun"],
        "answer": 1
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QCM - Réseaux de Neurones FFNN 🧠")

        self.q_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=500, font=("Helvetica", 14), justify="left")
        self.question_label.pack(pady=20)

        self.radio_var = tk.IntVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.radio_var, value=i, font=("Helvetica", 12))
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)

        self.next_btn = tk.Button(root, text="Suivant", command=self.next_question, font=("Helvetica", 12, "bold"))
        self.next_btn.pack(pady=20)

        self.load_question()

    def load_question(self):
        q = questions[self.q_index]
        self.question_label.config(text=q["question"])
        self.radio_var.set(-1)
        for i, option in enumerate(q["options"]):
            self.radio_buttons[i].config(text=option)

    def next_question(self):
        selected = self.radio_var.get()
        if selected == -1:
            messagebox.showwarning("Attention", "Merci de sélectionner une réponse.")
            return

        correct = questions[self.q_index]["answer"]
        if selected == correct:
            self.score += 1

        self.q_index += 1
        if self.q_index >= len(questions):
            self.show_result()
        else:
            self.load_question()

    def show_result(self):
        message = f"🎯 Score final : {self.score}/{len(questions)}\n"
        if self.score == len(questions):
            message += "💪 Parfait ! Tu maîtrises le sujet."
        elif self.score >= 3:
            message += "🧠 Pas mal ! Encore un petit effort."
        else:
            message += "📘 Il est temps de réviser ensemble 😉"
        messagebox.showinfo("Résultat", message)
        self.root.destroy()

# Lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
