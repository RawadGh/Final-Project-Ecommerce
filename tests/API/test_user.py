import pytest
from rest_framework.test import APIClient


'''
Integration testing testing api to register user
'''
@pytest.mark.django_db
def test_register_user():
    client = APIClient()

    payload = dict(
        name="testing123",
        email="test11@test.com",
        password="super-secret"
    )

    response = client.post("/api/users/register/", payload)

    data = response.data

    assert data["name"] == payload["name"]