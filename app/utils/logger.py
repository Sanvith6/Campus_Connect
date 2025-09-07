import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("CEMS")
logger.setLevel(logging.DEBUG)

# Rotating file handler (10 MB per file, keep 5 backups)
file_handler = RotatingFileHandler(
    os.path.join(LOG_DIR, "cems.log"), maxBytes=10*1024*1024, backupCount=5
)
file_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Optional console output for dev
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
