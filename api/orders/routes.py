from typing import TYPE_CHECKING

from sanic import Blueprint, json

from api.orders.models import Order
from api.services import OrdersService

if TYPE_CHECKING:
    from sanic import Request

orders = Blueprint("orders")


@orders.route("/orders", methods=["POST"], ctx_expected_content_type="application/json")
async def create_order(request: "Request"):
    data: Order = Order.load(request.json)
    order = OrdersService.create_order(data)
    return json({"id": order["id"]}, status=201)
