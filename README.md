# 🧠 Smart Task Manager (Flask)

A modular task management app built with **Flask**, featuring user authentication, session management, and personalized task dashboards. Built as a learning project with clean architecture using Flask Blueprints, Flask-Login, and SQLite.

---

## 🚀 Features (Phase 1–3 Complete)

- ✅ User Registration & Login (with session-based auth)
- ✅ Password hashing with Flask-Bcrypt
- ✅ Add, mark complete, and delete tasks
- ✅ Dashboard showing tasks per user
- ✅ Flash messages for actions
- ✅ Modular Flask Blueprint architecture
- ✅ SQLite + SQLAlchemy ORM
- ✅ CSRF protection with Flask-WTF

---

## ⚒️ Tech Stack

| Layer            | Technology                 |
|------------------|----------------------------|
| Language         | Python                     |
| Framework        | Flask (Blueprints)         |
| Database         | SQLite (via SQLAlchemy)    |
| Auth             | Flask-Login, Flask-WTF     |
| UI Framework     | HTML5, Bootstrap 5         |
| Deployment       | Local (soon: Render/Railway) |

---

## 🚧 Planned Next Steps

- [ ] Add task categories
- [ ] Set task due dates
- [ ] Filter tasks by category/date
- [ ] Add email reminders with Flask-Mail
- [ ] Add Celery + Redis for background tasks
- [ ] Deploy to Render or Railway
- [ ] Switch to MySQL/PostgreSQL

---

## 🧩 Folder Structure

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

---

## 📸 Screenshots

> _Coming soon as UI evolves..._

---

## 🙌 Credits

Made with ❤️ as part of a full-stack learning journey using Flask and Python.