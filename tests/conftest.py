import os
import pytest

CONSTANT = "placeholder"


def load_fixture(name, path):
    with open(f"{path}/{name}", "r") as f:
        return f.read()


@pytest.fixture(scope="session")
def load():
    def fn(name, path):
        return load_fixture(name, path)

    return fn


def set_env_vars():
    os.environ["DB_HOST"] = "0.0.0.0"
    os.environ["DB_PORT"] = "5432"
    os.environ["DB_USER"] = "postgres"
    os.environ["DB_PASS"] = "password"
    os.environ["DB_NAME"] = "postgres"


@pytest.fixture(scope="session")
def set_env():
    def fn():
        return set_env_vars()

    return fn


@pytest.fixture(scope="session")
def constant():
    return CONSTANT
