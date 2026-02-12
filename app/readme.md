# FastAPI RBAC System

A backend authentication and authorization system built with **FastAPI**, **SQLAlchemy**, **PostgreSQL**, and **JWT**, implementing **Role-Based Access Control (RBAC)** using clean architecture and FastAPI dependencies.

This project is intended as a reusable backend foundation for applications like blogs, admin page.

---

## Features

- JWT-based authentication
- OAuth2 Bearer token support
- Role-based authorization (RBAC)
- Clean separation of concerns (routers, services, repositories)
- SQLAlchemy ORM relationships
- PostgreSQL database

---

## Tech Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- PyJWT
- OAuth2PasswordBearer

## Authorization (RBAC)

Authorization is handled using FastAPI dependencies, not inside route logic.

Example roles:
- `admin`
- `user`

Role checks are enforced via callable dependency classes.

---

## Database Schema

### Users
- `id`
- `email`
- `password`
- `role_id`

### Roles
- `id`
- `name`

Users reference roles using a foreign key. SQLAlchemy relationships allow accessing role data without manual joins.

---

## Running the Project

1. Create and activate a virtual environment
2. Install dependencies


---

## Example Endpoints

- `POST /auth/signup`
- `POST /auth/token`
- `GET /users/me`
- `GET /users/admin`

Protected routes require a valid JWT and appropriate role.

---

## Notes

- This project focuses on backend architecture and security
