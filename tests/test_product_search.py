import pytest

from config import base_url

@pytest.mark.parametrize("query", ["phone", "laptop", "tv"])
def test_search_products(api_session, query):
    response = api_session.get(base_url + "/products/search", params={"q": query}, timeout=10)

    assert response.status_code == 200

    search_products = response.json()

    assert "products" in search_products
    assert isinstance(search_products["products"], list)
    assert len(search_products["products"]) > 0

    for product in search_products["products"]:
        assert isinstance(product["title"], str)
        assert product["title"].strip() != ""
        assert isinstance(product["id"], int)
        assert product["id"] > 0


def test_search_products_no_results(api_session):
    response = api_session.get(base_url + "/products/search", params={"q": "nonexistentSomething123"}, timeout=10)

    assert response.status_code == 200

    search_products = response.json()
    assert "products" in search_products
    assert isinstance(search_products["products"], list)
    assert len(search_products["products"]) == 0
    assert search_products["total"] == 0


def test_search_products_empty_query(api_session):
    response = api_session.get(base_url + "/products/search", params={"q": ""}, timeout=10)

    assert response.status_code == 200

    response2 = api_session.get(base_url + "/products/search", timeout=10)

    assert response2.status_code == 200

    data_empty_query = response.json()
    data_without_query = response2.json()

    assert data_empty_query["total"] == data_without_query["total"]
    assert data_empty_query["products"] == data_without_query["products"]