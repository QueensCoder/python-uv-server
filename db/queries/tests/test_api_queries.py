from ..api_queries import get_all_users


def test_get_all_users_returns_users():
    users = get_all_users()
    print(users, "....")
    assert False
