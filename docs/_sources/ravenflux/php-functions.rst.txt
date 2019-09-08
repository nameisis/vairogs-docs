php-functions
=============

``github``: https://github.com/ravenflux/php-functions

    Twig extension that implements a way to use native PHP functions and filters in Twig template

Installation
------------

.. code-block:: console

    $ composer require ravenflux/php-functions

Configuration
-------------

.. tip::

    If you are using this library inside a Symfony application, it will be configured for you using flex
    recipe and config file will be created in ``config/packages/ravenflux_php_functions.yaml``.

.. code-block:: yaml

    # config/packages/ravenflux_php_functions.yaml
    services:
        ravenflux.twig.extension.php_functions:
            class: RavenFlux\Twig\PhpFunctionsExtension
            arguments:
                - #first argument are functions
                    - 'count'
                    - 'explode'
                - #second argument are filters
                    - 'nl2br'
                    - 'json_decode'
            tags:
                -
                    name: twig.extension

Function VS Filter | `source <https://stackoverflow.com/a/18867285/9743366>`_
-----------------------------------------------------------------------------

.. tip::

    * A ``function`` is used when you need to compute things to render the result.

    * A ``filter`` is a way to transform the displayed data.

Usage
-----

Functions:

.. code-block:: twig

    {{ count(users) }}

    {{ raven_function('count', users) }}

    {{ explode('::', '1,2,3') }}

    {{ raven_function('explode', '::', '1,2,3') }}

Filters:

.. code-block:: twig

    {{ user.name|nl2br }}

    {{ user.name|raven_filter('nl2br') }}

    {{ '[1,2,3]'|json_decode(true) }}

    {{ raven_filter('json_decode', '[1,2,3]', true) }}

.. tip::

    ``raven_function`` and ``raven_filter`` are dynamical calls and can take any existing php function
    as an argument.
