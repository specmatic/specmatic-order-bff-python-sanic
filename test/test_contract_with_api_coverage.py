import pytest
from specmatic.core.specmatic import Specmatic

from test import APP, APP_HOST, APP_PORT, APP_STR, PROJECT_ROOT


class TestContract:
    pass


(
    Specmatic(PROJECT_ROOT)
    .with_mock()
    .with_asgi_app(APP_STR, APP_HOST, APP_PORT)
    .test_with_api_coverage_for_sanic_app(TestContract, APP)
    .run()
)

if __name__ == "__main__":
    pytest.main()
