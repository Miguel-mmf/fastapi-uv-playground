# **FastAPI UV Playground**
___

This repository contains a FastAPI application designed to return the current date and time via an endpoint. The project is built using the UV package manager and follows best practices for structuring and organizing a FastAPI project. The main goal is to provide a simple yet effective example of how to use FastAPI and UV together.

## **Features:**
- FastAPI setup with UV package manager
- Endpoint to return the current date and time
- Well-structured project layout
- Dockerfile for containerization
- Unit tests with pytest

## **Getting Started:**
1. Clone the repository
2. Install dependencies using Poetry
3. Run the application with UVicorn
4. Access the endpoint to get the current date and time

## **Requirements:**
- Python 3.12+
- [UV](./docs/notes.md) Python package and project manager
- [FastAPI](https://fastapi.tiangolo.com/)



## Repo structure

```
fastapi-uv-datetime/
├── Dockerfile
├── README.md
├── app
│   ├── api
│   │   └── endpoints.py
│   ├── main.py
│   ├── schemas
│   │   ├── datetime_schema.py
│   │   └── schemas.py
│   ├── services
│   │   └── datetime_service.py
│   └── settings
│       └── settings.py
├── docs
│   ├── notes.md
│   └── run_application.md
├── hello.py
├── pyproject.toml
├── tests
│   ├── conftest.py
│   └── test_datetime_services.py
└── uv.lock
```


---
**Feel free to contribute and explore the project!**
---
