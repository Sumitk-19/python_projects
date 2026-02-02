import tkinter as tk

def red():
    label.config(text="STOP", bg="red")

def yellow():
    label.config(text="READY", bg="yellow")

def green():
    label.config(text="GO", bg="green")

root = tk.Tk()
root.title("Traffic Signal")

label = tk.Label(root, text="", font=("Arial", 30), width=10)
label.pack(pady=20)

tk.Button(root, text="RED", command=red).pack(side="left", padx=10)
tk.Button(root, text="YELLOW", command=yellow).pack(side="left", padx=10)
tk.Button(root, text="GREEN", command=green).pack(side="left", padx=10)

root.mainloop()
