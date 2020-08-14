.PHONY: docs setup lint clean test
.ONESHELL: docs setup lint clean test

SHELL := /bin/bash
package := graph

clean:
	rm -fR ./dist
	rm -fR ./build
	rm -fR ./.pytest_cache
	rm -fR ./$(package).egg-info
	find ./tests -regex "\(.*__pycache__.*\|*.py[co]\)" -delete
	find ./$(package) -regex "\(.*__pycache__.*\|*.py[co]\)" -delete

setup:
	rm -fR ./venv
	virtualenv -p python3 ./venv
	. ./venv/bin/activate
	pip install -r requirements.txt

test: clean
	. ./scripts/set-env.sh
	PACKAGE=$(package) ./scripts/run-tests.sh

lint:
	. ./venv/bin/activate
	pylint --disable=C,R $(package)
	pylint --disable=C,R tests
	mypy ./$(package)

docs:
	./scripts/create-docs.sh