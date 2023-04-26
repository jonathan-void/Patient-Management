import subprocess
import tkinter as tk

def run_python_file(filename):
    subprocess.run(["python", filename])

def on_button_click():
    run_python_file("main.py")

root = tk.Tk()
root.geometry("700x500")

button = tk.Button(root, text="New Patient", command=on_button_click, width=10, height=7)
button.pack(side="top", padx=30, pady=150)

root.mainloop()