"""
    GEMATRIA Cryptography tool to aid in decyphering fo LP(Liber Primus)

    by lipeeeee
"""

import sys
import logging, coloredlogs
from arg_parser import ArgParser

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

def main() -> int:
    """GEMATRIA Entry Point"""
    
    # Parse args
    ap = ArgParser()
    parser_args = ap.parse()
    logger.info(parser_args)
    return 0


if __name__ == "__main__":
    sys.exit(main())

