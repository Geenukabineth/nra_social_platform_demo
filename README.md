# 🧠 NRA Social Platform

A full-featured blog and social platform built with Django. Users can register, create and manage blog posts, comment, categorize content, and interact with other users in a clean, mobile-friendly interface.

---

## 🚀 Features

- 🖊️ Full CRUD operations for blog posts
- 🔐 User authentication: Register, Login, Logout
- 💬 Comments on posts
- 🗂️ Post categorization and tagging
- 📅 Track user join date and last activity
- 📱 Responsive design with modern UI
- 🛠️ Admin dashboard for content and user management

---

## 🛠️ Tech Stack

| Layer       | Technology            |
|-------------|------------------------|
| Frontend    | HTML, CSS, JavaScript |
| Backend     | Django (Python)        |
| Auth        | Django Auth |
| Database    | SQLite (Dev) |


---

## 📂 Project Structure

https://github.com/Geenukabineth/nra_social_platform_demo/issues/2#issue-3174290151




---

## 🔧 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/nra_social_platform_demo.git
   cd nra_social_platform_demo
2. **Create a Virtual Environment**
   python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   venv\Scripts\activate           # On Windows
3. **Install Dependencies**
   pip install -r requirements.txt
4. **Run Migrations**
   python manage.py makemigrations
   python manage.py migrate
5. **Create Superuser**
   python manage.py createsuperuser
6. **Start the Development Server**
   python manage.py runserver

