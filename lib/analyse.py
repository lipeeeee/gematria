"""
    Main "Analyzing" script
"""

from __future__ import annotations
from .hashing import Hashing
from .writer import Writer
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
        self.hasher = Hashing(self.message, self.writer)

    def analyse(self) -> None:
        """Main analyze function"""
        # Hash and compare string into all implemented hash fn's
        self.hasher.str_check()

