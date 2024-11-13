import customtkinter as ctk
from src.splash import SplashScreen
from src.login import LoginScreen
from src.register import RegisterScreen
from src.dashboard import DashboardScreen

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

if __name__ == "__main__":
    main()
