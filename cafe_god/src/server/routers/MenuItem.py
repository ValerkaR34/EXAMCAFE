from fastapi import APIRouter, Depends, HTTPException
from typing import List
from server.sql_base.models import MenuItem
from server.resolvers.MenuItem import new_menu_item, get_menu_item, get_all_menu_items, delete_menu_item, update_menu_item

menu_router = APIRouter(prefix="/menu", tags=["Menu"])

@menu_router.get("/")
def get_menu_items() -> List[MenuItem]:
    return get_all_menu_items()

@menu_router.get("/{item_id}")
def get_current_menu_item(item_id: int) -> MenuItem:
    return get_menu_item(item_id)

@menu_router.post("/new/")
def add_menu_item(menu_item: MenuItem) -> MenuItem:
    return new_menu_item(menu_item)

@menu_router.put("/update/{item_id}")
def update_menu_item_info(item_id: int, updated_menu_item: MenuItem) ->MenuItem:
    return update_menu_item(updated_menu_item, item_id)

@menu_router.delete("/delete/{item_id}")
def delete_menu_item_info(item_id: int):
    result = delete_menu_item(item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return {"message": "Menu item deleted successfully"}
