"""
Candle class
"""
from light import Light


class Candle(Light):
    """
    A class representing a candle.

    Attributes:
        is_lit (bool): Whether the candle is lit or not.
        producer (str): The producer of the candle.
        operating_hours (int): The operating hours of the candle.
    """

    def __init__(self, is_lit=False, producer='Unknown', operating_hours=0):
        """
        Initialize a Candle object.

        Args:
            is_lit (bool, optional): Whether the candle is lit or not. Defaults to False.
            producer (str, optional): The producer of the candle. Defaults to 'Unknown'.
            operating_hours (int, optional): The operating hours of the candle. Defaults to 0.
        """
        super().__init__(producer, operating_hours)
        self.is_lit = is_lit
        self.colors_set = {"fiery"}

    def turn_on(self):
        """
        Turn on the candle by lighting it.
        """
        self.is_lit = True

    def turn_off(self):
        """
        Turn off the candle by extinguishing it.
        """
        self.is_lit = False

    def __str__(self):
        """
        Return a string representation of the Candle object.
        """
        return f"Candle: is_lit={self.is_lit}, producer={self.producer}, operating_hours={self.operating_hours}"

    @classmethod
    def do_something(cls):
        """
        Perform some action for the Candle object.
        """
        return "Candle is doing something"