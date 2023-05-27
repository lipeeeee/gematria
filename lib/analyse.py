"""
    Main "Analyzing" script
"""

from __future__ import annotations
from hashing import Hashing
from writer import Writer
import logging, coloredlogs

logger = logging.getLogger(__name__)

class Analyse(object):
    """Class that will take a message and do processing on the string"""

    # String to be processed
    message: str
    
    # Custom file writer
    writer: Writer

    def __init__(self, message: str, writer: Writer) -> None:
        self.message = message
        self.writer = writer

    def hash_analyse(self) -> None:
        """Processes Hash"""
        # Logging
        output_str = f"HASHING \"{self.message}\"..."
        logger.info(output_str)
        self.writer.title(output_str)

        # Hashing obj
        h = Hashing(self.message, self.writer)

        # blake2b
        h.assert_hash_fn(h.blake2b, "BLAKE2B")
    
        # blake512
        h.assert_hash_fn(h.blake512, "BLAKE512")

        # sha512
        h.assert_hash_fn(h.sha512, "SHA512")

        # sha3
        h.assert_hash_fn(h.sha3, "SHA3")

        # whirlpool
        h.assert_hash_fn(h.whirlpool, "WHIRLPOOL")

        # Skein512
        h.assert_hash_fn(h.skein512, "SKEIN512")

        # Tiger
        h.assert_hash_fn(h.tiger, "TIGER")

    def analyse(self) -> None:
        """Main analyze function"""
        self.hash_analyse()

