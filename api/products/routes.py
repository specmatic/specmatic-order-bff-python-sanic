from typing import TYPE_CHECKING

from sanic import Blueprint, json
from sanic.exceptions import ServiceUnavailable

from api.products.models import Product
from api.services import ProductService, ProductType

if TYPE_CHECKING:
    from sanic import Request

products = Blueprint("products")


@products.route("/findAvailableProducts", methods=["GET"])
async def find_available_products(request: "Request"):
    page_size, p_type = Product.validate_args(request.headers.get("pageSize"), request.args.get("type"))

    # NOTE: API_SPEC v4 requires expects TIMEOUT when type="other" or pageSize=20
    if p_type == ProductType.OTHER or page_size == 20:
        raise ServiceUnavailable("Timeout")

    products = ProductService.find_products(p_type)
    return json(Product.dump(products), status=200)


@products.route("/products", methods=["POST"])
async def add_product(request: "Request"):
    data: Product = Product.load(request.json)
    product = ProductService.create_product(data)
    return json({"id": product["id"]}, status=201)
