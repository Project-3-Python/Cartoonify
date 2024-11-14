import customtkinter as ctk

class RegisterScreen(ctk.CTkFrame):
    def __init__(self, master, switch_to_login):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        # Registration form elements
        self.username_label = ctk.CTkLabel(self, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.pack(pady=5)

        self.email_label = ctk.CTkLabel(self, text="Email:")
        self.email_label.pack(pady=5)
        self.email_entry = ctk.CTkEntry(self)
        self.email_entry.pack(pady=5)

        self.password_label = ctk.CTkLabel(self, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.pack(pady=5)

        # Register button
        self.register_button = ctk.CTkButton(self, text="Register", command=self.register_user)
        self.register_button.pack(pady=20)

        # Link to login page
        self.login_link = ctk.CTkButton(self, text="Already have an account? Login", command=switch_to_login)
        self.login_link.pack(pady=10)

    def register_user(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # In a real app, you would save these credentials securely in a database.
        # For now, just print them.
        print(f"Registered with Username: {username}, Email: {email}, Password: {password}")

        # You can then call a function to switch to the login page
        # This can be done in the switch_to_login function if needed.
