"""
Searchlight class
"""
from light import Light


class Searchlight(Light):
    """
    A class representing a search_light.

    Attributes:
        is_on (bool): Whether the search_light is on or off.
        brightness (int): The brightness level of the search_light (1-10).
        producer (str): The producer of the search_light.
        operating_hours (int): The operating hours of the search_light.
    """


    def __init__(self, is_on=False, brightness=5, producer='Unknown', operating_hours=0):
        """
        Initialize a Searchlight object.

        Args:
            is_on (bool, optional): Whether the search_light is on or off. Defaults to False.
            brightness (int, optional): The brightness level of the search_light (1-10). Defaults to 5.
            producer (str, optional): The producer of the search_light. Defaults to 'Unknown'.
            operating_hours (int, optional): The operating hours of the search_light. Defaults to 0.
        """
        super().__init__(producer, operating_hours)
        self.is_on = is_on
        self.brightness = brightness
        self.colors_set = {"white", "SOS"}

    def turn_on(self):
        """
        Turn on the search_light.
        """
        self.is_on = True

    def turn_off(self):
        """
        Turn off the search_light.
        """
        self.is_on = False

    def set_brightness(self, value):
        """
        Set the brightness level of the search_light.

        Args:
            value (int): The brightness level (1-10).
        """
        if value < 1:
            self.brightness = 1
        elif value > 10:
            self.brightness = 10
        else:
            self.brightness = value

    def __str__(self):
        """
        Return a string representation of the Searchlight object.
        """
        return (
            f"Searchlight: is_on={self.is_on}, brightness={self.brightness}, "
            f"producer={self.producer}, operating_hours={self.operating_hours}"
        )

    @classmethod
    def do_something(cls):
        """
        Perform some action for the SearchLight object.
        """
        return "Searchlight is doing something"
