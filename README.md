# DataChat API

A REST API that lets users query data using natural language, powered by a local LLM (LLaMA 3.2 via Ollama).

Built with Django, Django REST Framework, and PostgreSQL.

## What it does

- Accepts natural language questions via a POST endpoint
- Sends the question to LLaMA 3.2 running locally via Ollama
- Returns an AI-generated response
- Stores all queries and responses in a PostgreSQL database
- Supports full query history retrieval and deletion

## Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** PostgreSQL
- **AI/LLM:** Ollama (LLaMA 3.2)

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/query/` | Submit a natural language question |
| GET | `/api/history/` | Retrieve all past queries |
| DELETE | `/api/history/<id>/` | Delete a specific query |

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/APARNARAJN/datachat-api.git
cd datachat-api
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file:
```
DB_NAME=datachat
DB_USER=datachat_user
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

### 5. Set up PostgreSQL
```sql
CREATE DATABASE datachat;
CREATE USER datachat_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE datachat TO datachat_user;
```

### 6. Run migrations
```bash
python manage.py migrate
```

### 7. Start Ollama and run server
```bash
ollama serve  # in a separate terminal
python manage.py runserver
