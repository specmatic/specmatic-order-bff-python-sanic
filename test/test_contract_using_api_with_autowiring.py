import os

import pytest
from specmatic.core.specmatic import Specmatic

from definitions import PROJECT_ROOT_PATH
from test import APP_STR, PROJECT_ROOT, MOCK_HOST, MOCK_PORT


class TestContract:
    pass


def set_app_config(host: str, port: int):
    os.environ["ORDER_API_HOST"] = host
    os.environ["ORDER_API_PORT"] = str(port)
    os.environ["API_URL"] = f"http://{host}:{port}"


def reset_app_config():
    os.environ["ORDER_API_HOST"] = MOCK_HOST
    os.environ["ORDER_API_PORT"] = str(MOCK_PORT)
    os.environ["API_URL"] = f"http://{MOCK_HOST}:{MOCK_PORT}"


(
    Specmatic(PROJECT_ROOT)
    .with_specmatic_config_file_path(str(PROJECT_ROOT_PATH / "test" / "resources" / "specmatic_config_for_autowiring.yaml"))
    .with_mock()
    .with_asgi_app(
        APP_STR,
        set_app_config_func=set_app_config,
        reset_app_config_func=reset_app_config,
    )
    .test(TestContract)
    .run()
)

if __name__ == "__main__":
    pytest.main()
