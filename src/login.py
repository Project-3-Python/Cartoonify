import customtkinter as ctk
import sqlite3

class LoginScreen(ctk.CTkFrame):
    def __init__(self, master, switch_to_dashboard):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        # Username and Password fields
        self.username_label = ctk.CTkLabel(self, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.pack(pady=5)
        
        self.password_label = ctk.CTkLabel(self, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.pack(pady=5)

        # Login button
        self.login_button = ctk.CTkButton(self, text="Login", command=switch_to_dashboard)
        self.login_button.pack(pady=20)
