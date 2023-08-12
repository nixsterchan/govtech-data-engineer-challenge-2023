import pandas as pd
import re
import argparse
import logging

logging.basicConfig(
    filename='logger.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)


def main():
    logger.info('starting main code')
    return None


if __name__ == "__main__":
    main()