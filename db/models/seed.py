from .api_models import User
from ..connection import session


def seed_demo_users():
    user1 = User(username="user1", email="user1@example.com")
    user2 = User(username="user2", email="user2@example.com")

    session.add(user1)
    session.add(user2)
    session.commit()
