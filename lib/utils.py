"""
    Utility functions for Gematria
"""

from __future__ import annotations
import os
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

def file_into_array(file_path: str) -> List:
    """Read file contents into an array seperating by EOL"""
    content = []
    
    # Read content
    with open(file_path) as f:
        content = f.readlines()
    
    # Remove "\n" from content
    formated_content = [c[:-1] for c in content]

    return formated_content
