# FastAPI + SQLAlchemy ORM CRUD

A small backend project built with **FastAPI** and **SQLAlchemy ORM** to understand how Python applications interact with a relational database.

## 🚀 Technologies

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

## 📌 Project Overview

This project demonstrates basic **CRUD operations** using SQLAlchemy ORM with FastAPI.

CRUD stands for:

* **Create** – Add a new user
* **Read** – Retrieve users
* **Update** – Update existing user information
* **Delete** – Delete a user

## 🏗️ Architecture

```text
Client
   ↓
FastAPI
   ↓
Service Layer
   ↓
SQLAlchemy ORM
   ↓
SQLite Database
```

## 📂 Project Structure

```text
SQLAlchemy ORM/
│
├── app/
│   ├── main.py
│   ├── database/
│   │   └── db.py
│   ├── models/
│   │   └── user.py
│   └── services/
│       └── user_service.py
│
├── data/
│   └── sqlite.db
│
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Setup

Clone the repository:

```bash
git clone <repository-url>
cd "SQLAlchemy ORM"
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## 🔄 CRUD Endpoints

| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| POST   | `/users`      | Create a user       |
| GET    | `/users`      | Get all users       |
| GET    | `/users/{id}` | Get a specific user |
| PUT    | `/users/{id}` | Update a user       |
| DELETE | `/users/{id}` | Delete a user       |

## 🗄️ Database

This project uses **SQLite** as the database and **SQLAlchemy ORM** to communicate with it.

SQLAlchemy maps Python classes to database tables, allowing database operations to be performed using Python objects instead of writing raw SQL for every operation.

## 🎯 Learning Goals

This project was created to practice:

* ORM fundamentals
* SQLAlchemy models
* Database connections
* SQLAlchemy sessions
* CRUD operations
* FastAPI API routes
* Dependency injection
* SQLite database integration

## 📚 Purpose

The main purpose of this project is to build a simple and practical understanding of **SQLAlchemy ORM and its integration with FastAPI**.
