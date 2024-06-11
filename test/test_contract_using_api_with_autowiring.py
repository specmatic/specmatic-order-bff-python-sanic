import os

import pytest
from specmatic.core.specmatic import Specmatic

from test import APP_STR, ROOT_DIR, STUB_HOST, STUB_PORT, expectation_json_files


class TestContract:
    pass


def set_app_config(host: str, port: int):
    os.environ["ORDER_API_HOST"] = host
    os.environ["ORDER_API_PORT"] = str(port)
    os.environ["API_URL"] = f"http://{host}:{port}"


def reset_app_config():
    os.environ["ORDER_API_HOST"] = STUB_HOST
    os.environ["ORDER_API_PORT"] = str(STUB_PORT)
    os.environ["API_URL"] = f"http://{STUB_HOST}:{STUB_PORT}"


Specmatic().with_project_root(ROOT_DIR).with_stub(
    expectations=expectation_json_files,
).with_asgi_app(
    APP_STR,
    set_app_config_func=set_app_config,
    reset_app_config_func=reset_app_config,
).test(TestContract).run()

if __name__ == "__main__":
    pytest.main()
