import tkinter as tk
import random
from tkinter import messagebox

user_score = 0
computer_score = 0

def play(choice):
    global user_score, computer_score

    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    label_user_choice.config(text=f"Your Choice: {choice}")
    label_computer_choice.config(text=f"Computer Choice: {computer_choice}")

    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Scissors" and computer_choice == "Paper") or \
         (choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    label_result.config(text=result)
    label_score.config(text=f"Score → You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    label_user_choice.config(text="Your Choice: ")
    label_computer_choice.config(text="Computer Choice: ")
    label_result.config(text="Result")
    label_score.config(text="Score → You: 0 | Computer: 0")

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x450")
root.config(bg="#f4f6f8")


tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold"),
    bg="#f4f6f8"
).pack(pady=15)

tk.Label(
    root,
    text="Choose one option below",
    font=("Arial", 12),
    bg="#f4f6f8"
).pack()

btn_frame = tk.Frame(root, bg="#f4f6f8")
btn_frame.pack(pady=20)

tk.Button(
    btn_frame, text="Rock",
    width=12, height=2,
    bg="#FF7043", fg="white",
    command=lambda: play("Rock")
).grid(row=0, column=0, padx=10)

tk.Button(
    btn_frame, text="Paper",
    width=12, height=2,
    bg="#42A5F5", fg="white",
    command=lambda: play("Paper")
).grid(row=0, column=1, padx=10)

tk.Button(
    btn_frame, text="Scissors",
    width=12, height=2,
    bg="#66BB6A", fg="white",
    command=lambda: play("Scissors")
).grid(row=0, column=2, padx=10)


label_user_choice = tk.Label(root, text="Your Choice: ", bg="#f4f6f8", font=("Arial", 11))
label_user_choice.pack(pady=5)

label_computer_choice = tk.Label(root, text="Computer Choice: ", bg="#f4f6f8", font=("Arial", 11))
label_computer_choice.pack(pady=5)

label_result = tk.Label(
    root,
    text="Result",
    font=("Arial", 14, "bold"),
    bg="#f4f6f8",
    fg="#333"
)
label_result.pack(pady=10)

label_score = tk.Label(
    root,
    text="Score → You: 0 | Computer: 0",
    font=("Arial", 12),
    bg="#f4f6f8"
)
label_score.pack(pady=10)


tk.Button(
    root,
    text="Play Again / Reset",
    bg="#9C27B0",
    fg="white",
    width=20,
    command=reset_game
).pack(pady=15)

root.mainloop()
