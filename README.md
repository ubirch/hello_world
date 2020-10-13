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

1. Register your [UUID](https://www.uuidgenerator.net/)
 at https://console.prod.ubirch.com/
 and retrieve the "password" for your device
 
1. Insert your UUID and password in the example code.
    ```python
    uuid = UUID("<<insert your uuid>>")
    auth = "<<insert your device password>>"
    ```

1. Install dependencies:
    ```shell script
    $ pip install ubirch-protocol
    ```

1. Run the example:
    ```shell script
    $ python ./hello_world.py
    ``` 

### Further examples, verification etc.
A more elaborate example can be found here: [Python Example](https://github.com/ubirch/ubirch-protocol-python/blob/master/examples/example-client.py)
