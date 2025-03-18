# Django-CRUD-Backend
This project is based on performing CRUD operation using DRF(Django REST Framework) Architecture.
# Task Management API - Documentation

## Introduction
This is a Task Management API built using Django Rest Framework
(DRF) that allows users to perform CRUD operations on tasks.
The API includes authentication, filtering, pagination, and custom
permissions.

## Features
- User authentication with JWT (JSON Web Token)
- CRUD operations for tasks
- Filtering by completion status and date range
- Pagination for task lists
- Custom permissions for task access
- Error handling with proper status codes

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Django & DRF
- SQLite
- Virtual Environment (recommended)

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Django-CRUD-Backend.git
   cd Django-CRUD-Backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate #Windows User
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser (For admin access):
   ```bash
   python manage.py createsuperuser
   ```
6. Run the server:
   ```bash
   python manage.py runserver
   ```
   The API will be available at http://127.0.0.1:8000/

## Authentication
This API uses JWT authentication.
- Register a new user: `POST /api/register/`
- Login and get token: `POST /api/login/`
- Use the token in Authorization header for authenticated requests.

Example:
```http
Authorization: Bearer your-access-token
```

## API Endpoints

### User Authentication
| Method | Endpoint       | Description         |
| ------ | -------------- | ------------------- |
| POST   | /api/register/ | Register a new user |
| POST   | /api/login/    | Get access token    |

### Tasks
| Method | Endpoint         | Description                |
| ------ | ---------------- | -------------------------- |
| POST   | /api/tasks/      | Create a task              |
| GET    | /api/tasks/      | List all tasks (paginated) |
| GET    | /api/tasks/{id}/ | Get task details           |
| PUT    | /api/tasks/{id}/ | Update a task              |
| DELETE | /api/tasks/{id}/ | Delete a task              |

## Filtering Tasks
Tasks can be filtered using query parameters:

| Parameter                   | Description                     |
| --------------------------- | ------------------------------- |
| `completed=true`            | Filter by completed status      |
| `created_after=YYYY-MM-DD`  | Get tasks created after a date  |
| `created_before=YYYY-MM-DD` | Get tasks created before a date |
| `updated_after=YYYY-MM-DD`  | Get tasks updated after a date  |

**Example Request:**
```http
GET /api/tasks/?completed=true&created_after=2024-01-01
```

## Pagination
Pagination is enabled with a limit of **10 tasks per page**.

**Example:**
```http
GET /api/tasks/?page=2
```

## Permissions
- Only authenticated users can create, update, or delete tasks.
- A user can only update or delete their own tasks.
- Admin users can view all tasks.

## Error Handling
The API provides proper error messages:

| Status Code      | Meaning                        |
| ---------------- | ------------------------------ |
| 400 Bad Request  | Invalid request data           |
| 401 Unauthorized | Authentication required        |
| 403 Forbidden    | Not allowed to access resource |
| 404 Not Found    | Task or endpoint not found     |


## Conclusion
This Task Management API is designed to be secure, efficient, and
scalable.
It follows Django best practices and provides a robust backend for
task management applications.

