from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

"""
    Task Service
        1. Create
        2. Read 
        3. Update 
        4. Delete
"""


class TaskService:
    @classmethod
    def create_task(cls, conn, task_name: str, task_description: str, task_status: str, task_tag: str, created_by: str):
        try:
            insert_query = text("INSERT INTO tasks (task_name, task_description, task_status, task_tag, created_by) "
                                "VALUES (:task_name, :task_description, :task_status, :task_tag, :created_by)")
            conn.execute(insert_query, {'task_name': task_name, 'task_description': task_description,
                                        'task_status': task_status, 'task_tag': task_tag, 'created_by': created_by})
            conn.commit()
            return {"status_code": 201, "message": "Task Created", 'data': {}}
        except SQLAlchemyError as e:
            conn.rollback()
            error_message = f"Error occurred while creating task: {str(e)}"
            return {"status_code": 500, "message": error_message, 'data': {}}

    @classmethod
    def update_task(cls, conn, task_id: int, task_name: str, task_description: str, task_status: str, task_tag: str):
        update_query = text("UPDATE tasks SET task_name = :task_name, task_description = :task_description, "
                            "task_status = :task_status, task_tag = :task_tag WHERE id = :task_id")
        conn.execute(update_query, {'task_id': task_id, 'task_name': task_name, 'task_description': task_description,
                                    'task_status': task_status, 'task_tag': task_tag})
        conn.commit()
        return {"status_code": 200, "message": "Task Updated", 'data': {}}

    @classmethod
    def delete_task(cls, conn, task_id: int):
        print("Deleting Task", type(task_id))

        # Check if the task exists
        check_task_query = text("SELECT * FROM tasks WHERE id = :task_id")
        task_result = conn.execute(check_task_query, {'task_id': task_id}).fetchone()

        if not task_result:
            return {"status_code": 404, "message": "Task Not Found", 'data': {}}

        # Proceed with deletion
        delete_query = text("DELETE FROM tasks WHERE id = :task_id")
        conn.execute(delete_query, {'task_id': task_id})
        conn.commit()

        return {"status_code": 200, "message": "Task Deleted", 'data': {}}

    @classmethod
    def fetch_all_tasks(cls, conn, page, limit, status):
        offset = (page - 1) * limit
        print(status)

        # Construct the base query
        query = "SELECT * FROM tasks"

        # If status is provided, add WHERE clause to filter by status
        if status:
            query += " WHERE task_status = :status"

        # Add ORDER BY, LIMIT, and OFFSET clauses
        query += " ORDER BY id LIMIT :limit OFFSET :offset"

        # Execute the query with parameters
        result = conn.execute(text(query), {"status": status, "limit": limit, "offset": offset})

        # Fetch all rows
        data_result = result.fetchall()

        # Convert data result to tasks
        tasks = [
            {"id": str(row[0]), "task_name": row[1], "task_description": row[2], "task_status": row[3],
             "task_tag": row[4],
             "created_by": row[5], "created_at": str(row[6])} for row in data_result
        ]

        # If status is provided, count only tasks with that status; otherwise, count all tasks
        if status:
            count_query = text("SELECT COUNT(*) FROM tasks WHERE task_status = :status")
            total_count = conn.execute(count_query, {"status": status}).scalar()
        else:
            count_query = text("SELECT COUNT(*) FROM tasks")
            total_count = conn.execute(count_query).scalar()

        return {"status_code": 200, "message": "Tasks Fetched", "data": tasks, "count": total_count}
