from DeskLamp import DeskLamp

if __name__ == "__main__":
    """
    Create a list of DeskLamp objects with different configurations
    """
    lamps = [
        DeskLamp(),
        DeskLamp(True, 228, 'red', 'China'),
        DeskLamp.get_instance(),
        DeskLamp.get_instance()
    ]

    for i in lamps:
        print(i)
