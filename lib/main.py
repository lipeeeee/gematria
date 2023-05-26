"""
    GEMATRIA Cryptography tool to aid in decyphering fo LP(Liber Primus)

    by lipeeeee
"""

import sys
import logging, coloredlogs
from arg_parser import ArgParser
from analyse import Analyse

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

def main() -> int:
    """GEMATRIA Entry Point"""
    
    # Parse args
    logger.info("PARSING ARGS")
    ap = ArgParser()
    parsed_args = ap.parse()
    message = parsed_args

    # Analyze
    logger.info("STARTING TO ANALYSE")
    a = Analyse(message)
    a.analyse()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

