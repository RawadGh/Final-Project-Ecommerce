import pytest
from django.contrib.auth.models import User


'''
Unit tests -> checking user creation func
'''
@pytest.mark.django_db
def test_Admin_user_create():
    User.objects.create_user('test','test@test.com','test')
    count = User.objects.all().count()
    assert count == 1

@pytest.fixture()
def user_1(db):
    return User.objects.create_superuser(username="testing123@test.com",
        password="super-secret")

@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True



