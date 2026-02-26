# Simple Task Manager API

**Description:**

This project provides a simple RESTful API for managing tasks. It allows users to create, read, update, and delete tasks. The frontend provides a basic interface for interacting with the API.

**Why it's useful:**

A task manager is a fundamental tool for productivity. This API provides a foundation for building more complex task management applications or integrating task management functionality into existing systems.

**Installation:**

1.  **Clone the repository:**
    ```bash
    git clone https://github/your-username/simple-task-manager.git
    cd simple-task-manager
    ```

2.  **Set up the backend:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate  # Windows
    pip install -r requirements.txt
    ```

3.  **Set up the frontend:**
    ```bash
    npm install
    npm start
    ```

4.  **Set environment variables:**
    Create a `.env` file in the root directory and populate it with the following:
    ```
    DATABASE_URL=sqlite:///tasks.db
    ```

**API Endpoints:**

*   `GET /tasks`: Retrieves all tasks.
*   `GET /tasks/{id}`: Retrieves a specific task by ID.
*   `POST /tasks`: Creates a new task.  Request body: `{ "title": "Task Title", "description": "Task Description" }`
*   `PUT /tasks/{id}`: Updates an existing task. Request body: `{ "title": "New Title", "description": "New Description" }`
*   `DELETE /tasks/{id}`: Deletes a task by ID.

**Examples:**

*   **Create a task:**
    `curl -X POST -H "Content-Type: application/json" -d '{"title": "Grocery Shopping", "description": "Buy milk, eggs, and bread"}' http://localhost:5000/tasks`

*   **Get all tasks:**
    `curl http://localhost:5000/tasks`

*   **Update a task:**
    `curl -X PUT -H "Content-Type: application/json" -d '{"id": 1, "title": "Updated Task", "description": "Updated Description"}' http://localhost:5000/tasks/1`

**Error Handling:**

*   `404 Not Found`:  Returned when a resource is not found.

**License:**

MIT License