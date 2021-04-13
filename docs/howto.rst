How To - Project Documentation
======================================================================

TLDR
---------------------------------------------------------------------

::

    docker-compose -f local.yml up --build


Get Started
---------------------------------------------------------------------

Prerequisites:

- `Docker <https://docs.docker.com/docker-for-mac/install/>`_
- `Docker Compose <https://docs.docker.com/compose/>`_

Documentation can be written as rst files in the `wolf_and_badger/docs/_source`.


To build and serve docs, use the commands:
::

    docker-compose -f local.yml up docs


Changes to files in `docs/_source` will be picked up and reloaded automatically.

`Sphinx <https://www.sphinx-doc.org/>`_ is the tool used to build documentation.


Requires Docker to be installed:

::

    docker-compose -f local.yml build

    docker-compose -f local.yml up


Navigate to http://127.0.0.1:8000/

To use the Admin Panel, ensure you have created a superuser

::

    docker-compose -f local.yml run django python manage.py createsuperuser

Navigate to http://127.0.0.1:8000/admin/


View the Docs
^^^^^^^^^^^^^^^^

With the local development server running or run:

::

    docker-compose -f local.yml up docs

Navigate to http://127.0.0.1:7000/


Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

    docker-compose -f local.yml run django mypy wolf_and_badger

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage:

::

    docker-compose -f local.yml run django coverage run -m pytest

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    docker-compose -f local.yml run django pytest


Docstrings to Documentation
----------------------------------------------------------------------

The sphinx extension `apidoc <https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html/>`_ is used to automatically document code using signatures and docstrings.

Numpy or Google style docstrings will be picked up from project files and availble for documentation. See the `Napoleon <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/>`_ extension for details.

For an in-use example, see the `page source <_sources/users.rst.txt>`_ for :ref:`users`.

To compile all docstrings automatically into documentation source files, use the command, this can be done in the docker container:
::

    docker run --rm docs make apidocs
