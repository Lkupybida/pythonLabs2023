class DeskLamp:
    """
    DeskLamp class for first lab
    """
    __instance = None

    def __init__(self, is_on=False, brightness=5, color='blue', producer='I'):
        """
        Initialize the DeskLamp object with default values
        """
        self.is_on = is_on
        self.brightness = brightness
        self.color = color
        self.producer = producer

    def __str__(self):
        """
        Return a string representation of the DeskLamp object
        """
        return f"{self.is_on}, {self.brightness}, {self.color}, {self.producer}"

    @classmethod
    def get_instance(cls):
        """
        Return a string representation of the DeskLamp object
        """
        if cls.__instance is None:
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
