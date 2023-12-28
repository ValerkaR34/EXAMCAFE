from server.sql_base.models import MenuItem
from server.sql_base.Rescript import base_manager

def new_menu_item(menu_item: MenuItem):
    query = """INSERT INTO menu (item_name, item_description, price) VALUES (?, ?, ?) RETURNING item_id;"""
    result = base_manager.execute(query, (menu_item.item_name, menu_item.item_description, menu_item.price))
    return result

def get_menu_item(item_id: int):
    query = "SELECT item_id, item_name, item_description, price FROM menu WHERE item_id=?"
    result = base_manager.execute(query, args=(item_id,))
    return result

def get_all_menu_items():
    query = "SELECT item_id, item_name, item_description, price FROM menu"
    result = base_manager.execute(query, many=True)
    return result

def delete_menu_item(item_id: int):
    query = "DELETE FROM menu WHERE item_id=?"
    result = base_manager.execute(query, args=(item_id,))
    return result

def update_menu_item(updated_menu_item: MenuItem, item_id: int):
    query = """UPDATE menu SET (item_name, item_description, price) = (?, ?, ?) WHERE item_id=(?);"""
    result = base_manager.execute(query, (updated_menu_item.item_name, updated_menu_item.item_description, updated_menu_item.price, item_id))
    return result
