Php
===

.. code-block:: php

    use Vairogs\Utils\Php;

.. code-block:: php

    class Foo
    {
        private $bar = 'bar';

        public function getBar()
        {
            return $this->upper($this->bar);
        }

        private function upper($string)
        {
            retun ucfirst($string);
        }
    }

- Call any function in class (``any visibility``)

.. code-block:: php

    /**
     * @param callable $function
     * @param object $clone
     * @param bool $return
     *
     * @return mixed
     */
    public static function call(callable $function, object $clone, bool $return = false);

.. code-block:: php

    $model = new Foo();
    Php::call(function() use ($model){
        return $model->upper('test');
    }, $model, true); # Test

- Set value to any class variable (``any visibility``)

.. code-block:: php

    /**
     * @param object $object
     * @param string $property
     * @param $value
     */
    public static function hijackSet(object $object, string $property, $value): void;

.. code-block:: php

    $model = new Foo();
    $model->getBar(); # Bar
    Php::hijackSet($model, 'bar', 'foo');
    $model->getBar(); # Foo

- Get value of any class variable (``any visibility``)

.. code-block:: php

    /**
     * @param object $object
     * @param string $property
     *
     * @return mixed
     */
    public static function hijackGet(object $object, string $property);

.. code-block:: php

    $model = new Foo();
    Php::hijackGet($model, 'bar'); # bar

- Get bool value from variable

.. code-block:: php

    /**
     * @param $value
     *
     * @return bool
     */
    public static function boolval($value): bool;

.. code-block:: php

    Php::boolval(1);      # true
    Php::boolval(2);      # false
    Php::boolval(true);   # true
    Php::boolval('yes');  # true
    Php::boolval('true'); # true
    Php::boolval('n');    # false

- Returns constants of given class

.. code-block:: php

    /**
     * @param string $class
     *
     * @return array
     * @throws VairogsException
     * @throws ReflectionException
     */
    public static function getClassConstants(string $class): array;

.. code-block:: php

    use Symfony\Component\HttpFoundation\Response;

    Php::getClassConstants(Response::class); # ['HTTP_CONTINUE' => 100, 'HTTP_SWITCHING_PROTOCOLS' => 101, ...]
