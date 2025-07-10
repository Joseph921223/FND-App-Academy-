import tkinter as tk
from tkinter import messagebox
import re
import json
import os

def submit_details():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    address = address_entry.get("1.0", "end").strip()

    # Email validation using regex
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showwarning("Invalid Email", "Please enter a valid email address.")
        return

    if not name or not age or not email or gender == "Select Gender" or not address:
        messagebox.showwarning("Missing Information", "Please fill in all the fields.")
    else:
        messagebox.showinfo("Submitted",
                            f"Name: {name}\nAge: {age}\nEmail: {email}\nGender: {gender}\nAddress: {address}")
        
        # Save data to JSON file
        user_data = {
            "name": name,
            "age": age,
            "email": email,
            "gender": gender,
            "address": address
        }

        # Check if the JSON file exists
        if os.path.exists("user_data.json"):
            with open("user_data.json", "r") as file:
                data = json.load(file)
        else:
            data = []

        # Append new user data to the list
        data.append(user_data)

        # Save data back to JSON file
        with open("user_data.json", "w") as file:
            json.dump(data, file, indent=4)

        # Clear fields after submission
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        gender_var.set("Select Gender")
        address_entry.delete("1.0", tk.END)

# Create the main application window
window = tk.Tk()
window.title("eSim")
window.geometry("400x500")

# Create a label widget
tk.Label(window, text="Connect with us", font=("Arial", 16)).pack(pady=10)

# Name
tk.Label(window, text="Enter your name:").pack(pady=5)
name_entry = tk.Entry(window, width=40)
name_entry.pack()

# Age
tk.Label(window, text="Enter your age:").pack(pady=5)
age_entry = tk.Entry(window, width=40)
age_entry.pack()

# Email
tk.Label(window, text="Enter your email:").pack(pady=5)
email_entry = tk.Entry(window, width=40)
email_entry.pack()

# Gender
tk.Label(window, text="Select your gender:").pack(pady=5)
gender_var = tk.StringVar()
gender_var.set("Select Gender")  # default value
gender_dropdown = tk.OptionMenu(window, gender_var, "Male", "Female", "Other")
gender_dropdown.config(width=30)
gender_dropdown.pack()

# Address
tk.Label(window, text="Enter your address:").pack(pady=5)
address_entry = tk.Text(window, height=4, width=30)
address_entry.pack()

# Submit Button
tk.Button(window, text="Submit", command=submit_details).pack(pady=20)

# Run the application
window.mainloop()