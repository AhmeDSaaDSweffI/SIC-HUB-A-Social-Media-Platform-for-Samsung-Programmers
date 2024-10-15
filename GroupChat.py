import json
import tkinter as tk
from tkinter import scrolledtext, messagebox
from PIL import Image, ImageTk
from datetime import datetime


class GroupChatPage(tk.Frame):
    def __init__(self, parent, controller, user_email):
        tk.Frame.__init__(self, parent)
        self.user_email = user_email
        self.controller = controller
        self.configure(bg="#87CEEB")  # Blue theme

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Group Chat", font=("Arial", 16, 'bold'), bg="#4682b4", fg="white")
        label.pack(pady=10)

        # Frame for chat display
        self.chat_frame = tk.Frame(self, bg="#e6f2ff")
        self.chat_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Display chat messages in a scrolled text widget
        self.chat_display = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD, width=50, height=15, bg="#ffffff", state='disabled')
        self.chat_display.pack(fill="both", expand=True)

        # Load group chat messages from JSON
        self.load_group_chat()

        # Frame for input
        input_frame = tk.Frame(self, bg="#87CEEB")
        input_frame.pack(pady=5)

        self.message_entry = tk.Entry(input_frame, width=40, bg="#ffffff", font=("Arial", 12))
        self.message_entry.pack(side=tk.LEFT, padx=5)

        send_button = tk.Button(input_frame, text="Send", command=self.send_message, bg="#4682b4", fg="white")
        send_button.pack(side=tk.LEFT)

        # Back to Home button
        back_button = tk.Button(self, text="Back to Home", command=self.back_to_home, bg="#4682b4", fg="white")
        back_button.pack(pady=10)

    def load_group_chat(self):
        """Load group chat messages from the JSON file and display them."""
        try:
            with open('group_chat.json', 'r') as file:
                data = json.load(file)

            self.chat_display.config(state='normal')  # Enable editing to insert text
            for message in data["group_chat"]:
                user_label = f"{message['sender']}: {message['message']} ({message['timestamp']})\n"
                if message['sender'] == "your_email@example.com":  # Replace with actual user email
                    self.chat_display.insert(tk.END, f"You: {message['message']} ({message['timestamp']})\n")
                else:
                    self.chat_display.insert(tk.END, f"{message['sender']}: {message['message']} ({message['timestamp']})\n")
            self.chat_display.config(state='disabled')  # Disable editing to prevent user changes
            self.chat_display.yview(tk.END)  # Scroll to the bottom

        except FileNotFoundError:
            self.chat_display.config(state='normal')
            self.chat_display.insert(tk.END, "No group chat messages yet.\n")
            self.chat_display.config(state='disabled')

    def send_message(self):
        """Send a message and save it to the JSON file."""
        new_message = self.message_entry.get()
        if new_message:
            sender_email = "your_email@example.com"  # Replace with the current user's email
            timestamp = self.get_timestamp()

            # Insert new message in the chat display
            self.chat_display.config(state='normal')
            self.chat_display.insert(tk.END, f"You: {new_message} ({timestamp})\n")
            self.chat_display.config(state='disabled')
            self.chat_display.yview(tk.END)

            # Save the message to JSON
            self.save_message(sender_email, new_message, timestamp)

            # Clear the message entry
            self.message_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a message.")

    def save_message(self, sender, message, timestamp):
        """Save the new message to the group chat JSON file."""
        try:
            with open('group_chat.json', 'r') as file:
                data = json.load(file)

            new_entry = {"sender": sender, "message": message, "timestamp": timestamp}
            data["group_chat"].append(new_entry)

            with open('group_chat.json', 'w') as file:
                json.dump(data, file, indent=4)

        except FileNotFoundError:
            messagebox.showerror("Error", "Could not save message.")

    def get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")

    def back_to_home(self):
        self.controller.open_home_page(self.user_email)
