from user import User
import pytest


# def test_user_greet():
#     user = User("saba", "saba@example.com")
#     user.greet()
#     assert user.greet() == "Hello, saba!"


# def test_user_deactivate():
#     user = User("saba", "saba@example.com")
#     user.deactivate()
#     assert user.active == False


# def test_user_change_email():
#     user = User("saba", "saba@example.com")
#     user.change_email("newemail@example.com")
#     assert user.email == "newemail@example.com"


@pytest.fixture()
def exm_user():
    return User("saba", "saba@example.com")


def test_user_greet2(exm_user):
    assert exm_user.greet() == "Hello, saba!"


def test_user_deactivate2(exm_user):
    exm_user.deactivate()
    assert exm_user.active == False


def test_user_active_status(exm_user):
    assert exm_user.active == True


def test_user_change_email2(exm_user):
    exm_user.change_email("saba.new@example.com")
    assert exm_user.email == "saba.new@example.com"
