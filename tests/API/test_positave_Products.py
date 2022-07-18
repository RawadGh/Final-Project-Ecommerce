from rest_framework.test import APIClient

# Api test  - Integration testing

def test_api_positave_product_creation(db, user_1):
    client = APIClient()
    # user = User.objects.create_user(username="testuser", password="123456789")
    user = user_1
    client.force_authenticate(user)
    response = client.post("/api/products/create/")

    # data = response.data

    assert response.status_code == 200
