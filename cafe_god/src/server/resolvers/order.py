from server.sql_base.models import Order
from server.sql_base.Rescript import base_manager

def new_order(order: Order):
    query = """INSERT INTO orders (user_id, total_amount) VALUES (?, ?) RETURNING order_id;"""
    result = base_manager.execute(query, (order.user_id, order.total_amount))
    return result

def get_order(order_id: int):
    query = "SELECT order_id, user_id, total_amount FROM orders WHERE order_id=?"
    result = base_manager.execute(query, args=(order_id,))
    return result

def get_all_orders():
    query = "SELECT order_id, user_id, total_amount FROM orders"
    result = base_manager.execute(query, many=True)
    return result

def delete_order(order_id: int):
    query = "DELETE FROM orders WHERE order_id=?"
    result = base_manager.execute(query, args=(order_id,))
    return result

def update_order(updated_order: Order, order_id: int):
    query = """UPDATE orders SET (user_id, total_amount) = (?, ?) WHERE order_id=(?);"""
    result = base_manager.execute(query, (updated_order.user_id, updated_order.total_amount, order_id))
    return result
