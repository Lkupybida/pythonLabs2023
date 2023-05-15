"""
Create a list of DeskLamp objects with different configurations
"""
from desk_lamp import DeskLamp

if __name__ == "__main__":
    lamps = [
        DeskLamp(),
        DeskLamp(True, 9, 'red', 'China'),
        DeskLamp.get_instance(),
        DeskLamp.get_instance()
    ]
    for i in lamps:
        print(i)

def add_list_of_numbers(args):
    """
    Adds up any amount of numbers.
    """
    total = 0
    for num in args:
        total += num
    return total

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
