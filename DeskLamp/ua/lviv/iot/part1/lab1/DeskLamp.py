class DeskLamp:
    instance = None

    def __init__(self, is_on=False, brightness=69, color='red', producer='I'):
        self.is_on = is_on
        self.brightness = brightness
        self.color = color
        self.producer = producer

    @staticmethod
    def get_instance():
        if DeskLamp.instance is None:
            DeskLamp.instance = DeskLamp()
        return DeskLamp.instance

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_brightness(self, value):
        if value < 1:
            self.brightness = 1
        elif value > 10:
            self.brightness = 10
        else:
            self.brightness = value

    def set_color(self, color):
        self.color = color
