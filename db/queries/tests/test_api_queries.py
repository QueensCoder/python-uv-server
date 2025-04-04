from ..api_queries import get_all_users
from ...models.seed import user_one, user_two


def test_get_all_users_returns_users():
    users = get_all_users()
    expected = [user_one, user_two]
    assert users == expected
