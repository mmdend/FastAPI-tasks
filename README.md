# Task Manager API

A simple CRUD API for managing tasks, built with **FastAPI** and **PostgreSQL**.

## Tech stack

- Python, FastAPI
- PostgreSQL, SQLAlchemy 2.0 (psycopg2)
- Pydantic (schemas and settings)
- uv (dependency management)

## Project structure

```text
├── app
│   ├── __init__.py
│   ├── config.py        # settings loaded from .env
│   ├── crud.py          # database operations
│   ├── database.py      # engine, session, get_db
│   ├── main.py          # app entry point
│   ├── models.py        # SQLAlchemy models
│   ├── routers
│   │   ├── __init__.py
│   │   └── tasks.py     # /tasks endpoints
│   └── schemas.py       # Pydantic schemas
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
└── uv.lock
```

## API endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/tasks/` | List all tasks |
| GET | `/tasks/{task_id}` | Get one task |
| POST | `/tasks/` | Create a task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

Interactive documentation (Swagger UI): `/docs`

## Database schema

Table "public.tasks"


| Column | Type | Notes |
|--------|------|-------|
| `id` | integer | Primary key |
| `title` | varchar(255) | Required |
| `description` | text | Optional |
| `is_completed` | boolean | Defaults to `false` |
| `created_at` | timestamptz | Set automatically by the database |

Indexes:
    "tasks_pkey" PRIMARY KEY, btree (id)


## Local setup

1. Start PostgreSQL (example with Docker, change the credentials):

```bash
docker run -d --name tasks-postgres \
  -e POSTGRES_USER=<user> \
  -e POSTGRES_PASSWORD=<password> \
  -e POSTGRES_DB=tasks_db \
  -p 5432:5432 \
  -v tasks_pgdata:/var/lib/postgresql/data \
  postgres:16
```


2. Install dependencies:

```bash
uv sync
```

1. Create a `.env` file (change the credentials):

```env
DATABASE_URL=postgresql+psycopg2://<user>:<password>@localhost:5432/tasks_db
```

4. Run the app (tables are created on startup):

```bash
uv run fastapi dev
```

Open http://127.0.0.1:8000/docs

## Quick test

```bash
curl -X POST http://127.0.0.1:8000/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "First task from FIOTRIX", "description": "hello :D"}'

curl http://127.0.0.1:8000/tasks/
```

## References

- [Maktabkhooneh — FastAPI Ali Bigdeli](https://maktabkhooneh.org/course/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C-%D8%B3%D8%B1%D9%88%DB%8C%D8%B3-fastapi-mk10645/)
- [AliBigdeli — FastAPI Tutorial Service (GitHub Repo)](https://github.com/AliBigdeli/FastAPI-Tutorial-Service)
- [FastAPI — Official Documentation](https://fastapi.tiangolo.com/)
- [FastAPI — Dependencies with `yield`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#a-database-dependency-with-yield)
- [FastAPI — SQL Databases](https://fastapi.tiangolo.com/de/tutorial/sql-databases/)
- [FastAPI — Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [FastAPI — Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [FastAPI — Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [uv Setup Cheat Sheet](https://gist.github.com/AliBigdeli/4e5a533df6be07c99d5213e2d5cf2f85)
