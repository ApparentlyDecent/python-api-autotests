from config import base_url

def test_products_pagination(api_session):
    response = api_session.get(base_url + "/products", params={"limit": 5, "skip": 0}, timeout=10)
    assert response.status_code == 200

    first_page = response.json()
    assert first_page["limit"] == 5
    assert first_page["skip"] == 0
    assert isinstance(first_page["products"], list)
    assert len(first_page["products"]) == 5

    response2 = api_session.get(base_url + "/products", params={"limit": 5, "skip": 5}, timeout=10)
    assert response2.status_code == 200

    second_page = response2.json()
    assert second_page["limit"] == 5
    assert second_page["skip"] == 5
    assert isinstance(second_page["products"], list)
    assert len(second_page["products"]) == 5

    assert first_page["total"] == second_page["total"]

    first_page_ids = {product["id"] for product in first_page["products"]}
    second_page_ids = {product["id"] for product in second_page["products"]}

    assert first_page_ids.isdisjoint(second_page_ids)


def test_products_pagination_out_of_range(api_session):
    response = api_session.get(base_url + "/products", params={"skip": 999999}, timeout=10)

    assert response.status_code == 200

    result = response.json()

    assert "products" in result
    assert isinstance(result["products"], list)
    assert len(result["products"]) == 0
    assert result["skip"] == 999999

def test_products_pagination_negative_limit(api_session):
    response = api_session.get(base_url + "/products", params={"limit": -1, "skip": 0}, timeout=10)

    assert response.status_code == 400

    assert "message" in response.json()

    error = response.json()
    assert error["message"] == "Invalid 'limit' - should be a positive number"

def test_products_pagination_zero_limit(api_session):
    response = api_session.get(base_url + "/products", params={"limit": 0, "skip": 0}, timeout=10)

    assert response.status_code == 200

    result = response.json()
    assert "products" in result
    assert isinstance(result["products"], list)

    assert result["limit"] == result["total"]
    assert result["total"] == len(result["products"])