import os

from api import app
from definitions import ROOT_DIR

expectation_json_files = []
for root, _, files in os.walk(os.path.join(ROOT_DIR, "test/data")):  # noqa: PTH118
    for file in files:
        if file.endswith(".json"):
            expectation_json_files.append(os.path.join(root, file))  # noqa: PERF401, PTH118

APP_HOST = "127.0.0.1"
APP_PORT = 8000
MOCK_HOST = "127.0.0.1"
MOCK_PORT = 8080
APP = app
APP_STR = "api:app"

os.environ["SPECMATIC_GENERATIVE_TESTS"] = "true"
