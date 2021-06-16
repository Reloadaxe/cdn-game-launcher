# -*- coding: utf-8 -*-
# !/usr/bin/python3

# Python standard dependencies
import os
import sys
import copy

import logging
import logging.handlers

from logging.handlers import RotatingFileHandler

VERBOSE = bool(os.environ.get('VERBOSE', 1))
LOGDIR = os.environ.get('LOGDIR', '/usr/logs')

LOGGER_NAMES = [
    'requests',
    'urllib3',
    'extract_msg',
    'PIL.PngImagePlugin',
    'mgrspy.mgrs',
    'elasticsearch',
    'pdfminer',
    'PIL',
    'PIL.Image',
    'PIL.TiffImagePlugin',
    'geocoder'
]

COLORS = {
    'CRITICAL': "\033[0;31m",
    'ERROR': "\033[1;91m",
    'WARNING': "\033[1;93m",
    'INFO': "\033[0;37m",
    'DEBUG': "\033[0;34m",
}


class LogFormatter(logging.Formatter):
    """Log Formatter class"""
    def format(self, record):
        record = copy.copy(record)
        levelname = record.levelname
        if levelname in COLORS:
            record.levelname = COLORS[levelname] + levelname + "\033[0m"
        return logging.Formatter.format(self, record)


class Logger:
    """Logger class

    The logger will use the LogFormatter and LogFilter classes.
    """
    logger = logging.getLogger('stock-manager')
    logger.setLevel(logging.DEBUG if VERBOSE else logging.INFO)

    logger.propagate = False
    logger.handlers = []  # Disable logging on default handler

    # Disable debug logging output for all dependencies to avoid bloating stdout
    logging.getLogger().setLevel(logging.WARNING if VERBOSE else logging.ERROR)
    for logger_name in LOGGER_NAMES:
        external_logger = logging.getLogger(logger_name)
        if external_logger:
            external_logger.setLevel(logging.WARNING if VERBOSE else logging.ERROR)

    log_dir = os.path.abspath(LOGDIR)

    try:
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
    except OSError:
        raise Exception('main.py: ERROR: Invalid log directory.\n')

    if VERBOSE:
        sys.stdout.write(f'main.py: INFO: Writing logs to {log_dir}.\n')

    file_formatter = logging.Formatter('%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s')
    file_handler = RotatingFileHandler(os.path.join(log_dir, 'stock-manager.log'), 'a', 20000000, 20)
    file_handler.setLevel(logging.DEBUG if VERBOSE else logging.INFO)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    stdout_formatter = LogFormatter('%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s')
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.INFO)
    stdout_handler.setFormatter(stdout_formatter)
    logger.addHandler(stdout_handler)

    @staticmethod
    def debug(*args, **kwargs):
        """Debug logging function."""
        Logger.logger.debug(*args, **kwargs)

    @staticmethod
    def info(*args, **kwargs):
        """Info logging function."""
        Logger.logger.info(*args, **kwargs)

    @staticmethod
    def warning(*args, **kwargs):
        """Warning logging function."""
        Logger.logger.warning(*args, **kwargs)

    @staticmethod
    def error(*args, **kwargs):
        """Error logging function."""
        Logger.logger.error(*args, **kwargs)

    @staticmethod
    def critical(*args, **kwargs):
        """Critical logging function."""
        Logger.logger.critical(*args, **kwargs)
