# pylint: disable = unnecessary-dunder-call
"""
Create a list of DeskLamp objects with different configurations
"""
from desk_lamp import DeskLamp
from candle import Candle
from gas_light import GasLight
from search_light import Searchlight
from light_manager import LightManager
from decorator_manager import measure_execution_time, convert_output_to_tuple
from set_manager import SetManager
import logging
from exceptions import BrightnessMaxedOutException, InvalidProducerException

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
    lamps = manager.get_all_lights()
    for i in lamps:
        print(i)

    RESULTS = manager.get_results()
    print(RESULTS)

    set_manager = SetManager(manager)
    print(len(set_manager))
    print("testing")

    for variable in set_manager:
        print(variable)

    logging.basicConfig(filename='error.log', level=logging.ERROR)

    candle = Candle()
    try:
        candle.max_brightness()
    except BrightnessMaxedOutException as e:
        logging.error(str(e))
    candle.max_brightness()

    candle = Candle()
    try:
        candle.set_producer("China")
    except InvalidProducerException as e:
        logging.error(str(e))

    candle.set_producer("China")


@measure_execution_time
def add_numbers(*args):
    """
    Adds up any amount of numbers.
    """
    total = 0
    for num in args:
        total += num
    return total


@convert_output_to_tuple
def list_generator(list0):
    """
    Generates a list
    """
    list1 = list0
    list1 = [1, 2, 3]
    return list1


list2 = list_generator([1, 2])
print(list2)

RESULT = add_numbers(500, 700)
print(RESULT)

numbers = [10, 20]
RESULT = add_numbers(*numbers)
print(RESULT)
