Json
====

.. code-block:: php

    use Vairogs\Utils\Json;

Json class is using basic json functions but making them safer

- json_encode

.. code-block:: php

    /**
     * @param $value
     * @param int $flags
     *
     * @return string
     * @throws JsonException
     */
    public static function encode($value, int $flags = 0): string;

.. code-block:: php

    Json::encode([1,2,3]); # '[1,2,3]'

- json_decode

.. code-block:: php

    /**
     * @param string $json
     * @param int $flags
     *
     * @return mixed
     * @throws JsonException
     */
    public static function decode(string $json, int $flags = 0);

.. code-block:: php

    Json::decode('[1,2,3]'); # [1,2,3]
