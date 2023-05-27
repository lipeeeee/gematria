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
        h.assert_hash_fn(h.blake2b, "BLAKE2B")
        
        # sha512
        h.assert_hash_fn(h.sha512, "SHA512")

        # sha3
        h.assert_hash_fn(h.sha3, "SHA3")

        # whirlpool
        h.assert_hash_fn(h.whirlpool, "WHIRLPOOL")

    def analyse(self) -> None:
        """Main analyze function"""
        self.hash_analyse()

