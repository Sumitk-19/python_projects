import tkinter as tk

questions = [
    ("Python is interpreted?", "yes"),
    ("Function keyword is def?", "yes")
]

index = 0
score = 0

def submit():
    global index, score
    if entry.get().lower() == questions[index][1]:
        score += 1
    index += 1
    entry.delete(0, tk.END)
    if index < len(questions):
        question.config(text=questions[index][0])
    else:
        question.config(text=f"Score: {score}")
        button.config(state="disabled")

root = tk.Tk()
root.title("Quiz App")

question = tk.Label(root, text=questions[0][0])
question.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=submit)
button.pack()

root.mainloop()
