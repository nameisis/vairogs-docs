env-in-twig
===========

``github``: https://github.com/ravenflux/env-in-twig

    Twig extension that implements getenv in Twig template

Installation
------------

.. code-block:: console

    $ composer require ravenflux/env-in-twig

Configuration
-------------

.. tip::

    If you are using this library inside a Symfony application, it will be configured for you using flex
    recipe and config file will be created in ``config/packages/ravenflux_env_in_twig.yaml``.

.. code-block:: yaml

    # config/packages/ravenflux_env_in_twig.yaml
    services:
        ravenflux.twig.extension.env_in_twig:
            class: RavenFlux\Twig\EnvInTwigExtension
            tags:
                -
                    name: twig.extension

Usage
-----

.. code-block:: twig

    {{ getenv('APP_ENV') }}

