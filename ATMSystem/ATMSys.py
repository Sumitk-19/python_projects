import tkinter as tk

balance = 5000

def check_balance():
    label.config(text=f"Balance: ₹{balance}")

def deposit():
    global balance
    balance += int(entry.get())
    check_balance()

def withdraw():
    global balance
    amt = int(entry.get())
    if amt <= balance:
        balance -= amt
        check_balance()
    else:
        label.config(text="Insufficient Balance")

root = tk.Tk()
root.title("ATM System")

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Check Balance", command=check_balance).pack()
tk.Button(root, text="Deposit", command=deposit).pack()
tk.Button(root, text="Withdraw", command=withdraw).pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
