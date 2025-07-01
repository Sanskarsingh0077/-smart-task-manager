# 🧠 Smart Task Manager (Flask + MySQL/PostgreSQL)

A smart task management system built with **Flask**, featuring user authentication, task organization by categories and due dates, and automated email reminders using **Celery**. Designed to simulate real-world system design with modular backend architecture and secure session-based auth.

---

## 🚀 Features

- ✅ User Registration & Login (session-based authentication)
- ✅ Create, update, delete tasks
- ✅ Categorize tasks & set due dates
- ✅ Filter tasks by category or deadline
- ✅ Dashboard with organized task views
- ✅ Email reminders for upcoming deadlines
- ✅ Modular Flask Blueprints structure
- ✅ Secure password hashing & CSRF protection
- ✅ Clean responsive UI (Bootstrap 5)

---

## 🛠 Tech Stack

| Layer            | Technology                            |
|------------------|----------------------------------------|
| Language         | Python                                 |
| Framework        | Flask (with Blueprints)                |
| Database         | MySQL or PostgreSQL (SQLAlchemy ORM)   |
| Auth             | Flask-Login, Flask-WTF, Bcrypt         |
| Background Tasks | Celery + Redis                         |
| Email Service    | Flask-Mail                             |
| Frontend         | HTML5, CSS3, Bootstrap 5               |
| Deployment       | Render / Railway / Heroku              |

---

## 📸 Screenshots

> _Screenshots coming soon_  


---

## 🧩 Project Structure

```
smart-task-manager/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── auth/
│   │   ├── routes.py
│   │   └── forms.py
│   ├── tasks/
│   │   ├── routes.py
│   │   └── forms.py
│   ├── templates/
│   ├── static/
│   └── email/
├── config.py
├── run.py
├── celery_worker.py
├── requirements.txt
├── .env
└── .gitignore
```