import customtkinter as ctk
from PIL import Image  # For loading images
import sqlite3
import subprocess
import re
from tkinter import messagebox

# Create the SQLite database and table
def create_db():
    conn = sqlite3.connect('database/user_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    email TEXT PRIMARY KEY,
                    password TEXT)''')
    conn.commit()
    conn.close()

# Validate email format
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Validate password strength
def is_valid_password(password):
    return (
        len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    )

# Register a new user with validations
def register_user():
    email = entry_email.get().strip()
    password = entry_password.get()

    if not email or not password:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    if not is_valid_email(email):
        messagebox.showwarning("Invalid Email", "Please enter a valid email address.")
        return

    if not is_valid_password(password):
        messagebox.showwarning(
            "Weak Password",
            "Password must be at least 8 characters long, "
            "contain a number, an uppercase letter, and a special character."
        )
        return

    try:
        conn = sqlite3.connect('database/user_data.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Registration Successful", "You have successfully registered!")
        register_window.destroy()
        subprocess.run(["python", "cartoonify.py"])
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email already registered.")

# Navigate to Login Screen
def navigate_to_login():
    register_window.destroy()
    subprocess.run(["python", "login.py"])

# Registration screen
def register_screen():
    global register_window, entry_email, entry_password

    # Initialize customTkinter
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    register_window = ctk.CTk()
    register_window.title("Register")
    register_window.geometry(f"{register_window.winfo_screenwidth()}x{register_window.winfo_screenheight()}+0+0")
    register_window.configure(bg="white")

    # Load icons
    email_icon = ctk.CTkImage(Image.open("../assets/email1.png"), size=(20, 20))
    password_icon = ctk.CTkImage(Image.open("../assets/password1.png"), size=(20, 20))

    # Create a frame to center the form
    form_frame = ctk.CTkFrame(register_window, bg_color="white", corner_radius=10, width=500, height=450)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Title
    title_label = ctk.CTkLabel(
        form_frame,
        text="Register",
        font=ctk.CTkFont(size=20, weight="bold"),
        text_color="#3A86FF"  # Apply color
    )
    title_label.pack(pady=20)

    # Email Entry with Label
    email_label = ctk.CTkLabel(form_frame, text="Email:", image=email_icon, compound="left", anchor="w")
    email_label.pack(pady=(10, 5), anchor="w")
    entry_email = ctk.CTkEntry(form_frame, placeholder_text="Enter your email", width=300)  # Wider textbox
    entry_email.pack(pady=(0, 10), padx=20, fill="x")

    # Password Entry with Label
    password_label = ctk.CTkLabel(form_frame, text="Password:", image=password_icon, compound="left", anchor="w")
    password_label.pack(pady=(10, 5), anchor="w")
    entry_password = ctk.CTkEntry(form_frame, placeholder_text="Enter your password", show="*", width=300)  # Wider textbox
    entry_password.pack(pady=(0, 10), padx=20, fill="x")

    # Register Button
    register_button = ctk.CTkButton(form_frame, text="Register", command=register_user)
    register_button.pack(pady=20)

    # Login Redirect Label
    login_label = ctk.CTkLabel(
        form_frame,
        text="Take me to Login",
        text_color="#3A86FF",  # Apply color
        cursor="hand2",
    )
    login_label.pack(pady=10)
    login_label.bind("<Button-1>", lambda e: navigate_to_login())

    register_window.mainloop()

# Initialize the database and open the registration screen
create_db()
register_screen()
