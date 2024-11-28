import tkinter as tk
from tkinter import messagebox
import re

def assess_password_strength(password):
    has_numbers = any(char.isdigit() for char in password)
    has_upper_case = any(char.isupper() for char in password)
    has_lower_case = any(char.islower() for char in password)
    meets_length_requirement = len(password) >= 8
    has_special_characters = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    met_criteria_count = sum([has_numbers, has_upper_case, has_lower_case, meets_length_requirement, has_special_characters])

    if met_criteria_count == 5:
        return "Password Strength Level: Very Strong (All criteria are met).", "green"
    elif met_criteria_count == 4:
        return "Password Strength Level: Strong (Any 4 criteria are met).", "blue"
    elif met_criteria_count == 3:
        return "Password Strength Level: Moderately Strong (Any 3 criteria are met).", "orange"
    else:
        return "Password Strength Level: Weak (None or only one criterion is met).", "red"

def show_password_strength():
    password = entry_password.get()
    result, color = assess_password_strength(password)
    masked_password = password[0] + '#' * (len(password) - 2) + password[-1] if len(password) > 2 else password
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Entered Password: {masked_password}\n", "black")
    output_text.insert(tk.END, f"{result}\n", color)

def show_tips():
    tips = [
        "Here are some quick tips for creating a secure password:",
        "1. Length: Aim for at least 12 characters.",
        "2. Mix Characters: Use a combination of uppercase, lowercase, numbers, and symbols.",
        "3. Avoid Common Words: Don't use easily guessable information.",
        "4. No Personal Info: Avoid using names, birthdays, or personal details.",
        "5. Use Passphrases: Consider combining multiple words or a sentence.",
        "6. Unique for Each Account: Don't reuse passwords across multiple accounts.",
        "7. Regular Updates: Change passwords periodically.",
        "8. Enable 2FA: Use Two-Factor Authentication where possible.",
        "9. Be Wary of Phishing: Avoid entering passwords on suspicious sites.",
        "10. Password Manager: Consider using one for secure and unique passwords."
    ]
    
    tips_text = "\n".join(tips)
    tips_text_widget.delete(1.0, tk.END)
    tips_text_widget.insert(tk.END, tips_text, "blue")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="Password Strength Checker", font=("Helvetica", 16), bg="#f0f0f0")
title_label.pack(pady=10)

author_label = tk.Label(root, text="Author: 0xgh057r3c0n | Version: 1.0", font=("Helvetica", 10, "bold"), bg="#f0f0f0", fg="#ff6347")
author_label.pack(pady=5)

instruction_label = tk.Label(root, text="Enter your password below:", font=("Helvetica", 12), bg="#f0f0f0")
instruction_label.pack(pady=5)

entry_password = tk.Entry(root, font=("Helvetica", 12), show="*")
entry_password.pack(pady=10, padx=20, fill='x')

check_button = tk.Button(root, text="Check Password Strength", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=show_password_strength)
check_button.pack(pady=5)

output_text = tk.Text(root, font=("Helvetica", 12), height=5, width=50)
output_text.pack(pady=10)
output_text.tag_configure("green", foreground="green")
output_text.tag_configure("blue", foreground="blue")
output_text.tag_configure("orange", foreground="orange")
output_text.tag_configure("red", foreground="red")
output_text.tag_configure("black", foreground="black")

tips_button = tk.Button(root, text="Show Tips for a Strong Password", font=("Helvetica", 12), bg="#2196F3", fg="white", command=show_tips)
tips_button.pack(pady=5)

tips_text_widget = tk.Text(root, font=("Helvetica", 10), height=10, width=50)
tips_text_widget.pack(pady=10)
tips_text_widget.tag_configure("blue", foreground="blue")

root.mainloop()
