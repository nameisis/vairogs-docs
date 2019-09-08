Util
====

.. code-block:: php

    use Vairogs\Utils\Util;

- Returns ``true`` if given number is ``prime``

.. code-block:: php

    /**
     * @param int $number
     *
     * @return bool
     */
    public static function isPrime(int $number): bool;

.. code-block:: php

    Util::isPrime(7); # true

    Util::isPrime(4); # false
