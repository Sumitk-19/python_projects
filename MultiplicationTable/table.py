import tkinter as tk

def generate_table():
    num = int(entry.get())
    result.delete(1.0, tk.END)
    for i in range(1, 11):
        result.insert(tk.END, f"{num} x {i} = {num*i}\n")

root = tk.Tk()
root.title("Multiplication Table")

tk.Label(root, text="Enter Number").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Generate Table", command=generate_table).pack()

result = tk.Text(root, height=10)
result.pack()

root.mainloop()
