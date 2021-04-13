Wolf and Badger
===============

Prerequisites

- `Docker <https://docs.docker.com/docker-for-mac/install/>`_
- `Docker Compose <https://docs.docker.com/compose/>`_


Local deployment
^^^^^^^^^^^^^^^^

Requires Docker to be installed:

::

  $ docker-compose -f local.yml build
  $ docker-compose -f local.yml up


Navigate to http://127.0.0.1:8000/

To use the Admin Panel, ensure you have created a superuser

::

  $ docker-compose -f local.yml run django python manage.py createsuperuser

Navigate to http://127.0.0.1:8000/admin/


View the Docs
^^^^^^^^^^^^^^^^

With the local development server running or run:

::

  $ docker-compose -f local.yml up docs

Navigate to http://127.0.0.1:7000/


Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ docker-compose -f local.yml run django mypy wolf_and_badger

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage:

::

    $ docker-compose -f local.yml run django coverage run -m pytest

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ docker-compose -f local.yml run django pytest

:License: MIT


TODO
^^^^

- Disconnect SocialAuth once account is deleted
- Cleaner way of adding and managing addresses for a user
- Improve test coverage
