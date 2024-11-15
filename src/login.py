import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess
import customtkinter as ctk
import tkinter.messagebox as tkmb
from tkinter import PhotoImage  # Import to handle image loading

# Set the appearance mode and default color theme
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

# Function to login an existing user
def login_user():
    email = entry_login_email.get()
    password = entry_login_password.get()

    conn = sqlite3.connect('database/user_data.db')
    c = conn.cursor()
    # Check both email and password
    c.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = c.fetchone()  # Fetch one matching record
    conn.close()

    if user:
        messagebox.showinfo("Login Successful", "You have successfully logged in!")
        login_window.destroy()  # Close the login window
        subprocess.run(["python", "dashboard.py"])  # Open welcome1 screen
    else:
        messagebox.showerror("Login Failed", "Invalid email or password.")

# Function to open Register.py
def open_register():
    subprocess.run(["python", "Register.py"])

# Login screen
def login_screen():
    global login_window, entry_login_email, entry_login_password
    login_window = ctk.CTk()  # Use CTk instead of Tk for the main window
    login_window.title("Login")

    # Set the window to maximize on start but allow resizing
    login_window.geometry(f"{login_window.winfo_screenwidth()}x{login_window.winfo_screenheight()}+0+0")
    
    # Allow resizing
    login_window.resizable(True, True)

    # Create a frame for the login form
    frame = ctk.CTkFrame(login_window)
    frame.place(relx=0.5, rely=0.5, anchor='center')  # Position it at the center

    # Add widgets to the frame
    ctk.CTkLabel(frame, text="Welcome back", font=("Arial", 18), text_color="#3A86FF").grid(row=0, columnspan=2, pady=10)

    # Email label with icon
    email_icon = PhotoImage(file="../assets/email1.png")  # Load email icon
    email_icon = email_icon.subsample(3, 3)  # Scale the icon down (adjust values as needed)
    email_label = ctk.CTkLabel(frame, text="Email:", image=email_icon, compound="left")
    email_label.image = email_icon  # Keep a reference to the image
    email_label.grid(row=1, column=0, padx=5, pady=10, sticky="w")  # Align label to the left
    
    # Email entry below the label with wider width
    entry_login_email = ctk.CTkEntry(frame, width=300)  # Set width for the textbox
    entry_login_email.grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky="w")  # Align textbox to the left

    # Password label with scaled icon aligned with the textbox
    password_icon = PhotoImage(file="../assets/password1.png")  # Load password icon
    password_icon = password_icon.subsample(3, 3)  # Scale the icon down (adjust values as needed)
    password_label = ctk.CTkLabel(frame, text="Password:", image=password_icon, compound="left")
    password_label.image = password_icon  # Keep a reference to the image
    password_label.grid(row=3, column=0, padx=5, pady=10, sticky="w")  # Align label to the left
    
    # Password entry below the label with wider width
    entry_login_password = ctk.CTkEntry(frame, show="*", width=300)  # Set width for the textbox
    entry_login_password.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky="w")  # Align textbox to the left

    # Login button with custom color #3A86FF
    ctk.CTkButton(frame, text="Login", command=login_user, fg_color="#3A86FF", hover_color="#3A86FF").grid(row=5, columnspan=2, pady=10)

    # "Don't have an account? Register here" link
    register_label = ctk.CTkLabel(frame, text="Don't have an account? Register here", text_color="#3A86FF", cursor="hand2")
    register_label.grid(row=6, columnspan=2, pady=10)
    register_label.bind("<Button-1>", lambda e: open_register())  # Bind click event to open Register.py

    login_window.mainloop()

login_screen()
