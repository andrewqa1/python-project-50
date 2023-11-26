#!/usr/bin/env python3

install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff
	poetry run pytest ./tests

test-coverage:
	poetry run pytest --cov=gendiff ./tests/
