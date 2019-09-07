sort-functions
===========

github: https://github.com/ravenflux/sort-functions

Installation
------------

.. code-block:: terminal

    $ composer require ravenflux/sort-functions

.. tip::

    If you are using this library inside a Symfony application, it will be configured for you using flex
    recipe and config file will be created in config/packages/ravenflux_sort_functions.yaml

Usage
-----

.. code-block:: twig

    {% for user in users|usort('name') %}
        {{ user.name }}
    {% endfor %}

.. code-block:: twig

    {% for user in users|usort('name', 'DESC') %}
        {{ user.name }}
    {% endfor %}
