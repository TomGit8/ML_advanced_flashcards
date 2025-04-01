import tkinter as tk
from tkinter import messagebox
import json

# Charger les questions depuis le fichier JSON
with open("qcm_ffnn_30_questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QCM - Réseaux de Neurones FFNN 🧠")
        self.root.geometry("700x500")

        self.q_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=650, font=("Helvetica", 14), justify="left")
        self.question_label.pack(pady=20)

        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for _ in range(4):  # Max 4 choix affichés
            rb = tk.Radiobutton(root, text="", variable=self.radio_var, value="", font=("Helvetica", 12), wraplength=600)
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)

        self.next_btn = tk.Button(root, text="Suivant", command=self.next_question, font=("Helvetica", 12, "bold"))
        self.next_btn.pack(pady=20)

        self.load_question()

    def load_question(self):
        q = questions[self.q_index]
        self.radio_var.set(None)
        self.question_label.config(text=f"Q{self.q_index + 1}: {q['question']}")

        # Cacher tous les boutons au début
        for rb in self.radio_buttons:
            rb.pack_forget()

        if q["type"] in ["mcq", "true_false"]:
            options = q["choices"] if "choices" in q else ["Vrai", "Faux"]
            for i, option in enumerate(options):
                self.radio_buttons[i].config(text=option, value=option)
                self.radio_buttons[i].pack(anchor="w")
        else:
            self.question_label.config(text=f"{q['question']}\n\n(Type : question ouverte)\nRéponse attendue : {q['answer']}\n\nExplication : {q['explanation']}")

    def next_question(self):
        q = questions[self.q_index]

        if q["type"] in ["mcq", "true_false"]:
            selected = self.radio_var.get()
            if not selected:
                messagebox.showwarning("Attention", "Merci de sélectionner une réponse.")
                return

            correct = q["answer"]
            if selected.strip().lower() == correct.strip().lower():
                self.score += 1
                messagebox.showinfo("Bonne réponse ✅", f"✅ Bonne réponse !\n\n{q['explanation']}")
            else:
                messagebox.showinfo("Mauvaise réponse ❌", f"❌ Mauvaise réponse.\nRéponse correcte : {correct}\n\n{q['explanation']}")

        self.q_index += 1
        if self.q_index >= len(questions):
            self.show_result()
        else:
            self.load_question()

    def show_result(self):
        message = f"🎯 Score final : {self.score}/{len([q for q in questions if q['type'] in ['mcq', 'true_false']])}\n"
        if self.score == len(questions):
            message += "💪 Parfait ! Tu maîtrises tout."
        elif self.score >= 20:
            message += "🧠 Très bon niveau !"
        elif self.score >= 15:
            message += "🙂 Solide mais peut mieux faire."
        else:
            message += "📘 Besoin de réviser un peu !"
        messagebox.showinfo("Résultat", message)
        self.root.destroy()

# Lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
