"""
light.py
"""
from abc import ABC, abstractmethod
from plistlib import InvalidFileException
from exceptions import BrightnessMaxedOutException, InvalidProducerException, logged


class Light(ABC):
    """
    Abstract base class representing a light source.

    Attributes:
        producer (str): The producer of the light source.
        operating_hours (int): The operating hours of the light source.
        colors_set (set): The colors of the light source.
    """
    colors_set = set()
    """
    Declare an empty set as a class attribute
    """

    def iter(self):
        return iter(self.colors_set)

    def __init__(self, brightness_limit, producer='Unknown', operating_hours=0):
        """
        Initialize a Light object.

        Args:
            brightness_limit:
            producer (str, optional): The producer of the light source. Defaults to 'Unknown'.
            operating_hours (int, optional): The operating hours of the light source. Defaults to 0.
        """
        self.producer = producer
        self.operating_hours = operating_hours
        self.brightness_limit = brightness_limit
        self.brightness = 0

    @abstractmethod
    def turn_on(self):
        """
        Abstract method to turn on the light source.
        """

    @abstractmethod
    def turn_off(self):
        """
        Abstract method to turn off the light source.
        """

    def str(self):
        """
        Return a string representation of the Light object.
        """
        return f"Light: producer={self.producer}, operating_hours={self.operating_hours}"

    @logged(BrightnessMaxedOutException, "file")
    def max_brightness(self):
        """
        Method to set max brightness
        """
        if self.brightness >= self.brightness_limit:
            raise BrightnessMaxedOutException("Brightness is already at the maximum level")
        self.brightness = self.brightness_limit
        return self.brightness

    @logged(InvalidProducerException, "file")
    def set_producer(self, producer):
        """
        Method to set producer
        """
        if not self.is_valid_producer():
            raise InvalidFileException("Invalid producer")
        self.producer = producer

    @classmethod
    def is_valid_producer(cls):
        """
        Method to check producer validity
        """
        return True
