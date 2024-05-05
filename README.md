# Task Manager Application

## Description
This is a task manager application built on FastAPI, PostgreSQL using SQLAlchemy.

## Project Structure

### 1. Routes
Contains all the endpoint definitions for the API.

### 2. Services
Holds the business logic and interacts with the database through the ORM.

### 3. Configs
- **env**: Environment configuration files.
- **db**: Database configuration files.

### 4. Utils
Utility functions and helpers used across the project.

## Files

### main.py
Entry point of the application.

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to Task Manager API!"}
```

## Setup

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <project_directory>
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Configure environment variables:
   - Copy the `.env.example` file and rename it to `.env`.
   - Update the variables according to your environment.

7. Set up the database:
   - Ensure PostgreSQL is installed and running.
   - Create a new database and update the database configuration accordingly in `.env`.

8. Run the application:

   ```bash
   uvicorn main:app --reload
   ```

## Usage

Once the application is running, you can interact with the API using the defined routes.

