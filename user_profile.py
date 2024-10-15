import tkinter as tk
from PIL import Image, ImageTk
import json
from tkinter import messagebox, filedialog
import os

class UserManager:
    """Handles loading and saving user data."""
    USERS_FILE = "users.json"

    @staticmethod
    def get_users():
        """Retrieve users from the file."""
        try:
            with open(UserManager.USERS_FILE, "r") as f:
                users = json.load(f)
                return users
        except FileNotFoundError:
            return {}

    @staticmethod
    def save_users(users):
        """Save users to the file."""
        with open(UserManager.USERS_FILE, "w") as f:
            json.dump(users, f, indent=4)


class UserProfilePage(tk.Frame):
    def __init__(self, parent, controller, user_email):
        super().__init__(parent)
        self.user_email = user_email
        self.controller = controller
        self.configure(bg="#f0f8ff")
        self.pack(fill="both", expand=True)

        # Load user data
        user_data = self.load_user_data(user_email)
        if user_data:
            # Display Cover Photo
            if user_data.get("cover_pic") and os.path.exists(user_data["cover_pic"]):
                self.display_cover_photo(user_data["cover_pic"])

            # Display Profile Picture
            if user_data.get("profile_pic") and os.path.exists(user_data["profile_pic"]):
                self.display_profile_picture(user_data["profile_pic"])

            # User full name
            tk.Label(self, text=f"{user_data['first_name']} {user_data['last_name']}",
                     font=("Helvetica", 16, "bold"), bg="#4682b4", fg="white").pack(pady=10, padx=20)

            # Posts Section
            tk.Label(self, text="Posts:", font=("Helvetica", 14, "bold"), bg="#f0f8ff").pack(anchor="w", padx=20, pady=10)

            posts_frame = tk.Frame(self, bg="#f0f8ff")
            posts_frame.pack(padx=20, pady=10, fill="both", expand=True)

            # Add post functionality
            add_post_button = tk.Button(posts_frame, text="Add Post", font=("Helvetica", 10), bg="#4682b4", fg="white",
                                        command=lambda: self.add_post_window())
            add_post_button.pack(pady=10)

            back_to_main_button = tk.Button(posts_frame, text="Back to Main", font=("Helvetica", 10), bg="#4682b4", fg="white",
                                            command=self.back)
            back_to_main_button.pack(padx=10)

            # Load posts
            for post_id, post in user_data["posts"].items():
                self.create_post_frame(posts_frame, post, post_id)

    def back(self):
        self.controller.open_home_page(user_email=self.user_email)

    def add_post_window(self):
        """Open a new window to add a post."""
        add_post_window = tk.Toplevel(self)
        add_post_window.title("Add New Post")

        tk.Label(add_post_window, text="New Post Content:").pack(pady=10)
        post_content_entry = tk.Entry(add_post_window, width=50)
        post_content_entry.pack(pady=5)

        # Add image selection button
        image_path_var = tk.StringVar()
        tk.Button(add_post_window, text="Select Image", command=lambda: self.select_image(image_path_var)).pack(pady=5)

        tk.Button(add_post_window, text="Add Post",
                  command=lambda: self.add_post(post_content_entry.get(), image_path_var.get(), add_post_window)).pack(pady=10)

    def select_image(self, image_path_var):
        """Allow user to select an image."""
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            image_path_var.set(file_path)

    def add_post(self, post_content, image_path, window):
        """Add a post to the user's profile."""
        if post_content:
            user_data = self.load_user_data(self.user_email)

            # Assign a new post ID
            new_post_id = str(len(user_data['posts']) + 1)
            user_data['posts'][new_post_id] = {
                "content": post_content,
                "likes": 0,
                "comment": [],
                "date": "17/10/2024",  # You can use the current date here if needed
                "image": image_path if image_path else None  # Store image path if provided
            }

            self.save_user_data(user_data)
            messagebox.showinfo("Post Added", "Your post has been added!")
            window.destroy()
            self.refresh_profile()

    def load_user_data(self, email):
        """Load user data from the JSON file."""
        try:
            with open(UserManager.USERS_FILE, 'r') as file:
                users = json.load(file)
            return users.get(email)
        except FileNotFoundError:
            messagebox.showerror("Error", "User data file not found.")
            return {}

    def display_cover_photo(self, cover_pic_path):
        """Display the user's cover photo."""
        image = Image.open(cover_pic_path)
        image = image.resize((200, 100), Image.LANCZOS)
        cover_photo = ImageTk.PhotoImage(image)

        cover_label = tk.Label(self, image=cover_photo)
        cover_label.image = cover_photo  # Keep a reference to avoid garbage collection
        cover_label.pack()

    def display_profile_picture(self, profile_pic_path):
        """Display the user's profile picture."""
        image = Image.open(profile_pic_path)
        image = image.resize((50, 50), Image.LANCZOS)
        profile_photo = ImageTk.PhotoImage(image)

        profile_label = tk.Label(self, image=profile_photo, bg="#f0f8ff")
        profile_label.image = profile_photo  # Keep a reference to avoid garbage collection
        profile_label.pack(pady=10)

    def create_post_frame(self, parent, post, post_id):
        """Create a frame for displaying a user's post."""
        post_frame = tk.Frame(parent, bg="#ffffff", bd=2, relief="ridge", padx=10, pady=10)
        post_frame.pack(pady=10, fill="x")

        # Post content
        content_label = tk.Label(post_frame, text=post['content'], bg="#ffffff", font=("Helvetica", 12),
                                 wraplength=500, justify="left")
        content_label.pack(anchor="w")

        # Display image if present
        if post.get('image') and os.path.exists(post['image']):
            image = Image.open(post['image'])
            image = image.resize((200, 150), Image.LANCZOS)  # Resize the image
            post_image = ImageTk.PhotoImage(image)

            image_label = tk.Label(post_frame, image=post_image, bg="#ffffff")
            image_label.image = post_image  # Keep a reference to avoid garbage collection
            image_label.pack(anchor="w")

        # Post likes and comments
        likes_comments = f"Likes: {post['likes']} | Date: {post['date']}"
        post_details_label = tk.Label(post_frame, text=likes_comments, bg="#ffffff", font=("Helvetica", 10), fg="gray")
        post_details_label.pack(anchor="w")

        # Comments
        for comment in post['comment']:
            comment_label = tk.Label(post_frame, text=f"Comment: {comment}", bg="#f0f8ff",
                                     font=("Helvetica", 10, "italic"))
            comment_label.pack(anchor="w", padx=10)

        # Like Button
        like_button = tk.Button(post_frame, text="Like", font=("Helvetica", 10), bg="#4682b4", fg="white",
                                command=lambda: self.like_post(post_id))
        like_button.pack(side="left", pady=5, padx=5)

        # Add Comment Section
        comment_entry = tk.Entry(post_frame, font=("Helvetica", 10))
        comment_entry.pack(side="left", padx=10)
        add_comment_button = tk.Button(post_frame, text="Add Comment", font=("Helvetica", 10), bg="#4682b4", fg="white",
                                       command=lambda: self.add_comment(post_id, comment_entry.get()))
        add_comment_button.pack(side="left", padx=5)

        # Delete Post Button
        delete_button = tk.Button(post_frame, text="Delete Post", font=("Helvetica", 10), bg="red", fg="white",
                                  command=lambda: self.delete_post(post_id, post_frame))
        delete_button.pack(side="right", padx=5)

    def delete_post(self, post_id, post_frame):
        """Delete a post from the user's profile."""
        user_data = self.load_user_data(self.user_email)

        # Remove the post from the user's data
        if post_id in user_data["posts"]:
            del user_data["posts"][post_id]
            self.save_user_data(user_data)
            messagebox.showinfo("Post Deleted", "Your post has been deleted!")
            post_frame.destroy()  # Remove the post frame from the UI
            self.refresh_profile()  # Refresh the profile to update the view
        else:
            messagebox.showerror("Error", "Post not found.")
    def like_post(self, post_id):
        """Handle liking a post."""
        user_data = self.load_user_data(self.user_email)
        user_data["posts"][post_id]["likes"] += 1
        self.save_user_data(user_data)
        messagebox.showinfo("Liked", "You liked this post!")
        self.refresh_profile()

    def add_comment(self, post_id, comment):
        """Handle adding a comment."""
        if comment:
            try:
                user_data = self.load_user_data(self.user_email)
                user_data["posts"][post_id]["comment"].append(comment)
                self.save_user_data(user_data)
                messagebox.showinfo("Comment Added", "Your comment has been added!")
                self.refresh_profile()
            except Exception as e:
                messagebox.showerror("Error", f"Error adding comment: {e}")

    def refresh_profile(self):
        """Refresh the profile page."""
        parent = self.master  # Get the parent widget
        self.destroy()  # Destroy the current frame
        self.__init__(parent, self.controller, self.user_email)  # Reinitialize the frame correctly

    def save_user_data(self, data):
        """Save user data to the JSON file."""
        users = UserManager.get_users()
        users[self.user_email] = data
        UserManager.save_users(users)
