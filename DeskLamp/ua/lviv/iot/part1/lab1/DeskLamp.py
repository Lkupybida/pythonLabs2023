class DeskLamp:
    instance = None

    def __init__(self, isOn=False, brightness=69, color='red', producer='I'):
        self.isOn = isOn
        self.brightness = brightness
        self.color = color
        self.producer = producer

    @staticmethod
    def getInstance():
        if DeskLamp.instance is None:
            DeskLamp.instance = DeskLamp()
        return DeskLamp.instance

    def turnOn(self):
        self.isOn = True

    def turnOff(self):
        self.isOn = False

    def setBrightness(self, value):
        if value < 1:
            self.brightness = 1
        elif value > 10:
            self.brightness = 10
        else:
            self.brightness = value

    def setColor(self, color):
        self.color = color
