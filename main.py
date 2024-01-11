import tkinter as tk
from tkinter import messagebox

# main application window
root = tk.Tk()
root.title("Do your job")

# label example
label = tk.Label(root, text="Welcome do Do your job")
label.pack()

# button example
def on_button_click():
    messagebox.showinfo("Info", "Button clicked!")

button = tk.Button(root, text="Click me", command=on_button_click)
button.pack()

root.mainloop()