import customtkinter as ctk
import time

class SplashScreen(ctk.CTkFrame):
    def __init__(self, master, switch_to_login):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        
        # Display a welcome message or logo
        self.label = ctk.CTkLabel(self, text="Welcome to Cartoonify App", font=("Arial", 24))
        self.label.pack(pady=100)
        
        # Delay before switching to login
        self.after(3000, switch_to_login)
