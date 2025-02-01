import logging.config
from logging import Logger

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger: Logger = logging.getLogger(__name__)