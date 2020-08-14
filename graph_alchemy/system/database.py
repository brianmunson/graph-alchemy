from time import sleep
from contextlib import contextmanager
from sqlalchemy import create_engine

CONNECT_STRING = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
