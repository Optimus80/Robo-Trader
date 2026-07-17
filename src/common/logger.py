import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


logger = logging.getLogger("QuantBot")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

handler = RotatingFileHandler(
    LOG_DIR / "quantbot.log",
    maxBytes=10_000_000,
    backupCount=10
)

handler.setFormatter(formatter)

logger.addHandler(handler)
