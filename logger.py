import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "app.log"

# Ensure the logs directory exists
LOG_DIR.mkdir(parents=True, exist_ok=True)


def _create_handler(handler: logging.Handler, formatter: logging.Formatter) -> logging.Handler:
    """Helper to attach formatter to handler."""
    handler.setFormatter(formatter)
    return handler


def get_logger(name: str = __name__) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s")

        # Attach both file and console handlers
        logger.addHandler(_create_handler(
            logging.FileHandler(LOG_FILE), formatter))
        logger.addHandler(_create_handler(logging.StreamHandler(), formatter))

    return logger
