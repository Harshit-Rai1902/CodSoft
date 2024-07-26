#PASSWORD GENERATOR

import tkinter as tk
import random

class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator")
        self.window.geometry("300x250")
        self.window.configure(background="#f0f0f0")  # light gray background
        self.label = tk.Label(self.window, text="PASSWORD GENERATOR", font=("Helvetica", 18, "bold"), fg="red", bg="#f0f0f0")  # blue font on light gray background
        self.label.pack(pady=10)
        self.number_letter_label = tk.Label(self.window, text="Enter the length of alphabets:", font=("Helvetica", 12), fg="#333", bg="#f0f0f0")  # dark gray font on light gray background
        self.number_letter_label.pack()
        self.number_letter_entry = tk.Entry(self.window, width=20, font=("Helvetica", 12), fg="#333", bg="#fff")  # white background with dark gray font
        self.number_letter_entry.pack()
        self.number_digits_label = tk.Label(self.window, text="Enter the length of digits:", font=("Helvetica", 12), fg="#333", bg="#f0f0f0")  # dark gray font on light gray background
        self.number_digits_label.pack()
        self.number_digits_entry = tk.Entry(self.window, width=20, font=("Helvetica", 12), fg="#333", bg="#fff")  # white background with dark gray font
        self.number_digits_entry.pack()
