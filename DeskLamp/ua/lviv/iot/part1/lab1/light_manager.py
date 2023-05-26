"""
light_manager.py
"""

from light import Light


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
