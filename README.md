# Hello World in Python3

This is a bare-minimum implementation of the [ubirch-protocol](https://github.com/ubirch/ubirch-protocol)
for [Python 3](https://www.python.org/). Please see [ubirch-protocol](https://github.com/ubirch/ubirch-protocol)
for details.

The library consists of three parts which can be used individually:

* `ubirch.API` - a python layer covering the ubirch backend REST API
* `ubirch.Protocol` - the protocol compiler which packages messages and handles signing and verification
* `ubirch.KeyStore` - a simple key store based on [pyjks](https://pypi.org/project/pyjks/) to store keys and certificates

> the [ubirch](https://ubirch.com) protocol uses the [Ed25519](https://ed25519.cr.yp.to/) signature scheme by default.

### Quick Start

1. Install dependencies.
    ```shell script
    $ pip install ubirch-protocol
    ```

1. Register your [UUID](https://www.uuidgenerator.net/)
 at https://console.prod.ubirch.com/
 and retrieve the "password" for your device

1. Insert your UUID and password in the example code.
    ```python
    uuid = UUID("<<insert your uuid>>")
    auth = "<<insert your device password>>"
    ```

1. Insert your own message in the example code.
    ```python
    test_message = "ubirch me!"
    ```
   > The message has to be unique! You'll get a **`409`** status code, if you try to anchor an already anchored message.

1. Run the example.
    ```shell script
    $ python ./hello_world.py
    ``` 
   
   The output should look like this:
   ```
    key registration status code: 200
    message hash: FJXjDsX0jS3pEX7H28pvkp7brOPWqCfzl1V7fqv+P10=
    status code: 200
    https://ubirch.de/verifier/hash-verifier#hash=FJXjDsX0jS3pEX7H28pvkp7brOPWqCfzl1V7fqv+P10=
   ```

1. Verify your message hash at https://ubirch.de/verifier/hash-verifier

### Further examples, verification etc.
A more elaborate example can be found here: [Python Example](https://github.com/ubirch/ubirch-protocol-python/blob/master/examples/example-client.py)
