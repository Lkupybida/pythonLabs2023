# pylint disable = invalid-name
# pylint disable = invalid-name
"""
DeskLamp class
"""
from light import Light


# from exceptions import BrightnessMaxedOutException, InvalidProducerException


class DeskLamp(Light):
    """
    Private variable instance
    """
    instance = None

    def __init__(self, is_on=False, brightness=5, color='white',
               producer='Unknown', operating_hours=0):
        """
        Initialize the DeskLamp object with default values
        isOn: logical value which shows if lamp is on, by default False
        brightness: lamps brightness value ranges from 1 to 10, by default 5
        color: lamps color of light, by default white
        producer: producer of the lamp, by default Unknown
        """
        super().__init__(10, producer, operating_hours)
        self.is_on = is_on
        self.brightness = brightness
        self.color = color
        self.producer = producer

    def __str__(self):
        return (
            f"DeskLamp: is_on={self.is_on}, brightness={self.brightness}, "
            f"color={self.color}, producer={self.producer}, "
            f"operating_hours={self.operating_hours}"
        )

    @classmethod
    def get_instance(cls):
        """
        Return a string representation of the DeskLamp object
        """
        if not cls.__instance:
            cls.__instance = DeskLamp()
        return cls.__instance

    def turn_on(self):
        """
        Turn on the desk lamp
        """
        self.is_on = True

    def turn_off(self):
        """
        Turn off the desk lamp
        """
        self.is_on = False

    def set_brightness(self, value):
        """
        Set the brightness of the desk lamp within a valid range
        """
        if value < 1:
            self.brightness = 1
        elif value > 10:
            self.brightness = 10
        else:
            self.brightness = value

    def set_color(self, color):
        """
        Set the color of the desk lamp
        """
        self.color = color

    @classmethod
    def do_something(cls):
        """
        Perform some action for the Candle object.
        """
        return "Candle is doing something"

    def set_max_brightness(self):
        """
        Method to set max brightness
        """
        super().max_brightness()
