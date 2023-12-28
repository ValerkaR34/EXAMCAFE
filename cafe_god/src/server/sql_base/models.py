


from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    username: str
    email: str
    password: str
    registration_date: Optional[str]

class Order(BaseModel):
    order_id: int
    user_id: int
    total_amount: float

class MenuItem(BaseModel):
    item_id: int
    item_name: str
    item_description: Optional[str]
    price: float

class SpecialMenuItem(BaseModel):
    special_id: int
    item_id: int
    special_name: str
    special_description: Optional[str]
    special_price: float

class Review(BaseModel):
    review_id: int
    user_id: int
    order_id: int
    rating: int
    comment: Optional[str]
    review_date: Optional[str]


