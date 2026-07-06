<div align="center">

<!-- Replace the placeholder below with your project logo (e.g. logooo.jpg) -->
<img src="https://via.placeholder.com/160x160.png?text=SIC+HUB" alt="SIC HUB Logo" width="160" height="160" />

# 🌐 SIC HUB

### *A Social Media Platform for Samsung Programmers*

**SIC HUB** is a Python-powered desktop social network built exclusively for Samsung programmers to connect, share, and collaborate inside their own private hub. Post updates, react to your peers, and jump into a shared group chat — all in one lightweight, offline-first application. 🚀

<br />

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FF6F00?style=for-the-badge&logo=windowsterminal&logoColor=white)
![Pillow](https://img.shields.io/badge/Imaging-Pillow-8A2BE2?style=for-the-badge)
![OOP](https://img.shields.io/badge/Design-OOP-1E90FF?style=for-the-badge)
![Storage](https://img.shields.io/badge/Storage-JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)

<br />

![Samsung Innovation Campus](https://img.shields.io/badge/Built%20at-Samsung%20Innovation%20Campus-1428A0?style=for-the-badge&logo=samsung&logoColor=white)

</div>

---

## 📖 Table of Contents

- [✨ Overview](#-overview)
- [🎯 Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📂 Project Structure](#-project-structure)
- [⚙️ Prerequisites](#️-prerequisites)
- [🚀 Installation & Setup](#-installation--setup)
- [🕹️ Usage](#️-usage)
- [🖼️ Screenshots](#️-screenshots)
- [🗄️ Data Model](#️-data-model)
- [🤝 Contributing](#-contributing)
- [🌱 Future Enhancements](#-future-enhancements)
- [👥 Team](#-team)
- [📜 License](#-license)

---

## ✨ Overview

SIC HUB brings the essentials of a social network to the desktop in a clean, self-contained package. Designed as a **private hub for Samsung programmers**, it lets members register with a profile, publish posts (with images), engage through likes and comments, discover other members, and chat together in a shared group room.

The entire application is built on **Object-Oriented Programming (OOP)** principles, with each responsibility isolated into its own class and module. It requires **no database server and no internet connection** — all data is persisted locally in human-readable **JSON** files.

---

## 🎯 Features

| 🔑 Category | Description |
| ----------- | ----------- |
| 🔐 **Authentication** | Secure **Register** and **Login** flow with field validation and duplicate-email checks. |
| 👤 **User Profiles** | Personal profile with **profile picture** and **cover photo** (defaults provided if none chosen). |
| 📝 **Posts** | Create posts with optional images, then **delete** them anytime from your profile. |
| ❤️ **Engagement** | **Like** posts and add **comments** on both the home feed and profile pages. |
| 🏠 **News Feed** | A scrollable home page that aggregates posts from every member of the hub. |
| 🔍 **User Search** | Fast, case-insensitive **linear search** to find members by name or email. |
| 💬 **Group Chat** | A shared, timestamped group chat room that persists across sessions. |
| 🔒 **Private Hub** | An exclusive, offline environment tailored for tech professionals. |
| 💾 **Local Persistence** | All users, posts, and messages stored in editable **JSON** files. |

---

## 🛠️ Tech Stack

| Layer | Technology |
| ----- | ---------- |
| **Language** | 🐍 Python 3.8+ |
| **GUI Framework** | 🪟 Tkinter (standard library) |
| **Image Handling** | 🖼️ Pillow (PIL) |
| **Data Storage** | 🗂️ JSON (local files) |
| **Architecture** | 🧩 Object-Oriented Programming (OOP) |

---

## 📂 Project Structure

```text
SIC-HUB/
│
├── main.py            # 🚪 Entry point — bootstraps the app & controls page navigation
├── mainPage.py        # 🏠 Home page: news feed, likes, comments & user search
├── user_auth.py       # 🔐 Login & Register pages, plus the User model
├── user_profile.py    # 👤 Profile page: view, add & delete posts (UserManager lives here)
├── GroupChat.py       # 💬 Group chat page: send, load & persist messages
│
├── users.json         # 🗄️ User database (credentials, profiles, posts)
└── group_chat.json    # 🗄️ Group chat message log
```

### 🧭 How It Fits Together

- **`main.py`** defines `SocialMediaApp`, the central controller that swaps between pages inside a single Tkinter window.
- **`user_auth.py`** exposes `LoginPage`, `RegisterPage`, and the `User` class.
- **`user_profile.py`** exposes `UserProfilePage` and the shared **`UserManager`** helper used across modules to read/write `users.json`.
- **`mainPage.py`** renders the feed (`SocialMediaHomePage`) and drives search & engagement.
- **`GroupChat.py`** renders `GroupChatPage` and reads/writes `group_chat.json`.

---

## ⚙️ Prerequisites

Before you begin, make sure you have the following installed:

- ✅ **Python 3.8 or higher** — [Download here](https://www.python.org/downloads/)
- ✅ **Tkinter** — bundled with most Python installations (on some Linux distros: `sudo apt-get install python3-tk`)
- ✅ **Pillow** — required for loading and rendering images

> 💡 SIC HUB loads a logo (`logooo.jpg`) and default images (`defaultProf.jpg`, `defaultCov.png`) at runtime. These are optional — the app runs without them (it simply skips missing images), but adding them gives you the full experience.

---

## 🚀 Installation & Setup

Follow these steps to get SIC HUB running locally:

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/SIC-HUB-A-Social-Media-Platform-for-Samsung-Programmers.git
cd SIC-HUB-A-Social-Media-Platform-for-Samsung-Programmers
```

### 2️⃣ (Recommended) Create a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install pillow
```

### 4️⃣ Run the application

```bash
python main.py
```

🎉 The SIC HUB window will launch, greeting you with the welcome screen.

---

## 🕹️ Usage

The typical user journey flows through three stages: **Authenticate → Profile → Connect**.

```text
   ┌──────────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
   │   Welcome    │ ───> │   Register   │ ───> │    Login     │ ───> │  Home Feed   │
   │    Screen    │      │  (new user)  │      │ (credentials)│      │  (news feed) │
   └──────────────┘      └──────────────┘      └──────────────┘      └──────┬───────┘
                                                                            │
                              ┌─────────────────────────────────────────────┼─────────────────┐
                              ▼                        ▼                     ▼                 ▼
                        ┌───────────┐          ┌───────────┐          ┌───────────┐     ┌───────────┐
                        │  Profile  │          │  Search   │          │   Like /  │     │   Group   │
                        │ (posts)   │          │  Users    │          │  Comment  │     │   Chat    │
                        └───────────┘          └───────────┘          └───────────┘     └───────────┘
```

1. **🔐 Register / Login**
   - New members click **Register**, enter their name, email, and password, and optionally pick a profile & cover photo.
   - Returning members click **Login** and enter their credentials.

2. **🏠 Explore the Home Feed**
   - After login you land on the home page showing posts from every member.
   - **Like** posts (one like per user), **add comments**, or use **Search User** to find colleagues by name or email.

3. **👤 Manage Your Profile**
   - Click **Go to Profile** to view your own page.
   - **Add posts** (with optional images) or **delete** existing ones.

4. **💬 Join the Group Chat**
   - Click **Group Chat** to enter the shared room.
   - Type a message and hit **Send** — messages are timestamped and saved to `group_chat.json`, so they persist between sessions.

5. **🚪 Log Out** anytime to return to the welcome screen.

---

## 🖼️ Screenshots

<div align="center">

| | |
| :---: | :---: |
| ![Welcome](https://github.com/user-attachments/assets/0cfa18db-fd66-4de2-bcfc-6cd3ffa3ac73) | ![Login](https://github.com/user-attachments/assets/d2c7f13f-ee4a-4bd1-a14a-6d52acd6dd09) |
| ![Register](https://github.com/user-attachments/assets/b0a67e70-a37e-449f-a91a-09c097f55879) | ![Feed](https://github.com/user-attachments/assets/2b58afaf-27e2-4ff0-851f-9984b687485a) |
| ![Profile](https://github.com/user-attachments/assets/65020a3a-b06c-4d8c-aa71-a8f38f844024) | ![Posts](https://github.com/user-attachments/assets/424f70b9-91a2-405b-b63a-eb08edfc31a1) |
| ![Search](https://github.com/user-attachments/assets/5e3300c4-1c4b-4f7f-acc5-1289a3662527) | ![Group Chat](https://github.com/user-attachments/assets/25357ee9-2112-404e-89e0-e4a384c59bbd) |
| ![Interaction](https://github.com/user-attachments/assets/e26efc66-1206-4efe-9f46-9c3b2e80e83b) | ![Detail](https://github.com/user-attachments/assets/67f6d6d0-8c7d-49f7-9ec1-b234b6186570) |

</div>

---

## 🗄️ Data Model

SIC HUB persists everything in two local JSON files — no server required.

<details>
<summary><b>📄 users.json</b> — user accounts, profiles & posts</summary>

```json
{
  "user@example.com": {
    "first_name": "Ada",
    "last_name": "Lovelace",
    "password": "••••••",
    "profile_pic": "defaultProf.jpg",
    "cover_pic": "defaultCov.png",
    "posts": {
      "1": {
        "content": "Welcome to my profile! This is my first post.",
        "likes": 0,
        "comment": [],
        "date": "29/9/2024",
        "liked_by": []
      }
    }
  }
}
```
</details>

<details>
<summary><b>📄 group_chat.json</b> — shared chat log</summary>

```json
{
  "group_chat": [
    {
      "sender": "user@example.com",
      "message": "Hello, SIC HUB!",
      "timestamp": "2024-10-15 20:19"
    }
  ]
}
```
</details>

> ⚠️ **Note:** Passwords are currently stored in plain text and this project is intended for **educational / demonstration** purposes. See [Future Enhancements](#-future-enhancements) for planned security improvements.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn and build. Any contributions you make are **greatly appreciated**! 🙌

1. 🍴 **Fork** the project
2. 🌿 Create your feature branch — `git checkout -b feature/AmazingFeature`
3. 💾 Commit your changes — `git commit -m "Add some AmazingFeature"`
4. 📤 Push to the branch — `git push origin feature/AmazingFeature`
5. 🔃 Open a **Pull Request**

Please keep changes consistent with the existing OOP structure and coding style.

---

## 🌱 Future Enhancements

Ideas on the roadmap to take SIC HUB to the next level:

- [ ] 🔒 **Password hashing** (e.g. `bcrypt`) instead of plain-text storage
- [ ] 🕐 **Dynamic timestamps** for posts (currently hardcoded dates)
- [ ] 👤 **Private / direct messaging** between members
- [ ] 🔔 **Notifications** for likes, comments, and new messages
- [ ] 🌓 **Dark mode** and theming options
- [ ] 🗃️ **Database migration** (SQLite/PostgreSQL) for scalability
- [ ] 🌍 **Network/multi-user** support beyond a single machine
- [ ] 🧪 **Unit tests** and CI integration
- [ ] 📱 **Responsive layout** improvements for the Tkinter UI

---

## 👥 Team

SIC HUB was designed and developed by a team of three as part of the **Samsung Innovation Campus (SIC)** program. 🎓

<div align="center">

| Member | Connect |
| :----- | :------ |
| **Asmaa Waleed** | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/asma-waleed/) |
| **Ahmed Baher** | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ahmed-baher-8b6564266/) |
| **Ahmed Saad Sweffi** | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ahmed-saad-sweffi-09b2751a9/) |

</div>

> 🙏 Special thanks to **Samsung Innovation Campus** for the training, mentorship, and opportunity that made this project possible.

---

## 📜 License

Distributed under the **MIT License**. See the `LICENSE` file for more information.

---

<div align="center">

### ⭐ If you find SIC HUB useful, consider giving it a star!

Made with 🐍 and ❤️ for the **Samsung Programmer community**

</div>
