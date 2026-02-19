import pytest
from specmatic.core.specmatic import Specmatic
from specmatic.coverage.servers.sanic_app_coverage_server import SanicAppCoverageServer
from specmatic.servers.asgi_app_server import ASGIAppServer

from test import APP, APP_HOST, APP_PORT, APP_STR, PROJECT_ROOT

app_server = ASGIAppServer(APP_STR, APP_HOST, APP_PORT)
coverage_server = SanicAppCoverageServer(APP)

app_server.start()
coverage_server.start()


class TestContract:
    pass


(
    Specmatic(PROJECT_ROOT)
    .with_mock()
    .with_endpoints_api(coverage_server.endpoints_api)
    .test(TestContract, APP_HOST, APP_PORT)
    .run()
)

app_server.stop()
coverage_server.stop()

if __name__ == "__main__":
    pytest.main()
