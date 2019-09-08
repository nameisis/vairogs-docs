sort-functions
==============

``github``: https://github.com/ravenflux/sort-functions

    Twig extension that implements sorting functions in Twig template

Installation
------------

.. code-block:: twig

    $ composer require ravenflux/sort-functions

Configuration
-------------

.. tip::

    If you are using this library inside a Symfony application, it will be configured for you using flex
    recipe and config file will be created in ``config/packages/ravenflux_sort_functions.yaml``.

.. code-block:: yaml

    # config/packages/ravenflux_sort_functions.yaml
    services:
        ravenflux.twig.extension.sort_functions:
            class: RavenFlux\Twig\SortExtension
            tags:
                -
                    name: twig.extension

Usage
-----

Sort functions will work on any iterable object or array with associative keys and that has given parameter
as a key, public variable or has get{Parameter}() function.

.. code-block:: twig

    {% for user in users|usort('name') %}
        {{ user.name }}
    {% endfor %}

.. code-block:: twig

    {% for user in users|usort('name', 'DESC') %}
        {{ user.name }}
    {% endfor %}
