
from server.sql_base.Rescript import base_manager

from  ..sql_base.models import User

def new_user(user: User):
    query = """INSERT INTO Users (username, email, password, registration_date) VALUES (?, ?, ?, ?) RETURNING user_id;"""
    result = base_manager.execute(query, (user.username, user.email, user.password, user.registration_date))
    return result

def get_user(user_id: int):
    query = "SELECT user_id, username, email, password, registration_date FROM Users WHERE user_id=?"
    result = base_manager.execute(query, args=(user_id,))
    return result

def get_all_users():
    query = "SELECT user_id, username, email, password, registration_date FROM Users"
    result = base_manager.execute(query, many=True)
    return result

def delete_user(user_id: int):
    query = "DELETE FROM Users WHERE user_id=?"
    result = base_manager.execute(query, args=(user_id,))
    return result

def update_user(user: User, user_id: int):
    query = """UPDATE Users SET (username, email, password, registration_date) = (?, ?, ?, ?) WHERE user_id=(?);"""
    result = base_manager.execute(query, (user.username, user.email, user.password, user.registration_date, user_id))
    return result
