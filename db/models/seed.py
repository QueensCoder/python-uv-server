from .api_models import User
from ..connection import session

user_one = {"username": "user1", "email": "user1@example.com", "id": 1}
user_two = {"username": "user2", "email": "user2@example.com", "id": 2}


def seed_demo_users():
    user1 = User(**user_one)
    user2 = User(**user_two)

    session.add(user1)
    session.add(user2)
    session.commit()
