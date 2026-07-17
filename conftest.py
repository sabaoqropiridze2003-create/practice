import pytest
from user import User


@pytest.fixture
def sample_user():
    return User("saba", "saba@gmail.com")


@pytest.fixture
def admin_user():
    user = User("admin", "admin@gmail.com")
    user.role = "admin"
    return user


@pytest.fixture
def sample_users():
    return [
        User("saba", "saba@gmail.com"),
        User("giorgi", "giorgi@gmail.com"),
        User("nino", "nino@gmail.com")
    ]
