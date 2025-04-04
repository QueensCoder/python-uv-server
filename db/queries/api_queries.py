from dataclasses import dataclass, asdict

from ..models import User, Campaign
from ..connection import session


def get_user_by_id(user_id: str):
    user = session.query(User).filter(User.id == user_id).first()
    return user


def create_user(username: str, email: str):
    new_user = User(username=username, email=email)
    session.add(new_user)
    session.commit()
    return new_user


def get_all_users():
    users = session.query(User).all()
    users_serialized = [asdict(user) for user in users]
    return users_serialized
