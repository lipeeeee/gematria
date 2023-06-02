"""
    Hashing Script
"""

import hashlib
import logging, coloredlogs
import whirlpool
import blake512 # https://github.com/tweqx/python-blake512
import skein # https://pythonhosted.org/pyskein/skein.html
from tigerhash import tiger
from writer import Writer

logger = logging.getLogger(__name__)

class Hashing(object):
    """Hashing class that will handle all hashing of a specified string"""

    # String to be hased
    message: str
    b_message: bytes # bytes message

    # DEEPWEB HASH FROM LP
    DEEPWEB_HASH: str

    # Custom file writer
    writer: Writer

    def __init__(self, message: str, writer: Writer) -> None:
        self.message = message
        self.b_message = self.message.encode('UTF-8')
        self.writer = writer

        self.DEEPWEB_HASH = "36367763ab73783c7af284446c59466b4cd653239a311cb7116d4618dee09a8425893dc7500b464fdaf1672d7bef5e891c6e2274568926a49fb4f45132c2a8b4".encode('UTF-8')

    def blake2b(self) -> str:
        """Blake2b Hashing"""
        h = hashlib.blake2b(digest_size=64)
        h.update(self.b_message)
        return h.hexdigest()
    
    def blake512(self) -> str:
        """Blake1-512 Hashing"""
        h = blake512.hash(self.message)
        return h

    def sha512(self) -> str:
        """Sha512 Hashing"""
        h = hashlib.sha512()
        h.update(self.b_message)
        return h.hexdigest()

    def sha3(self) -> str:
        """SHA3 64 digest hashing"""
        h = hashlib.sha3_512()
        h.update(self.b_message)
        return h.hexdigest()

    def whirlpool(self) -> str:
        """Whirlpool hashing"""
        h = whirlpool.new(self.b_message)
        return h.hexdigest()

    def skein512(self) -> str:
        """Skein512 Hashing"""
        h = skein.skein512()
        h.update(self.b_message)
        return h.hexdigest()

    def tiger(self) -> str:
        """TigerHash Hashing"""
        return "NOT WORKING ATM"
        h = tiger.hash(self.message)
        return h

    def assert_hash_fn(self, hash_fn, str_info) -> bool:
        """Assert if a hash function hashes to the DEEPWEB HASH"""
        h = hash_fn()
        is_deepweb_hash = self.is_byte_deepweb_hash(h)
        
        output_str = f"{str_info} -> {h} | IS_DEEPWEB_HASH() -> {is_deepweb_hash}"
        print(output_str)
        if True: # False if u dont want file printing
            self.writer.write(output_str)

        # Deepweb hash alert
        if is_deepweb_hash:
            import sys
            log.critical(f"FOUND DEEPWEB HASH IN {self.message} ENCODED IN {str_info}") 
            sys.exit(0)
        
        return is_deepweb_hash

    def str_check(self) -> bool:
        """For every hash function:
            1. Hash string
            2. Compare to DWH
        """
        # Logging
        output_str = f"HASHING \"{self.message}\"..."
        logger.info(output_str)
        self.writer.title(output_str)

        # blake2b
        self.assert_hash_fn(self.blake2b, "BLAKE2B")
    
        # blake512
        self.assert_hash_fn(self.blake512, "BLAKE512")

        # sha512
        self.assert_hash_fn(self.sha512, "SHA512")

        # sha3
        self.assert_hash_fn(self.sha3, "SHA3")

        # whirlpool
        self.assert_hash_fn(self.whirlpool, "WHIRLPOOL")

        # Skein512
        self.assert_hash_fn(self.skein512, "SKEIN512")

        # Tiger
        self.assert_hash_fn(self.tiger, "TIGER")

    def is_deepweb_hash(self) -> bool:
        """Checks if message given earlier is deepweb hash"""
        # TODO goes through every hashing algorithm and check if it is
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

