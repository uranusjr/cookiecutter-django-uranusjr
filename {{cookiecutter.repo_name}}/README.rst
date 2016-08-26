=============================
{{cookiecutter.project_name}}
=============================


Requirements
============

* Python 3.5 or above
* PostgreSQL 9.5 with a database available (by default named `{{cookiecutter.repo_name}}`)
* Ability to install `psycopg2` (usually available)


Development Environment Setup
==============================

Database Setup
--------------

You need to create a PostgreSQL database for the site.


Project Setup
-------------

Assuming you’re inside the project root (where this file locates).

First you need to provide some environment variables. This project supports
doing this via Dotenv, e.g. create ``.env`` in the project root with the
following content::

    DJANGO_SECRET_KEY=secret
    DJANGO_DATABASE_URL=postgres:///{{cookiecutter.repo_name}}


Now you can configure the webapp::

    pip install -Ur requirements/local.txt
    DJANGO_SETTINGS_MODULE=settings.local python manage.py migrate


Run Development server
=======================

In Un\*x shells::

    DJANGO_SETTINGS_MODULE=settings.local python manage.py runserver


Run Tests
==========

In Un\*x shells::

    DJANGO_SETTINGS_MODULE=settings.testing pytest --cov=site/apps site/apps
