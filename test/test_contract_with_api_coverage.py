import pytest
from specmatic.core.specmatic import Specmatic

from test import APP, APP_HOST, APP_PORT, APP_STR, ROOT_DIR, MOCK_HOST, MOCK_PORT, expectation_json_files


class TestContract:
    pass


Specmatic().with_project_root(ROOT_DIR).with_mock(MOCK_HOST, MOCK_PORT, expectation_json_files).with_asgi_app(
    APP_STR,
    APP_HOST,
    APP_PORT,
).test_with_api_coverage_for_sanic_app(TestContract, APP).run()

if __name__ == "__main__":
    pytest.main()
