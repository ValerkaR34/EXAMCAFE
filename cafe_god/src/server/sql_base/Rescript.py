import sqlite3
import os
from settings import DB_PATH, create_script, create_info


class BaseWorker:
    def __init__(self, base_path: str):
        self.base_path = base_path

    def db_connect(self) -> tuple:
        connection = sqlite3.connect(self.base_path, timeout=5)
        cursor = connection.cursor()
        return connection, cursor

    def check_base(self) -> bool:
        return os.path.exists(self.base_path)

    def create_base(self, sql_file: str) -> None:
        connect, cursor = self.db_connect()
        if self.check_base():
            cursor.executescript(open(sql_file).read())
            connect.commit()
            connect.close()



    def execute(self, query: str, args: tuple = (), many: bool = False):
        connect, cursor = self.db_connect()
        try:
            res_ctx = cursor.execute(query, args)
            if many:
                res = res_ctx.fetchall()
            else:
                res = res_ctx.fetchone()
        except sqlite3.Error as ex:
            print(ex)
            connect.close()
            return {'error': ex}
        connect.commit()
        connect.close()
        return res


base_manager = BaseWorker(base_path=DB_PATH)


if not base_manager.check_base():
    base_manager.create_base(create_script)  # Создание таблиц
    base_manager.create_base(create_info)  # Вставка начальных данных

