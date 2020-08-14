#! /usr/bin/env bash

docker run -d \
    -p 5432:5432 \
    --name graph-alchemy \
    -e POSTGRES_PASSWORD=password \
    postgres:12-alpine > /dev/null
. ./venv/bin/activate
pytest -s \
    --cov-branch \
    --cov=$PACKAGE \
    --cov-fail-under=80 \
    --cov-report=term-missing \
    tests/
docker rm -f graph-alchemy > /dev/null
deactivate