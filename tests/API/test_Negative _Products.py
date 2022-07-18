from rest_framework.test import APIClient

# Api test  - Integration testing

def test_api_Negative_product_creation(db, user_2):
    client = APIClient()
    user = user_2
    client.force_authenticate(user)
    response = client.post("/api/products/create/")
    assert response.status_code == 200
