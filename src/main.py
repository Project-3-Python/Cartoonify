import customtkinter as ctk
from splash import SplashScreen
from login import LoginScreen
from register import RegisterScreen
from dashboard import DashboardScreen
import sqlite3
import os
from theme import apply_theme
from customtkinter import CTk, CTkButton, CTkLabel

# Initialize your application and apply theme
app = CTk()
apply_theme()

# Ensure the path to the database file is correct
db_path = os.path.join(os.path.dirname(__file__), "database", "user_data.db")

# Function to save user data (example function)
def save_user_data(user_id, data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (id, data) VALUES (?, ?)", (user_id, data))
    conn.commit()
    conn.close()

# Function to get user data (example function)
def get_user_data(user_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, password_hash FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result


def get_db_connection():
    # Construct the path to the database file
    db_path = os.path.join(os.path.dirname(__file__), 'user_data.db')
    return sqlite3.connect(db_path)


def main():
    app = ctk.CTk() 
    app.geometry("800x600")

    # Show splash screen, then switch to login
    splash = SplashScreen(app)
    splash.after(3000, lambda: switch_to_login(app))  # Adjust timing as needed

    app.mainloop()

def switch_to_login(app):
    login = LoginScreen(app)
    login.pack(fill="both", expand=True)
    # Use a function or button in LoginScreen to trigger switch_to_dashboard

def switch_to_dashboard(app, user_data):
    dashboard = DashboardScreen(app, user_data)
    dashboard.pack(fill="both", expand=True)

# Example usage for registration:
def register_user(username, email, password):
    save_user_data(username, email, password)
    print("User successfully registered.")

# Example usage for login:
def login_user(username, password):
    user_data = get_user_data(username)
    if user_data:
        stored_hash = user_data[3]  # The password hash is stored in the 4th column
        if check_password(stored_hash, password):
            print("Login successful!")
        else:
            print("Invalid password!")
    else:
        print("User not found.")



if __name__ == "__main__":
    main()
