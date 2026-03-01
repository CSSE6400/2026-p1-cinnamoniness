[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=22804633)
# CSSE6400 Week 1 Practical

Construction of a simple HTTP server in Python using Flask.

Please see the [instructions](https://csse6400.uqcloud.net/practicals/week01.pdf) for more details.

## Running the App

Install dependencies:
```bash
poetry install
```

Run the server:
```bash
poetry run flask --app todo run -p 6400
```

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/v1/health | Health check |
| GET | /api/v1/todos | List all todos |
| GET | /api/v1/todos/\<id\> | Get a specific todo |
| POST | /api/v1/todos | Create a todo |
| PUT | /api/v1/todos/\<id\> | Update a todo |
| DELETE | /api/v1/todos/\<id\> | Delete a todo |