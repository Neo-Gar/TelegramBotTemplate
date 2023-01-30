import logging
import datetime
import sys
from pathlib import Path
import yaml
from logging import config

BASE_DIR = Path(__file__).resolve().parent.parent.parent
BASE_LOGS_DIR = f'{BASE_DIR}/logs/base'
DEBUG_LOGS_DIR = f'{BASE_DIR}/logs/debug'
ENABLE_CORE_SQL_LOGS = False


def init(mode):

    # load config
    if mode == 'base':
        with open(f'{BASE_DIR}/modules/logs/base_config.yaml', 'r') as file:
            log_cfg = yaml.safe_load(file.read())

        config.dictConfig(log_cfg)
    elif mode == 'debug':
        with open(f'{BASE_DIR}/modules/logs/debug_config.yaml', 'r') as file:
            log_cfg = yaml.safe_load(file.read())

        config.dictConfig(log_cfg)

    # base logger
    if mode == 'base':
        base_logger = logging.getLogger('base')
        base_file_handler = logging.FileHandler(
            filename=f'{BASE_LOGS_DIR}/{Path(__file__).name}_{datetime.datetime.now().strftime("%Y-%m-%d")}.log'
        )
        base_file_formatter = logging.Formatter(
            '[%(asctime)s] [%(filename)s] [%(funcName)s] [%(levelname)s]: %(message)s'
        )
        base_file_handler.setFormatter(base_file_formatter)
        base_logger.addHandler(base_file_handler)
        base_logger.propagate = False
        return base_logger

    # debug logger
    elif mode == 'debug':
        debug_logger = logging.getLogger('debug')
        debug_file_handler = logging.FileHandler(
            filename=f'{DEBUG_LOGS_DIR}/{Path(__file__).name}_{datetime.datetime.now().strftime("%Y-%m-%d")}.log'
        )
        base_file_formatter = logging.Formatter(
            '[%(asctime)s] [%(filename)s] [%(funcName)s] [%(levelname)s]: %(message)s'
        )
        debug_file_handler.setFormatter(base_file_formatter)
        debug_logger.addHandler(debug_file_handler)
        debug_logger.propagate = False
        return debug_logger


def get_logger():

    logger = init('base')

    if len(sys.argv) >= 2:
        if sys.argv[1] == '-debug':
            logger = init('debug')

    return logger


logger = get_logger()
