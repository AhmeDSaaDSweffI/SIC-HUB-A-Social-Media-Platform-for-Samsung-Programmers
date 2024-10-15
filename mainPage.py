import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import json
from PIL import Image, ImageTk

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


class SocialMediaHomePage(tk.Frame):
    def __init__(self, parent, controller, user_email):
        super().__init__(parent)
        self.controller = controller  # Controller to switch pages
        self.user_email = user_email  # Logged-in user's email
        self.users = UserManager.get_users()
        self.create_widgets()

    def linear_search(self, query, users):
        """Perform a linear search for users matching the query."""
        results = []
        query_lower = query.lower()  # Convert query to lowercase for case-insensitive search
        for email, user_info in users.items():
            full_name = f"{user_info.get('first_name', '')} {user_info.get('last_name', '')}"
            if query_lower in full_name.lower() or query_lower in email.lower():
                results.append({"email": email, "full_name": full_name})
        return results

    def open_search_popup(self):
        """Open a popup window to handle the search."""
        self.search_popup = tk.Toplevel(self)
        self.search_popup.title("Search User")
        self.search_popup.geometry("400x400")
        self.search_popup.config(bg="#f0f8ff")


        search_label = tk.Label(self.search_popup, text="Search User:")
        search_label.pack(pady=10)

        self.search_entry = tk.Entry(self.search_popup, width=30)  # Define as an instance variable
        self.search_entry.pack(pady=5)

        search_button = tk.Button(self.search_popup, text="Search", command=self.search_user_in_popup)
        search_button.pack(pady=5)

        self.result_listbox = tk.Listbox(self.search_popup, width=50, height=10)  # Define as an instance variable
        self.result_listbox.pack(pady=10)
        # Bind the listbox to open profile when a result is clicked
        self.result_listbox.bind("<<ListboxSelect>>")

    def search_user_in_popup(self):
        """Perform the search and populate the result listbox in the popup."""
        query = self.search_entry.get()  # Get the query from the entry widget

        with open('users.json', 'r') as f:
            users = json.load(f)

        results = self.linear_search(query, users)

        self.result_listbox.delete(0, tk.END)  # Clear previous results

        if results:  # Populate the listbox with results
            for idx, user in enumerate(results):
                # Store the email as part of the listbox entry
                self.result_listbox.insert(tk.END, f"{user['full_name']} ({user['email']})")
                self.result_listbox.user_data = results  # Store the full result for reference later
        else:
            self.result_listbox.insert(tk.END, "No results found.")

    def create_widgets(self):
        self.wrapper_frame = tk.Frame(self, bg="#f0f8ff")
        self.wrapper_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create a frame for the header buttons
        header_frame = tk.Frame(self.wrapper_frame, bg="#f0f8ff")
        header_frame.pack(fill="x", pady=(10, 0))

        # Go to Profile Button
        profile_button = tk.Button(header_frame, text="Go to Profile", font=("Helvetica", 10), bg="#4682b4", fg="white",command=self.go_to_profile)
        profile_button.pack(side="left", padx=10)

        # Log Out Button
        logout_button = tk.Button(header_frame, text="Log Out", font=("Helvetica", 10), bg="#4682b4", fg="white", command=self.logout)
        logout_button.pack(side="left", padx=10)
        group_chat_button = tk.Button(header_frame, text="Group Chat",font=("Helvetica", 10), bg="#4682b4", fg="white", command=self.go_to_group)
        group_chat_button.pack(pady=10)

        self.search_button = tk.Button(header_frame, text="Search User",font=("Helvetica", 10), bg="#4682b4", fg="white", command=self.open_search_popup)
        self.search_button.pack(pady=10)

        # Create a canvas for scrolling
        self.canvas = tk.Canvas(self.wrapper_frame, bg="#f0f8ff")
        self.scrollbar = tk.Scrollbar(self.wrapper_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#f0f8ff")

        # Configure the canvas
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Pack the canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Attach scrollbar to canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Display all users and their posts
        self.display_users_and_posts()

    def display_users_and_posts(self):
        for email, user in self.users.items():
            # Display user's name
            user_name = f"{user['first_name']} {user['last_name']}"
            user_label = tk.Label(self.scrollable_frame, text=user_name, font=("Helvetica", 10, "bold"),  bg="darkblue", fg= "white")
            user_label.pack(pady=10)

            # Container for posts
            posts_frame = tk.Frame(self.scrollable_frame, bg="#f0f8ff")
            posts_frame.pack(fill="both", expand=True)

            # Display posts for each user
            if 'posts' in user and user['posts']:
                for post_id, post in user['posts'].items():
                    self.create_post_frame(posts_frame, post, post_id, email)
            else:
                no_posts_label = tk.Label(posts_frame, text="No posts available.", font=("Helvetica", 12, "italic"),
                                          bg="#f0f8ff")
                no_posts_label.pack(pady=10)

    def create_post_frame(self, parent, post, post_id, user_email):
        """Create a frame for displaying a user's post with an optional image."""
        post_frame = tk.Frame(parent, bg="#ffffff", bd=2, relief="ridge", padx=10, pady=10)
        post_frame.pack(pady=10, fill="x")

        # Post content
        content_label = tk.Label(post_frame, text=post['content'], bg="#ffffff", font=("Helvetica", 12), wraplength=500,
                                 justify="left")
        content_label.pack(anchor="w")

        # Display post image if available
        if post.get('image'):
            img = Image.open(post['image'])  # Open the image file
            img = img.resize((200, 200))  # Resize the image to fit within the frame
            photo = ImageTk.PhotoImage(img)

            image_label = tk.Label(post_frame, image=photo, bg="#ffffff")
            image_label.image = photo  # Keep a reference to avoid garbage collection
            image_label.pack(anchor="w", pady=5)




        # Post likes and date
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
                                command=lambda: self.like_post(user_email, post_id))
        like_button.pack(side="left", pady=5, padx=5)

        # Add Comment Section
        comment_entry = tk.Entry(post_frame, font=("Helvetica", 10))
        comment_entry.pack(side="left", padx=10)

        add_comment_button = tk.Button(post_frame, text="Add Comment", font=("Helvetica", 10), bg="#4682b4", fg="white",
                                       command=lambda: self.add_comment(user_email, post_id, comment_entry.get()))
        add_comment_button.pack(side="left", padx=5)

    def like_post(self, user_email, post_id):
        """Handle liking a post, ensuring that each user can only like once."""
        # Get the specific post by the user
        post = self.users[ user_email ][ 'posts' ][ post_id ]

        # Check if the user has already liked the post
        if user_email in post.get('liked_by', [ ]):
            messagebox.showwarning("Warning", "You have already liked this post.")
            return

        # Add the user to the liked_by list and increment likes
        post[ 'liked_by' ] = post.get('liked_by', [ ])  # Ensure liked_by exists
        post[ 'liked_by' ].append(user_email)
        post[ 'likes' ] += 1

        UserManager.save_users(self.users)  # Save changes to the user data
        messagebox.showinfo("Liked", "You liked this post!")
        self.refresh_posts()  # Refresh the posts to reflect the new like count
    def add_comment(self, user_email, post_id, comment):
        """Handle adding a comment."""
        if comment:
            self.users[user_email]['posts'][post_id]['comment'].append(comment)
            UserManager.save_users(self.users)
            messagebox.showinfo("Comment Added", "Your comment has been added!")
            self.refresh_posts()
        else:
            messagebox.showwarning("Warning", "Comment cannot be empty.")

    def go_to_profile(self):
        self.controller.open_user_profile(self.user_email)

    def go_to_group(self):
        self.controller.show_group_chat(self.user_email)

    def logout(self):
        self.controller.show_main_menu()

    def refresh_posts(self):
        """Refresh the displayed posts."""
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.display_users_and_posts()

#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = SocialMediaHomePage(root)
#     root.mainloop()