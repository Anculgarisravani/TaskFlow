# TaskFlow API

## Overview

TaskFlow API is an Enterprise Task & Workflow Management System built using FastAPI and PostgreSQL. It helps users manage projects and tasks through secure REST APIs with JWT-based authentication and authorization.

## Features

* User Registration
* Secure Password Hashing using bcrypt
* User Login with JWT Authentication
* Protected API Routes
* Project Management (CRUD Operations)
* Task Management (CRUD Operations)
* Project-Task Relationship
* PostgreSQL Database Integration
* SQLAlchemy ORM
* Interactive Swagger API Documentation

## Tech Stack

### Backend

* FastAPI
* Python

### Database

* PostgreSQL
* SQLAlchemy ORM

### Authentication

* JWT (JSON Web Tokens)
* OAuth2 Password Bearer

### Tools

* Git
* GitHub
* Swagger UI / OpenAPI

## Project Structure

```text
TaskFlow/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── utils.py
│   └── routers/
│       ├── projects.py
│       ├── tasks.py
│       └── users.py
│
├── .gitignore
└── requirements.txt
```

## API Endpoints

### Authentication

| Method | Endpoint     | Description   |
| ------ | ------------ | ------------- |
| POST   | /users       | Register User |
| POST   | /users/login | User Login    |

### Projects

| Method | Endpoint                     |
| ------ | ---------------------------- |
| GET    | /projects                    |
| POST   | /projects                    |
| GET    | /projects/{project_id}       |
| PUT    | /projects/{project_id}       |
| DELETE | /projects/{project_id}       |
| GET    | /projects/{project_id}/tasks |

### Tasks

| Method | Endpoint         |
| ------ | ---------------- |
| GET    | /tasks           |
| POST   | /tasks           |
| PUT    | /tasks/{task_id} |
| DELETE | /tasks/{task_id} |

## Authentication Flow

1. Register a user.
2. Login using email and password.
3. Receive JWT access token.
4. Authorize using the token in Swagger UI.
5. Access protected endpoints.

## How to Run

### Clone Repository

```bash
git clone https://github.com/Anculgarisravani/TaskFlow.git
cd TaskFlow
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn app.main:app --reload
```

### Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

## Future Enhancements

* User-Owned Projects
* Role-Based Access Control
* Project Analytics Dashboard
* Task Priority Management
* Due Date Notifications
* File Attachments
* Docker Deployment

## Author

**ANCUL GARI SRAVANI**

B.Tech – Computer Science & Engineering (Cyber Security)

FastAPI | Python | PostgreSQL | Backend Development
