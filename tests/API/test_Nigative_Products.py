import pytest
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from ..unit.test_Admin_User import user_1



# Api test  - Integration testing

def test_api_nigative_product_creation(db,user_2):
    client = APIClient()
    # user = User.objects.create_user(username="testuser", password="123456789")
    user = user_2
    client.force_authenticate(user)
    response = client.post("/api/products/create/")

    # data = response.data

    assert response.status_code == 200

