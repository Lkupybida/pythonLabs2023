"""
Create a list of DeskLamp objects with different configurations
"""
from desk_lamp import DeskLamp
from candle import Candle
from gas_light import GasLight
from search_light import Searchlight
from light_manager import LightManager

if __name__ == "__main__":

    manager = LightManager()

    lamp = DeskLamp(True, 8, 'red', 'China', 100)
    candle = Candle(True, 'Beeswax', 10)
    gas_light = GasLight(False, 'Propane', 50)
    searchlight = Searchlight(True, 8, 'Unknown', 100)
    manager.add_light(candle)
    manager.add_light(gas_light)
    manager.add_light(searchlight)
    manager.add_light(lamp)

    """
    Access the lights through the light manager
    """
    lamps = manager.get_all_lights()
    for i in lamps:
        print(i)


def add_numbers(*args):
    """
    Adds up any amount of numbers.
    """
    total = 0
    for num in args:
        total += num
    return total


result = add_numbers(500, 700)
print(result)

numbers = [10, 20]
result = add_numbers(*numbers)
print(result)
