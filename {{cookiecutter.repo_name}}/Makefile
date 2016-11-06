ALL: help

.PHONY: help


help:
	@echo "Available commands: test lint"

test:
	py.test site --cov=site/apps

lint:
	flake8 site
