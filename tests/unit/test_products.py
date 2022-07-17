import pytest
from base.models import Product


def create_product():
    return Product.objects.create(
        name="vitamin c",
        price=20,
        brand="Sample brand",
        countInStock=0,
        category="Sample category",
        description=" ")


@pytest.fixture()
def test_product_creation():
    p = create_product()
    assert isinstance(p, Product) is True
    assert p.name == "vitamin c"
    assert p.price == 20
