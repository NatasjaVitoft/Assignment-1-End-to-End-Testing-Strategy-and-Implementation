from src.models.task import Task
from typing import List

class TaskController:
    
    def __init__(self, conn):
        self.conn = conn

    def add_task(self, title: str, description=None, deadline=None, list_id=None) -> int:
        with self.conn:
            cursor = self.conn.execute(
                'INSERT INTO tasks (title, description, deadline, list_id) VALUES (?, ?, ?, ?)',
                (title, description, deadline, list_id)
            )
        return cursor.lastrowid

    def get_task(self, task_id: int) -> Task:
        cursor = self.conn.execute('SELECT * FROM tasks WHERE id=?', (task_id,))
        row = cursor.fetchone()
        return Task(id=row['id'], title=row['title'], description=row['description'],
                    deadline=row['deadline'], completed=bool(row['completed']), list_id=row['list_id']) if row else None

    def update_task(self, task_id: int, title=None, description=None, deadline=None):
        with self.conn:
            self.conn.execute(
                'UPDATE tasks SET title=?, description=?, deadline=? WHERE id=?',
                (title, description, deadline, task_id)
            )

    def delete_task(self, task_id: int):
        with self.conn:
            self.conn.execute('DELETE FROM tasks WHERE id=?', (task_id,))

    def mark_completed(self, task_id: int):
        with self.conn:
            self.conn.execute('UPDATE tasks SET completed=1 WHERE id=?', (task_id,))
    
    def change_status_task(self, task_id: int, completed: bool):
        with self.conn:
            self.conn.execute('UPDATE tasks SET completed=? WHERE id=?', (int(completed), task_id))

    def get_all_tasks(self) -> List[Task]:
        cursor = self.conn.execute('SELECT * FROM tasks')
        return [
            Task(id=row['id'], title=row['title'], description=row['description'],
                 deadline=row['deadline'], completed=bool(row['completed']), list_id=row['list_id'])
            for row in cursor.fetchall()
        ]

    def add_task_to_list(self, task_id: int, list_id: int):
        with self.conn:
            self.conn.execute('UPDATE tasks SET list_id=? WHERE id=?', (list_id, task_id))
