import tkinter as tk

def calculate():
    marks = int(entry.get())
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"
    result.config(text=f"Grade: {grade}")

root = tk.Tk()
root.title("Student Result")

tk.Label(root, text="Enter Marks").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calculate", command=calculate).pack()
result = tk.Label(root, text="")
result.pack()

root.mainloop()
