from src.models.list_task import ListTask

class ListTaskController:
    
    def __init__(self, conn):
        self.conn = conn

    def add_list(self, name: str) -> int:
        with self.conn:
            cursor = self.conn.execute('INSERT INTO lists (name) VALUES (?)', (name,))
        return cursor.lastrowid

    def get_list(self, list_id: int) -> ListTask:
        cursor = self.conn.execute('SELECT * FROM lists WHERE id=?', (list_id,))
        row = cursor.fetchone()
        return ListTask(id=row['id'], name=row['name']) if row else None

    def delete_list(self, list_id: int):
        with self.conn:
            self.conn.execute('DELETE FROM lists WHERE id=?', (list_id,))

    def get_all_lists(self):
        cursor = self.conn.execute('SELECT * FROM lists')
        return [ListTask(id=row['id'], name=row['name']) for row in cursor.fetchall()]
