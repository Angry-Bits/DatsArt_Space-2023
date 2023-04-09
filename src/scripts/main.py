# !usr/bin/env python3

import requests

from src.logger import logger


def main(url: str = 'https://www.google.ru/') -> None:
    """Request checking script."""
    page = requests.get(url)
    if page.status_code:
        logger.info('К хакатону готовы!')


if __name__ == '__main__':
    main()
