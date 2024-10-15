import tkinter as tk
from user_auth import LoginPage, RegisterPage
from user_profile import UserProfilePage
from mainPage import SocialMediaHomePage
from PIL import Image, ImageTk
from GroupChat import GroupChatPage


class SocialMediaApp:
    """Main application controller."""
    def __init__(self, root):
        self.root = root
        self.root.title("Social Media App")
        self.root.geometry("400x600")
        self.current_page = None
        self.show_main_menu()

    def show_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.current_page = tk.Frame(self.root, bg="#87CEEB")
        self.current_page.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(self.current_page, text="Welcome to SIC Hub!", font=("Arial", 14),
                         bg="darkblue", fg= "white")  # Match label backgroun
        label.pack(pady=20)

        try:
            image = Image.open("logooo.jpg")  # Update this path to your image
            image = image.resize((400, 400),Image.LANCZOS)  # Resize image (optional)
            self.photo = ImageTk.PhotoImage(image)  # Create PhotoImage from the image
            image_label = tk.Label(self.current_page, image=self.photo, bg="#87CEEB")
            image_label.pack(pady=10)
        except Exception as e:
            print(f"Error loading image: {e}")


        login_button = tk.Button(self.current_page, text="Login", command=self.show_login_page, width=20, height=2,
                                 bg="#4682B4", fg="white")  # Darker blue button
        login_button.pack(pady=10)

        register_button = tk.Button(self.current_page, text="Register", command=self.show_register_page, width=20,
                                    height=2, bg="#4682B4", fg="white")  # Darker blue button
        register_button.pack(pady=10)

    def show_login_page(self):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = LoginPage(self.root, self)

    def show_register_page(self):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = RegisterPage(self.root, self)

    def open_user_profile(self, user_email):
        """Display the user's profile in the main window."""
        for widget in self.root.winfo_children():
            widget.destroy()

            # Load the ProfilePage with the correct email
        profile_page = UserProfilePage(self.root,self,user_email)
        profile_page.pack(fill="both", expand=True)

    def open_home_page(self, user_email):
        self.user_email = user_email
        for widget in self.root.winfo_children():
            widget.destroy()

            # Load the ProfilePage with the correct email
        profile_page = SocialMediaHomePage(self.root, self, user_email)
        profile_page.pack(fill="both", expand=True)

    def show_group_chat(self, user_email):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.current_page = GroupChatPage(self.root, self, user_email)
        self.current_page.pack(fill="both", expand=True)



root = tk.Tk()
app = SocialMediaApp(root)
root.mainloop()
