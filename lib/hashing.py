"""
    Hashing Script
"""

import hashlib
import logging, coloredlogs
import whirlpool

logger = logging.getLogger(__name__)

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

    def whirlpool(self) -> str:
        """Whirlpool hashing"""
        h = whirlpool.new(self.b_message)
        return h.hexdigest()

    def sha3(self) -> str:
        """SHA3 64 digest hashing"""
        h = hashlib.sha3_512()
        h.update(self.b_message)
        return h.hexdigest()

    def assert_hash_fn(self, hash_fn, str_info) -> bool:
        """Assert if a hash function hashes to the DEEPWEB HASH"""
        h = hash_fn()
        is_deepweb_hash = self.is_byte_deepweb_hash(h)
        print(f"{str_info} -> {h} | IS_DEEPWEB_HASH() -> {is_deepweb_hash}")
        
        # Deepweb hash alert
        if is_deepweb_hash:
            import sys
            log.critical(f"FOUND DEEPWEB HASH IN {self.message} ENCODED IN {str_info}") 
            sys.exit(0)
        
        return is_deepweb_hash

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
    print("\n")
    print(hashing.whirlpool())
    print(hashing.is_deepweb_hash())

