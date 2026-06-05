import json as jsonlib
import os
from datetime import UTC, datetime

from dotenv import load_dotenv
from marshmallow import ValidationError
from sanic import Sanic, json
from sanic.exceptions import SanicException

load_dotenv()
app = Sanic("OrderBFF")
app.config["ORDER_API_HOST"] = os.getenv("ORDER_API_HOST")
app.config["ORDER_API_PORT"] = os.getenv("ORDER_API_PORT")
app.config["API_URL"] = f"http://{app.config['ORDER_API_HOST']}:{app.config['ORDER_API_PORT']}"
app.config["AUTH_TOKEN"] = os.getenv("AUTH_TOKEN") or "API-TOKEN-SPEC"
app.config["REQ_TIMEOUT"] = os.getenv("REQ_TIMEOUT") or 3000


@app.exception(ValidationError)
async def handle_marshmallow_validation_error(_, exc: "ValidationError"):
    return json(
        {
            "timestamp": datetime.now(tz=UTC).isoformat(),
            "status": 400,
            "error": "Bad Request",
            "message": jsonlib.dumps(exc.messages),
        },
        status=400,
    )


@app.exception(SanicException)
async def http_error_handler(_, exception: "SanicException"):
    return json(
        {
            "timestamp": datetime.now(tz=UTC).isoformat(),
            "status": exception.status_code,
            "error": exception.__class__.__name__,
            "message": str(exception),
        },
        status=exception.status_code,
    )

@app.on_request
async def enforce_expected_content_type(request):
    route = getattr(request, "route", None)
    if route is None:
        return

    expected = getattr(route.ctx, "expected_content_type", None)
    if not expected:
        return

    actual = (request.headers.get("content-type") or "").split(";")[0].strip().lower()
    expected_types = {expected} if isinstance(expected, str) else set(expected)
    if actual in expected_types:
        return

    return json(
        {
            "status": 415,
            "timestamp": datetime.now(tz=UTC).isoformat(),
            "error": "Unsupported Media Type",
            "message": f"Content-Type must be one of: {', '.join(sorted(expected_types))}",
        },
        status=415,
    )

from api.orders.routes import orders  # noqa: E402
from api.products.routes import products  # noqa: E402

app.blueprint(products)
app.blueprint(orders)
