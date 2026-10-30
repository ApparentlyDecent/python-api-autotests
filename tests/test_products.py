import pytest

from config import base_url


def test_product(api_session):
    response = api_session.get(base_url + "/products", timeout=10)

    assert response.status_code == 200


def test_get_products_valid_structure(api_session):
    response = api_session.get(base_url + "/products", timeout=10)

    assert response.status_code == 200

    data = response.json()
    assert "products" in data


@pytest.mark.parametrize("product_id", [1, 2, 3, 10])
def test_get_product_by_id(api_session, product_id):
    response = api_session.get(f"{base_url}/products/{product_id}", timeout=10)

    assert response.status_code == 200

    product = response.json()

    assert product["id"] == product_id
    assert isinstance(product["title"], str)
    assert product["title"].strip() != ""
    assert isinstance(product["price"], (int, float))
    assert product["price"] >= 0
    assert "rating" in product
    assert isinstance(product["rating"], (int, float))
    assert 5 >= product["rating"] >= 0


def test_products_not_found(api_session):
    response = api_session.get(base_url + "/products/99999", timeout=10)

    assert response.status_code == 404

    assert response.json().get("message") == "Product with id '99999' not found"


@pytest.mark.parametrize("product_id", [0, -1])
def test_get_product_by_invalid_id(api_session, product_id):
    response = api_session.get(f"{base_url}/products/{product_id}", timeout=10)

    assert response.status_code == 404

    error = response.json()

    assert error["message"] == "Product with id '{}' not found".format(product_id)