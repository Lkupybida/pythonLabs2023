"""
GasLight class
"""
from light import Light


class GasLight(Light):
    """
    A class representing a gas_light.

    Attributes:
        is_on (bool): Whether the gas_light is on or off.
        producer (str): The producer of the gas_light.
        operating_hours (int): The operating hours of the gas_light.
    """

    def __init__(self, is_on=False, producer='Unknown', operating_hours=0):
        """
        Initialize a GasLight object.

        Args:
            is_on (bool, optional): Whether the gas_light is on or off. Defaults to False.
            producer (str, optional): The producer of the gas_light. Defaults to 'Unknown'.
            operating_hours (int, optional): The operating hours of the gas_light. Defaults to 0.
        """
        super().__init__(producer, operating_hours)
        self.is_on = is_on
        self.colors_set = {"yellowIsh", "blueIsh"}

    def turn_on(self):
        """
        Turn on the gas_light.
        """
        self.is_on = True

    def turn_off(self):
        """
        Turn off the gas_light.
        """
        self.is_on = False

    def __str__(self):
        """
        Return a string representation of the GasLight object.
        """
        return f"GasLight: is_on={self.is_on}, producer={self.producer}, operating_hours={self.operating_hours}"

    @classmethod
    def do_something(cls):
        """
        Perform some action for the GasLight object.
        """
        return "GasLight is doing something"