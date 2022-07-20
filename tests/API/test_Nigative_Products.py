import pytest
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from ..unit.test_Admin_User import user_1



# Api test  - Integration testing.
@pytest.mark.django_db
def test_api_Nigative_product_creation():
    client = APIClient()
    user2 = User.objects.create_user(username="test11@test.com",password="super-secret")
    # user2 = user_2
    client.force_authenticate(user2)
    response = client.post("/api/products/create/")

    # data = response.data

    assert response.status_code == 200

