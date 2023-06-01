"""
light.py
"""

from abc import ABC, abstractmethod


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
    def __iter__(self):
        return iter(self.colors_set)

    def __init__(self, producer='Unknown', operating_hours=0):
        """
        Initialize a Light object.

        Args:
            producer (str, optional): The producer of the light source. Defaults to 'Unknown'.
            operating_hours (int, optional): The operating hours of the light source. Defaults to 0.
        """
        self.producer = producer
        self.operating_hours = operating_hours

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

    def __str__(self):
        """
        Return a string representation of the Light object.
        """
        return f"Light: producer={self.producer}, operating_hours={self.operating_hours}"
