SHELL := /bin/bash

.PHONY: help
## List the tasks of the Makefile.
help:
	@grep '^##' -A1 Makefile

.PHONY: env
## Setup the development environment.
env:
	pipenv install '-e .' --dev

.PHONY: doc
## Generate the project documentation.
doc:
	pipenv run sphinx-apidoc -o doc/apidoc . *.py *test*
	pipenv run python setup.py build_sphinx

.PHONY: type
## Check the types of the source code.
type:
	pipenv run mypy .

.PHONY: lint
## Check the style of the source code.
lint:
	pipenv run flake8 .

.PHONY: test
## Run tests for the project packages.
test:
	pipenv run pytest */test/*.py

.PHONY: cov
## Generate coverage report from test.
cov:
	pipenv run pytest --cov . */test/

.PHONY: dist
## Create a wheel distribution package.
dist: clean
	pipenv run python setup.py bdist_wheel

.PHONY: check
## Check the project structure is valid.
check:
	pipenv check
	pipenv run python setup.py check

.PHONY: update
## Upgrade out-dated Pipfile dependencies.
update:
	pipenv update

.PHONY: upload
## Publish a package on the Pypi website.
upload: dist
	# remember to register with twine
	pipenv run twine upload dist/*.whl

## Perform a global project verification.
all: check test type lint cov doc dist;

## Purge down to the initialization stage.
clean_all: clean clean_env clean_doc;

## Purge down to the distribution stage.
clean: clean_dist clean_python;

## Purge the development environment.
clean_env:
	pipenv uninstall --all

## Purge generated documentation.
clean_doc:
	rm -rf doc/html/
	rm -rf doc/apidoc/
	rm -rf doc/doctrees/

## Purge distribution artifacts.
clean_dist:
	rm -rf dist/
	rm -rf build/

## Purge temporary Python files.
clean_python:
	find . -name '*.pyc' -exec rm -rf {} +
	find . -name '*.pyd' -exec rm -rf {} +
	find . -name '*.pyo' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -rf {} +
	find . -name '*.eggs' -exec rm -rf {} +
	find . -name '*.egg-info' -exec rm -rf {} +
