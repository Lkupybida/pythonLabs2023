from DeskLamp import DeskLamp

if __name__ == "__main__":
    lamps = [
        DeskLamp(),
        DeskLamp(True, 228, 'green', 'AM'),
        DeskLamp(True, 420, 'blue', 'SPEED'),
    ]

    for i, lamp in enumerate(lamps):
        print(f"Lamp {i+1}: is_on = {lamp.is_on}, brightness = {lamp.brightness}, color = {lamp.color}, producer = {lamp.producer}")
