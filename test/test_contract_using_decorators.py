import pytest
from specmatic.core.decorators import specmatic_contract_test, specmatic_mock, start_asgi_app

from test import APP_HOST, APP_PORT, APP_STR, PROJECT_ROOT


# NOTE: Type Hint AppRouteAdapter in specmatic_contract_test decorator should be AppRouteAdapter | None
@specmatic_contract_test(project_root=PROJECT_ROOT)  # type: ignore[reportArgumentType]
@start_asgi_app(APP_STR, APP_HOST, APP_PORT)
@specmatic_mock(project_root= PROJECT_ROOT)
class TestApiContract:
    pass


if __name__ == "__main__":
    pytest.main()
