"""
This script sets up different logging handlers for the Core module.
It provides console, file, and mail logging capabilities based on the
 provided settings.
"""
import logging
import os
from datetime import datetime


def _setup_console_handler(logger: logging.Logger, log_level: int) -> None:
    """
    Configure a console handler for the given logger
    :param logger: The logger instance to set up a console handler for
    :type logger: logging.Logger
    :param log_level: The log level for the console handler
    :type log_level: int
    :return: None
    :rtype: NoneType
    """
    console_handler: logging.StreamHandler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    logger.addHandler(console_handler)


def _create_logs_folder() -> str:
    """
    Create a logs folder if it doesn't already exist
    :return: The path to the logs folder
    :rtype: str
    """
    project_root: str = os.path.dirname(os.path.abspath(__file__))
    print(project_root)
    while os.path.basename(project_root) != "dojo_pep8":
        project_root = os.path.dirname(project_root)
    print("now:", project_root)
    logs_folder_path: str = f"{project_root}/logs"
    if not os.path.exists(logs_folder_path):
        os.makedirs(logs_folder_path, exist_ok=True)
    return logs_folder_path


def _build_log_filename() -> str:
    """
    Create a log filename using the current date and configured date
     format.
    :return: The filename for the log file
    :rtype: str
    """
    return f"log-{datetime.today().strftime('%d-%b-%Y-%H-%M-%S')}.log"


def _configure_file_handler(
        log_filename: str, log_level: int
) -> logging.FileHandler:
    """
    Configure a file handler with the given filename and log level
    :param log_filename: The filename for the log file
    :type log_filename: str
    :param log_level: The log level for the file handler
    :type log_level: int
    :return: A configured file handler
    :rtype: logging.FileHandle
    """
    fmt: str = "[%(name)s][%(asctime)s][%(levelname)s][%(module)s]" \
               "[%(funcName)s][%(lineno)d]: %(message)s"
    date_fmt: str = "%Y-%m-%d %H:%M:%S"
    formatter: logging.Formatter = logging.Formatter(fmt, date_fmt)
    file_handler: logging.FileHandler = logging.FileHandler(log_filename)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    return file_handler


def _setup_file_handler(
        logger: logging.Logger, log_level: int,
) -> None:
    """
    Configure a file handler for the given logger
    :param logger: The logger instance to set up a file handler for
    :type logger: logging.Logger
    :param log_level: The log level for the file handler
    :type log_level: int
    :return: None
    :rtype: NoneType
    """
    logs_folder_path = _create_logs_folder()
    log_filename = _build_log_filename()
    filename_path: str = f"{logs_folder_path}/{log_filename}"
    file_handler = _configure_file_handler(filename_path, log_level)
    logger.addHandler(file_handler)
    file_handler.flush()


def setup_logging(
        log_level: int = logging.ERROR,
) -> None:
    """
    Initialize logging for the application
    :param log_level: The log level to use for the application.
     Defaults to DEBUG
    :type log_level: int
    :return: None
    :rtype: NoneType
    """
    logger: logging.Logger = logging.getLogger()
    logger.handlers.clear()
    logger.propagate = False
    logger.setLevel(log_level)
    _setup_console_handler(logger, log_level)
    _setup_file_handler(logger, log_level)
