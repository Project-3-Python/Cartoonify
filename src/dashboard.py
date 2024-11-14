import customtkinter as ctk
from cartoonify import cartoonify_image

class DashboardScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        self.upload_button = ctk.CTkButton(self, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=20)

        self.cartoonify_button = ctk.CTkButton(self, text="Cartoonify Image", command=self.cartoonify_image)
        self.cartoonify_button.pack(pady=20)
        
    def upload_image(self):
        # Logic to upload image (placeholder for now)
        pass

    def cartoonify_image(self):
        # Call the cartoonify_image function
        cartoonify_image(self.uploaded_image_path)
