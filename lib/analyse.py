"""
    Main "Analyzing" script
"""

from __future__ import annotations
from hashing import Hashing
import logging, coloredlogs
logger = logging.getLogger(__name__)

class Analyse(object):

    message: str

    def __init__(self, message) -> None:
        self.message = message

    def hash_analyse(self) -> None:
        """Processes Hash"""
        logger.info(f"HASHING \"{self.message}\"...")
        h = Hashing(self.message)

        # blake2b
        b_hash = h.blake2b()
        print(f"Blake2b -> {b_hash} | IS_DEEPWEB_HASH -> {h.is_byte_deepweb_hash(b_hash)}")
    
        # sha512
        b_hash = h.sha512()
        print(f"SHA512 -> {b_hash} | IS_DEEPWEB_HASH -> {h.is_byte_deepweb_hash(b_hash)}")

    def analyse(self) -> None:
        """Main analyze function"""
        self.hash_analyse()

