"""
    Main "Analyzing" script
"""

from __future__ import annotations
import logging, coloredlogs
logger = logging.getLogger(__name__)

class Analyze(object):

    message: str

    def __init__(self, message) -> None:
        self.message = message

    def hash_analyze(self) -> None:
        """Analyzes if a given string has 

