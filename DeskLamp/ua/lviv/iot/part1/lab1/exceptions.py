"""
exeptions.py file
"""
import logging


class BrightnessMaxedOutException(Exception):
    """
    BrightnessMaxedOutException exeption
    """


class InvalidProducerException(Exception):
    """
    InvalidProducerException exeption
    """


def logged(exception, mode):
    """
    Method logged
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e_e:
                if mode == "console":
                    logging.error(str(e_e))
                elif mode == "file":
                    logging.basicConfig(filename='error.log', level=logging.ERROR)
                    logging.error(str(e_e))
                else:
                    raise ValueError("Invalid logging mode") from e_e

        return wrapper

    return decorator
