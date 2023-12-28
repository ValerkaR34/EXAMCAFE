from fastapi import APIRouter, Depends, HTTPException
from typing import List
from server.sql_base.models import Order
from server.resolvers.order import new_order, get_order, get_all_orders, delete_order, update_order

orders_router = APIRouter(prefix="/orders", tags=["Orders"])

@orders_router.get("/")
def get_orders() -> List[Order]:
    return get_all_orders()

@orders_router.get("/{order_id}")
def get_current_order(order_id: int) -> Order:
    return get_order(order_id)

@orders_router.post("/new/")
def add_order(order: Order) -> Order:
    return new_order(order)

@orders_router.put("/update/{order_id}")
def update_order_info(order_id: int, updated_order: Order) -> Order:
    return update_order(updated_order, order_id)

@orders_router.delete("/delete/{order_id}")
def delete_order_info(order_id: int):
    result = delete_order(order_id)
    if not result:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order deleted successfully"}
