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
    echo Php::call(function() use ($model){
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
    echo $model->getBar(); # Bar
    Php::hijackSet($model, 'bar', 'foo');
    echo $model->getBar(); # Foo

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
    echo Php::hijackGet($model, 'bar'); # bar
