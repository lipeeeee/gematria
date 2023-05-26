"""
    Hashing Script
"""

import hashlib

class Hashing(object):

    message: str
    b_message: bytes # bytes message

    DEEPWEB_HASH: str # DEEPWEB_HASH FROM LP

    def __init__(self, message: str) -> None:
        self.message = message
        self.b_message = self.message.encode('UTF-8')

        self.DEEPWEB_HASH = "36367763ab73783c7af284446c59466b4cd653239a311cb7116d4618dee09a8425893dc7500b464fdaf1672d7bef5e891c6e2274568926a49fb4f45132c2a8b4".encode('UTF-8')

    def blake2b(self) -> str:
        """Blake2b Hashing"""
        h = hashlib.blake2b(digest_size=64)
        h.update(self.b_message)
        return h.hexdigest()

    def sha512(self) -> str:
        """Sha512 Hashing"""
        h = hashlib.sha512()
        h.update(self.b_message)
        return h.hexdigest()

    def is_deepweb_hash(self) -> bool:
        """Checks if message given earlier is deepweb hash"""
        return self.is_byte_deepweb_hash(self.b_message)

    def is_byte_deepweb_hash(self, b_string: bytes) -> bool:
        """Checks if given byte str is the deepweb hash from LP"""
        if isinstance(b_string, str):
            b_string = b_string.encode('UTF-8')

        return b_string == self.DEEPWEB_HASH

if __name__ == "__main__":
    hashing = Hashing("teste")
    print(hashing.sha512())
    print(hashing.is_deepweb_hash())

