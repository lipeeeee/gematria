"""
    Utility functions for Gematria
"""

import logging, coloredlogs
logger = logging.getLogger(__name__)

def hamming_distance(string1: str, string2: str) -> int:
    """Calculates Hamming Distance between 2 strings"""
    if len(string1) != len(string2):
        logger.critical(f"[HAMMING DISTANCE] STRINGS MUST BE OF EQUAL LENGTH;\n1.{string1}\n2.{string2}")
        return 128

    if len(string1) != 128:
        logger.critical(f"[HAMMING DISTANCE] STRINGS ARE NOT 64 BIT DIGESTED;\n1.{string1}\n2.{string2}")
        return 128

    distance: int = 0
    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            distance += 1

    return distance

