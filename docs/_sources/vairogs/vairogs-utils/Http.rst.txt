Http
====

.. code-block:: php

    use Vairogs\Utils\Http;
    use Symfony\Component\HttpFoundation\Request;

- Returns ``schema`` of given $request

.. code-block:: php

    Http::getSchema(Request $request); # http:// or https://

- Returns ``true`` if given $request uses ``https`` schema

.. code-block:: php

    Http::useHttps(Request $request); # true or false

- Returns ``client ip`` from current ``http`` $request

.. code-block:: php

    Http::getRemoteIp(Request $request, true); # 127.0.0.1

- Returns ``client ip`` from current ``https`` $request

.. code-block:: php

    Http::getRemoteIp(Request $request, false); # 127.0.0.1

- Returns ``true`` if given $path is ``absolute``

.. code-block:: php

    Http::isAbsolute('https://docs.vairogs.com'); # true

    Http::isAbsolute('docs.vairogs.com'); # false

    Http::isAbsolute('//docs.vairogs.com'); # true
