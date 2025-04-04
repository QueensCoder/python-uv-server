from ..models import User, Campaign
from ..connection import session


def get_user_by_id(user_id: str):
    """
    Fetch a user by their ID.
    """
    user = session.query(User).filter(User.id == user_id).first()
    return user


def create_user(username: str, email: str):
    """
    Create a new user.
    """
    new_user = User(username=username, email=email)
    session.add(new_user)
    session.commit()
    return new_user


def get_all_users():
    """
    Fetch all users.
    """
    users = session.query(User).all()
    print(users, "....")
    return users
