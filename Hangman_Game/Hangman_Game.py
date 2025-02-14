import tkinter as tk
import random

HangmanWords = {
    "apple": "A red or green fruit that keeps the doctor away.",
    "banana": "A long yellow fruit that monkeys love.",
    "chair": "Something you sit on.",
    "table": "A flat surface with legs, used for eating or working.",
    "pencil": "Used for writing and erasing.",
    "river": "A flowing body of water.",
    "tiger": "A big wild cat with orange and black stripes.",
    "pizza": "A round food with cheese and toppings.",
    "soccer": "A sport played with a ball and goals.",
    "shadow": "A dark shape made by blocking light."
}

selected_word, hint_text = random.choice(list(HangmanWords.items()))
selected_word = selected_word.upper()
wordLength = len(selected_word)

guessed_letters = set()
max_mistakes = 7
mistakes = 0

def update_word_display():
    display_word = ""
    for letter in selected_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    word_label.config(text=display_word.strip())
def check_guess():
    global mistakes
    guess = guess_entry.get().strip().upper()
    guess_entry.delete(0, tk.END)  # Clear the entry box

    if len(guess) != 1 or not guess.isalpha():
        result_label.config(text="Please enter a single letter!", fg="red")
        return

    if guess in guessed_letters:
        result_label.config(text="You already guessed that letter!", fg="red")
        return

    guessed_letters.add(guess)

    if guess not in selected_word:
        mistakes += 1
        result_label.config(text="Incorrect guess!", fg="red")
        draw_hangman()
    else:
        result_label.config(text="Correct guess!", fg="green")

    update_word_display()

    # Check for win or lose
    if all(letter in guessed_letters for letter in selected_word):
        result_label.config(text="Congratulations! You won! 🎉", fg="green")
        submit_button.config(state=tk.DISABLED)
    elif mistakes >= max_mistakes:
        result_label.config(text=f"Game Over! The word was: {selected_word}", fg="red")
        submit_button.config(state=tk.DISABLED)

# Function to draw the hangman step by step
def draw_hangman():

    if mistakes == 1:
        canvas.create_line(100, 30, 100, 50)
    elif mistakes == 2:
        canvas.create_oval(90, 50, 110, 70)
    elif mistakes == 3:
        canvas.create_line(100, 70, 100, 110)
    elif mistakes == 4:
        canvas.create_line(100, 80, 85, 100)
    elif mistakes == 5:
        canvas.create_line(100, 80, 115, 100)
    elif mistakes == 6:
        canvas.create_line(100, 110, 85, 140)
    elif mistakes == 7:
        canvas.create_line(100, 110, 115, 140)


# Create main window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("640x300+325+175")

# frame
frame1 = tk.Frame(root,height=440,width=400,relief=tk.RIDGE,bg="light yellow",borderwidth=2)
frame1.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Word to Guess Label
word_label = tk.Label(frame1, text="", font=("Arial", 24), bg="lightblue", width=20,borderwidth=2, relief=tk.SOLID)
word_label.grid(row=0, column=0, padx=10, pady=10)

#Hint Label
hint_label = tk.Label(frame1, text=f"Hint: {hint_text}", font=("Arial", 12), bg="lightgreen", width=45)
hint_label.grid(row=1, column=0, padx=10, pady=10)

# Entry Box for Guess
guess_entry = tk.Entry(frame1, font=("Arial", 12), width=20)
guess_entry.grid(row=2, column=0, padx=10, pady=5)

# Instruction Label
instruction_label = tk.Label(frame1, text="Guess one letter at a time", font=("Arial", 10), bg="yellow")
instruction_label.grid(row=3, column=0, padx=10, pady=5)

#Submit Button
submit_button = tk.Button(frame1, text="Submit", font=("Arial", 12), bg="purple", fg="white", command=check_guess)
submit_button.grid(row=4, column=0, padx=10, pady=10)

# Result Label
result_label = tk.Label(frame1, text="", font=("Arial", 12))
result_label.grid(row=5, column=0, padx=10, pady=5)

# Hangman Drawing (Canvas)
canvas = tk.Canvas(frame1, width=150, height=200, bg="white", highlightbackground="red")
canvas.grid(row=0, column=1, rowspan=6, padx=20, pady=10)

canvas.create_line(30, 160, 80, 160)#Base
canvas.create_line(55, 160, 55, 30) #Pole
canvas.create_line(55, 30, 100, 30) #Rope

update_word_display()
root.mainloop()
