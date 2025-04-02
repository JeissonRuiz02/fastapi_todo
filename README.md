# 🗂️ FastAPI ToDo API with JWT Authentication

A modern, production-ready RESTful API for managing To-Do tasks, built using **FastAPI** with **JWT-based authentication** and backed by **PostgreSQL**. Designed to demonstrate clean architecture, modular code, and best practices in backend development.

---

## 🎯 Project Goals

- Secure user registration and login using JWT.
- CRUD operations for personal tasks.
- Support for search, filtering, and pagination.
- Due date validation to prevent past deadlines.
- Automatically generated OpenAPI documentation.

---

## 🚀 Tech Stack

- ⚙️ **FastAPI** – High-performance Python web framework.
- 🐘 **PostgreSQL** – Relational database for persistence.
- 🔐 **JWT** – Secure authentication with access tokens.
- 🔄 **SQLAlchemy** – ORM for database interaction.
- 🧪 **Pytest** – Unit and integration testing.
- 📦 **Poetry** – Dependency and environment management.
- 📚 **Pydantic v2** – Data validation and serialization.

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/fastapi_todo.git
cd fastapi_todo

# Install dependencies
poetry install

# Activate the virtual environment
poetry shell

# Run the server
uvicorn app.main:app --reload
```


## ⚙️ Environment Variables
You can configure these in app/config.py or using a .env file:

```bash
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/fastapi_todo
```

## 🧪 Running Tests
```bash
poetry run pytest -v
```
Test coverage includes:

- Authentication and registration

- Task creation, listing, updating, and deletion

- JWT validation

- Schema and business logic validation

## 📄 Key Endpoints

| Method | Endpoint         | Description                      |
|--------|------------------|----------------------------------|
| POST   | /auth/register   | Register a new user              |
| POST   | /auth/token      | Log in and receive a JWT         |
| GET    | /tasks           | List user's tasks (paginated, filterable) |
| POST   | /tasks           | Create a new task                |
| PUT    | /tasks/{id}      | Update a specific task           |
| DELETE | /tasks/{id}      | Delete a specific task           |

---

## 📚 API Docs

Once the app is running, access:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)  
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🗂️ Project Structure

```bash
fastapi_todo/
│
├── app/
│   ├── auth/               # Authentication logic
│   ├── db/                 # Database setup and session
│   ├── models/             # SQLAlchemy models
│   ├── routers/            # API route definitions
│   ├── schemas/            # Pydantic schemas
│   ├── utils/constants/    # Reusable constants
│   └── config.py           # Global configuration
│
├── tests/                  # Test suite
├── pyproject.toml          # Poetry project file
└── README.md               # Project documentation
```
--- 
## 🤝 Contributing
Feel free to fork this project, open issues, or submit pull requests. All feedback and contributions are welcome!

---

## 👤 Author
- Jeisson – GitHub
- Backend Engineer | Clean Code Advocate | Pythonista
---
## 📜 License
This project is licensed under the [MIT License](LICENSE).
