import logging

from .logging_setup import setup_logging
from .settings import settings


def main() -> None:
    setup_logging(settings.log_level)
    logging.getLogger("sample_app").info("hello")
