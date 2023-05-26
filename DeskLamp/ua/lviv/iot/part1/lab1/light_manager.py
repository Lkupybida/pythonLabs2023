from light import Light
from decorator_manager import measure_execution_time, convert_output_to_tuple
from candle import Candle

class LightManager:
    """
    Class representing a light manager.
    Attributes:
        lights (list): List of light sources.
    """

    def __init__(self):
        """
        Initialize a LightManager object.
        """
        self.lights = []

    def get_elements(self):
        """
        Get the set of elements for each light source in the light manager.
        Returns:
            dict: A dictionary with light sources as keys and their sets of elements as values.
        """
        return {light: set(light) for light in self.lights}

    @measure_execution_time
    def add_light(self, light: Light):
        """
        Add a light source to the light manager.
        Args:
            light (Light): The light source to be added.
        """
        self.lights.append(light)

    def get_all_lights(self):
        """
        Get all light sources in the light manager.
        Returns:
            list: List of light sources.
        """
        return self.lights

    def display_lights(self):
        """
        Display the details of all light sources in the light manager.
        """
        for light in self.lights:
            print(light)

    def __str__(self):
        """
        Return a string representation of the LightManager object.
        """
        return f"LightManager: lights={len(self.lights)}"

    def __len__(self):
        """
        Return the number of light sources in the light manager.
        """
        return len(self.lights)

    def __getitem__(self, index):
        """
        Return the light source at the given index in the light manager.
        Args:
            index (int): The index of the light source.
        Returns:
            Light: The light source at the index.
        """
        return list.__getitem__(self.lights, index)

    def __iter__(self):
        """
        Return an iterator over the light sources in the light manager.
        Returns:
            iterator: An iterator object.
        """
        return list.__iter__(self.lights)

    @convert_output_to_tuple
    def get_results(self):
        """
        Get a list of results of calling do_something() on each light source in the light manager.
        Returns:
            list: A list of results.
        """
        return [light.do_something() for light in self.lights]

    def get_numbers(self):
        """
        Get a list of tuples of (object, ordinal number) for each light source in the light manager.
        Returns:
            list: A list of tuples.
        """
        return [(light, index + 1) for index, light in enumerate(self.lights)]

    def get_pairs(self):
        """
        Get a list of tuples of (object, result) for each light source in the light manager.
        Returns:
            list: A list of tuples.
        """
        return list(zip(self.lights, self.get_results()))

    def get_attributes(self, data_type):
        """
        Get a dictionary with all keys and values of attributes of an object that match a given data type.
        Args:
            data_type (type): The data type to filter by.
        Returns:
            dict: A dictionary with matching attributes.
        """
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    def check_condition(self):
        """
        Check if all objects or any object from the manager's list satisfy the condition is_on().
        Returns:
            dict: A dictionary with keys "all" and "any" and boolean values.
       """
        return {"all": all(light.is_on() for light in self.lights), "any": any(light.is_on() for light in self.lights)}
