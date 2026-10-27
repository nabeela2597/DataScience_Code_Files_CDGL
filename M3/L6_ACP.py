
import tkinter as tk
import random

# Function to play the game
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        update_score(1, 0)
    else:
        result = "Computer Wins!"
        update_score(0, 1)

    user_label.config(text="Your Choice: " + user_choice)
    computer_label.config(text="Computer's Choice: " + computer_choice)
    result_label.config(text=result)


# Function to update the score
user_score = 0
computer_score = 0

def update_score(user_points, computer_points):
    global user_score, computer_score
    user_score += user_points
    computer_score += computer_points
    score_label.config(
        text=f"Score - You: {user_score} | Computer: {computer_score}"
    )


# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0

    user_label.config(text="Your Choice: ")
    computer_label.config(text="Computer's Choice: ")
    result_label.config(text="Choose your move!")
    score_label.config(text="Score - You: 0 | Computer: 0")


# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("420x400")
root.config(bg="lightblue")

# Heading
title_label = tk.Label(
    root, text="Rock Paper Scissors",
    font=("Arial", 20, "bold"), bg="lightblue"
)
title_label.pack(pady=15)

# Choice buttons
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10)

for choice in ["Rock", "Paper", "Scissors"]:
    tk.Button(
        button_frame,
        text=choice,
        font=("Arial", 12),
        width=9,
        command=lambda c=choice: play(c)
    ).pack(side=tk.LEFT, padx=5)

# Display choices and result
user_label = tk.Label(root, text="Your Choice: ",
                      font=("Arial", 12), bg="lightblue")
user_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer's Choice: ",
                          font=("Arial", 12), bg="lightblue")
computer_label.pack(pady=5)

result_label = tk.Label(root, text="Choose your move!",
                        font=("Arial", 15, "bold"), bg="lightblue")
result_label.pack(pady=10)

# Score display
score_label = tk.Label(
    root, text="Score - You: 0 | Computer: 0",
    font=("Arial", 12), bg="lightblue"
)
score_label.pack(pady=10)

# Reset button
reset_button = tk.Button(
    root, text="Reset Game",
    font=("Arial", 11), command=reset_game
)
reset_button.pack(pady=10)

# Run the GUI event loop
root.mainloop()
