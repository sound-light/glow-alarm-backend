from typing import Dict, Any

from logging import Formatter

class ANSIFormatter(Formatter):

    WHITE = '\033[1;37m'   # ANSI code for white
    GREEN = '\033[0;32m'   # ANSI code for green
    YELLOW = '\033[1;33m'   # ANSI code for yellow
    RED = '\033[31m'   # ANSI code for red
    RESET = '\033[0m'  # ANSI code to reset the colors

    def format(self, record):
        msg = super().format(record)
        if record.levelname == "DEBUG":
            msg = f"{self.WHITE}{msg}{self.RESET}"
        elif record.levelname == "INFO":
            msg = f"{self.GREEN}{msg}{self.RESET}"
        elif record.levelname == "WARNING":
            msg = f"{self.YELLOW}{msg}{self.RESET}"
        elif record.levelname == "ERROR":
            msg = f"{self.RED}{msg}{self.RESET}"
        else:
            msg = f"{self.RESET}{msg}"
        return msg

LOGGING_CONFIG: Dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "ansi_formatter": {
            "()": ANSIFormatter
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "ansi_formatter"  # Add the custom formatter
        }
    },
    "loggers": {
        "uvicorn": {"handlers": ["console"], "level": "INFO"},
        "uvicorn.access": {"handlers": ["console"], "level": "INFO"},
    },
    "root": {"handlers": ["console"], "level": "DEBUG"},
}
