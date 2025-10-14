import pytest
from specmatic.core.specmatic import Specmatic
from specmatic.servers.asgi_app_server import ASGIAppServer

from test import APP, APP_HOST, APP_PORT, APP_STR, ROOT_DIR, MOCK_HOST, MOCK_PORT, expectation_json_files

app_server = ASGIAppServer(APP_STR, APP_HOST, APP_PORT)
app_server.start()


class TestContract:
    pass


Specmatic().with_project_root(ROOT_DIR).with_mock(
    MOCK_HOST,
    MOCK_PORT,
    expectation_json_files,
).test_with_api_coverage_for_sanic_app(TestContract, APP, APP_HOST, APP_PORT).run()

app_server.stop()

if __name__ == "__main__":
    pytest.main()
