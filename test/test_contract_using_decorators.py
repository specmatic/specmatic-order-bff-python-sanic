import pytest
from specmatic.core.decorators import specmatic_contract_test, specmatic_stub, start_asgi_app

from test import APP_HOST, APP_PORT, APP_STR, ROOT_DIR, STUB_HOST, STUB_PORT, expectation_json_files


# NOTE: Type Hint AppRouteAdapter in specmatic_contract_test decorator should be AppRouteAdapter | None
@specmatic_contract_test(APP_HOST, APP_PORT, ROOT_DIR)  # type: ignore[reportArgumentType]
@start_asgi_app(APP_STR, APP_HOST, APP_PORT)
@specmatic_stub(STUB_HOST, STUB_PORT, ROOT_DIR, expectation_json_files)
class TestApiContract:
    pass


if __name__ == "__main__":
    pytest.main()
