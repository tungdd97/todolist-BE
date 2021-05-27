from src.helper import singleton
from src.common import LOG_CONF_FILE, FILE_LOG
import logging.config
import logging.handlers


@singleton
class SystemLog:

    def __init__(self):
        logging.config.fileConfig(LOG_CONF_FILE, None, disable_existing_loggers=False)
        self.logger = logging.getLogger('simpleTodoList')
        self.logger.addHandler(logging.handlers.RotatingFileHandler(filename=FILE_LOG))
