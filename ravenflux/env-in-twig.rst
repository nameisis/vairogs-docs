env-in-twig
===========

github: https://github.com/ravenflux/env-in-twig

Installation
------------

.. code-block:: terminal

    $ composer require ravenflux/env-in-twig

.. tip::

    If you are using this library inside a Symfony application, it will be configured for you using flex
    recipe and config file will be created in config/packages/ravenflux_env_in_twig.yaml

Usage
-----

.. code-block:: twig

    {{ getenv('APP_ENV') }}

