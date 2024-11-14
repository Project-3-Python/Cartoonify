from customtkinter import set_appearance_mode, set_default_color_theme

# Define the primary colors and fonts for the theme
PRIMARY_COLOR = "#FFAA00"  # Primary accent color (e.g., a warm orange)
BACKGROUND_COLOR = "#1E1E1E"  # Background color for dark mode
TEXT_COLOR = "#FFFFFF"  # Default text color
BUTTON_COLOR = "#FFAA00"  # Button color (same as primary)
BUTTON_HOVER_COLOR = "#FFCC66"  # Button hover color
FONT = ("Helvetica", 12)  # Default font

# Function to apply theme to CustomTkinter widgets
def apply_theme():
    set_appearance_mode("dark")  # "dark", "light" or "system"
    set_default_color_theme("dark-blue")  # You can also set custom themes here
