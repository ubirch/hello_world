# Hello World in Python3

This is a bare-minimum implementation of the [ubirch-protocol](https://github.com/ubirch/ubirch-protocol)
for [Python 3](https://www.python.org/). Please see [ubirch-protocol](https://github.com/ubirch/ubirch-protocol)
for details.

The library consists of three parts which can be used individually:

* `ubirch.API` - a python layer covering the ubirch backend REST API
* `ubirch.Protocol` - the protocol compiler which packages messages and handles signing and verification
* `ubirch.KeyStore` - a simple key store based on [pyjks](https://pypi.org/project/pyjks/) to store keys and certificates

> the [ubirch](https://ubirch.com) protocol uses the [Ed25519](https://ed25519.cr.yp.to/) signature scheme by default.
 
## Usage

Install the library: `pip install ubirch-protocol`
  
### Hello World

```python
import ubirch
import hashlib
import json
from ed25519 import VerifyingKey, BadSignatureError
from uuid import UUID
from ubirch.ubirch_protocol import UBIRCH_PROTOCOL_TYPE_REG, UBIRCH_PROTOCOL_TYPE_BIN

# Config Variables --> register your UUID at https://console.prod.ubirch.com
uuid = UUID("<<insert your uuid>>")
authkey = "<<insert your device password>>"
env = "prod"

# Implement the ubirch-protocol with signing and saving the signatures
class Proto(ubirch.Protocol):
    def __init__(self, key_store: ubirch.KeyStore, uuid: UUID) -> None:
        super().__init__()
        self.__ks = key_store

        # check if the device already has keys or generate a new pair
        if not keystore.exists_signing_key(uuid):
            keystore.create_ed25519_keypair(uuid)

    def _sign(self, uuid: UUID, message: bytes) -> bytes:
        return self.__ks.find_signing_key(uuid).sign(message)

# create a keystore and insert the verifying key
keystore = ubirch.KeyStore("demo-device.jks", "keystore")

# create an instance of the protocol with signature saving
protocol = Proto(keystore, uuid)

# create an instance of the ubirch API and set the password
# register your UUID at https://console.prod.ubirch.com and retrieve your password
api = ubirch.API(env=env)
api.set_authentication(uuid, authkey)  

# register the public key at the UBIRCH key service
if not api.is_identity_registered(uuid):
    certificate = keystore.get_certificate(uuid)
    key_registration = protocol.message_signed(uuid, UBIRCH_PROTOCOL_TYPE_REG, certificate)
    r = api.register_identity(key_registration)

# test-message --> messages have to be unique, change content if sending more than once
message = {'ts': 124, 'data': 'hello world!'}
serialized = json.dumps(message, separators=(',', ':'), sort_keys=True, ensure_ascii=False).encode()
msg = protocol.message_chained(uuid, 0x53, hashlib.sha256(serialized).digest())

# send message to ubirch backend
r = api.send(uuid, msg)
print(msg)
print(r.status_code)
```

### Further examples, verification etc.
A more elaborate example including error-handling, logging and verification can be found here: [Python Example](https://github.com/ubirch/ubirch-protocol-python/blob/master/examples/example-client.py)
