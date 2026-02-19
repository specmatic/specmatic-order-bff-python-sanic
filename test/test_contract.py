import pytest
from specmatic.core.specmatic import Specmatic

from test import APP_HOST, APP_PORT, APP_STR, PROJECT_ROOT


class TestContract:
    pass


(
    Specmatic(PROJECT_ROOT)
    .with_mock()
    .with_asgi_app(APP_STR, APP_HOST, APP_PORT)
    .test(TestContract)
    .run()
)

if __name__ == "__main__":
    pytest.main()
