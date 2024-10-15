import tkinter as tk
from tkinter import messagebox,filedialog
from user_profile import UserManager
import os

class User:
    """Represents a user profile."""

    def __init__(self, email, first_name, last_name, profile_pic, cover_pic, posts=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.profile_pic = profile_pic
        self.cover_pic = cover_pic
        self.posts = posts if posts else [ ]

    def add_post(self, post):
        """Add a post to the user's profile."""
        self.posts.append(post)


class LoginPage(tk.Frame):
    """Handles the Login functionality."""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.frame = tk.Frame( bg="#87CEEB" )  # Light blue background
        self.frame.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(self.frame, text="Login", font=("Arial", 14), bg="darkblue", fg= "white")
        label.pack(pady=20)

        tk.Label(self.frame, text="Email", bg="#87CEEB", fg="white").pack(pady=5)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.pack(pady=5)

        tk.Label(self.frame, text="Password", bg="#87CEEB", fg="white").pack(pady=5)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack(pady=5)

        login_button = tk.Button(self.frame, text="Login", command=self.sign_in, bg="#4682B4", fg="white")
        login_button.pack(pady=20)

        back_button = tk.Button(self.frame, text="Back", command=self.controller.show_main_menu, bg="#4682B4", fg="white")
        back_button.pack(pady=5)

    def sign_in(self):
        """Validate the user's credentials and login."""
        email = self.email_entry.get()
        password = self.password_entry.get()
        users = UserManager.get_users()
        if email in users and users[email]['password'] == password:
            messagebox.showinfo("Success", "Successful Login")
            self.controller.open_home_page(email)
        else:
            messagebox.showerror("Error", "Invalid email or password!")

    def destroy(self):
        self.frame.destroy()


class RegisterPage:
    """Handles the Registration functionality."""

    def __init__(self, root, app):
        self.root = root
        self.app = app  # Main app instance
        self.frame = tk.Frame(self.root, bg="#87CEEB")  # Light blue background
        self.frame.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(self.frame, text="Register", font=("Arial", 14), bg="darkblue", fg="white")
        label.pack(pady=10)

        tk.Label(self.frame, text="First Name", bg="#87CEEB", fg="white").pack(pady=5)
        self.first_name_entry = tk.Entry(self.frame)
        self.first_name_entry.pack(pady=5)

        tk.Label(self.frame, text="Last Name", bg="#87CEEB", fg="white").pack(pady=5)
        self.last_name_entry = tk.Entry(self.frame)
        self.last_name_entry.pack(pady=5)

        tk.Label(self.frame, text="Email", bg="#87CEEB", fg="white").pack(pady=5)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.pack(pady=5)

        tk.Label(self.frame, text="Password", bg="#87CEEB", fg="white").pack(pady=5)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack(pady=5)

        # Button to choose profile picture
        self.profile_pic_path = None  # Default to None
        self.profile_pic_button = tk.Button(self.frame, text="Choose Profile Photo", command=self.choose_profile_photo, bg="#4682B4", fg="white")
        self.profile_pic_button.pack(pady=10)

        # Button to choose cover photo
        self.cover_pic_path = None  # Default to None
        self.cover_pic_button = tk.Button(self.frame, text="Choose Cover Photo", command=self.choose_cover_photo, bg="#4682B4", fg="white")
        self.cover_pic_button.pack(pady=10)

        register_button = tk.Button(self.frame, text="Register", command=self.register, bg="#4682B4", fg="white")
        register_button.pack(pady=20)

        back_button = tk.Button(self.frame, text="Back", command=self.app.show_main_menu, bg="#4682B4", fg="white")
        back_button.pack(pady=5)

    def choose_profile_photo(self):
        """Allow the user to choose a profile photo."""
        file_path = filedialog.askopenfilename(
            title="Choose a Profile Photo",
            filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"))
        )
        if file_path:
            self.profile_pic_path = file_path  # Store the selected profile picture path
            messagebox.showinfo("Photo Selected", f"Profile photo selected: {os.path.basename(file_path)}")
        else:
            self.profile_pic_path = None

    def choose_cover_photo(self):
        """Allow the user to choose a cover photo."""
        file_path = filedialog.askopenfilename(
            title="Choose a Cover Photo",
            filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
        )
        if file_path:
            self.cover_pic_path = file_path  # Store the selected cover picture path
            messagebox.showinfo("Photo Selected", f"Cover photo selected: {os.path.basename(file_path)}")
        else:
            self.cover_pic_path = None

    def register(self):
        """Register a new user."""
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not all([first_name, last_name, email, password]):
            messagebox.showerror("Error", "All fields are required")
            return

        users = UserManager.get_users()
        if email in users:
            messagebox.showerror("Error", "Email is already registered")
        else:
            # Set default profile and cover photos if none are chosen
            default_profile_pic = "defaultProf.jpg"
            default_cover_pic = "defaultCov.png"
            if self.profile_pic_path:
                profile_pic = self.profile_pic_path
            else:
                profile_pic = default_profile_pic

            if self.cover_pic_path:
                cover_pic = self.cover_pic_path
            else:
                cover_pic = default_cover_pic
            users[email] = {
                'first_name': first_name,
                'last_name': last_name,
                'password': password,
                'profile_pic': profile_pic,
                'cover_pic': cover_pic,
                'posts': {
                    "1": {
                        "content": "Welcome to my profile! This is my first post.",
                        "likes": 0,
                        "comment": [],
                        "date": "29/9/2024"
                    }
                }
            }
            UserManager.save_users(users)
            messagebox.showinfo("Success", "Registration successful")
            self.app.show_main_menu()

    def destroy(self):
        self.frame.destroy()
