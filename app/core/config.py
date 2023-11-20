import logging

logger = logging.getLogger(__name__)


def logger_config():
    logging.basicConfig(
        datefmt="%d.%m.%Y %H:%M:%S",
        format="%(asctime)s, %(levelname)s, %(message)s",
        level=logging.INFO,
    )
