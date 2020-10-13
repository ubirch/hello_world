import ubirch
import binascii
import hashlib
import urllib
from uuid import UUID
from ubirch.ubirch_protocol import UBIRCH_PROTOCOL_TYPE_REG, UBIRCH_PROTOCOL_TYPE_BIN

# Config Variables --> register your UUID at https://console.prod.ubirch.com
# and retrieve the "password" for your device
# if you need to generate a new uuid go here https://www.uuidgenerator.net/
uuid = UUID("<<insert your uuid>>")
auth = "<<insert your device password>>"
env = "prod"

# test-message --> messages have to be unique, change content
test_message = "ubirch me!"


# implement a signing method for the ubirch-protocol to use for signing UPPs (Ubirch Protocol Packages)
class Proto(ubirch.Protocol):
    def __init__(self, key_store: ubirch.KeyStore, uuid: UUID) -> None:
        super().__init__()
        self.__ks = key_store

        # check if the device already has keys or generate a new pair
        if not keystore.exists_signing_key(uuid):
            keystore.create_ed25519_keypair(uuid)

    def _sign(self, uuid: UUID, message: bytes) -> bytes:
        return self.__ks.find_signing_key(uuid).sign(message)


# create a keystore
keystore = ubirch.KeyStore("demo-device.jks", "keystore")

# create an instance of the protocol
protocol = Proto(keystore, uuid)

# create an instance of the ubirch API and set the password
api = ubirch.API(env=env)
api.set_authentication(uuid, auth)

# register the public key at the UBIRCH key service
if not api.is_identity_registered(uuid):
    certificate = keystore.get_certificate(uuid)
    key_registration = protocol.message_signed(uuid, UBIRCH_PROTOCOL_TYPE_REG, certificate)
    r = api.register_identity(key_registration)
    print("key registration status code:", r.status_code)

# hash the test message
test_message_hash = hashlib.sha256(test_message.encode()).digest()
test_message_ascii=binascii.b2a_base64(test_message_hash, newline=False).decode()
print("message hash:", test_message_ascii)

# create a protocol message with the test message hash
upp = protocol.message_chained(uuid, UBIRCH_PROTOCOL_TYPE_BIN, test_message_hash)
# print("UPP: ", binascii.hexlify(upp).decode())

# send protocol message to ubirch backend
r = api.send(uuid, upp)
print("status code:", r.status_code)

#print verification link
print("https://ubirch.de/verifier/hash-verifier#hash="+urllib.parse.quote(str(test_message_ascii)))
