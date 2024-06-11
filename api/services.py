from typing import ClassVar

import requests
from sanic.exceptions import SanicException

from api import app
from api.orders.models import Order
from api.products.models import Product
from api.schemas import ProductType


class ProductService:
    _API_LIST: ClassVar[dict[str, str]] = {
        "SEARCH": "/products",
        "CREATE": "/products",
    }

    @staticmethod
    def find_products(p_type: ProductType | None) -> list[Product]:
        resp = requests.get(
            f"{app.config['API_URL']}{ProductService._API_LIST['SEARCH']}",
            params={"type": p_type.value if p_type else None},
            timeout=app.config["REQ_TIMEOUT"],
        )
        if resp.status_code != 200:
            raise SanicException("An error occurred while retrieving the products.", status_code=resp.status_code)

        return Product.load_many(resp.json())

    @staticmethod
    def create_product(product: Product) -> dict[str, int]:
        resp = requests.post(
            f"{app.config['API_URL']}{ProductService._API_LIST['CREATE']}",
            json=product.asdict(),
            headers={"Authenticate": app.config["AUTH_TOKEN"]},
            timeout=app.config["REQ_TIMEOUT"],
        )

        if resp.status_code != 200:
            raise SanicException("An error occurred while creating the product.", status_code=resp.status_code)

        return resp.json()


class OrdersService:
    _API_LIST: ClassVar[dict[str, str]] = {
        "CREATE": "/orders",
    }

    @staticmethod
    def create_order(order: Order) -> dict[str, int]:
        resp = requests.post(
            f"{app.config['API_URL']}{OrdersService._API_LIST['CREATE']}",
            json=order.asdict(),
            headers={"Authenticate": app.config["AUTH_TOKEN"]},
            timeout=app.config["REQ_TIMEOUT"],
        )

        if resp.status_code != 200:
            raise SanicException("An error occurred while creating the order.", status_code=resp.status_code)

        return resp.json()
