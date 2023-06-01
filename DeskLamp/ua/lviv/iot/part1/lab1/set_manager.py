# pylint: disable = unused-variable
"""
Class representing a SetManager.
"""


class SetManager:
    """
    Attributes:
        regular_manager (LightManager): The regular manager object.
        color_set (set): The set of colors common to all light objects.
        current_obj (int): Index of the current object in LightManager.
        current_set (iterator): Iterator for the set of the current object.
    """

    def __init__(self, regular_manager):
        """
        Initialize a SetManager object.

        Args:
            regular_manager (LightManager): The regular manager object.
            color_set (set): The set of colors common to all light objects.
        """
        self.regular_manager = regular_manager

    def __iter__(self):
        """
        Return an iterator over the elements in the set of each object in the LightManager.
        """
        new_set = set()
        for lights in self.regular_manager.__iter__():
            new_set.update(lights.colors_set)
        return iter(new_set)

    def __next__(self):
        """
        Return the next element in the SetManager iterator.
        Raises:
            StopIteration: If there are no more elements to iterate over.
        """
        for lights in self.regular_manager.__iter__():
            return next(lights)

    def __len__(self):
        """
        Return the length of the SetManager iterator,
        which is the product of the lengths of sets in the LightManager.
        """
        length = 0
        for lights in self.regular_manager.__iter__():
            length += len(lights.colors_set)
        return length

    def __getitem__(self, index):
        """
        Return the element at the given index in the SetManager iterator.

        Args:
            index (int): The index of the element.

        Returns:
            Any: The element at the index.

        Raises:
            IndexError: If the index is out of range.
        """
        for lights in self.regular_manager.__iter__():
            return lights[index]
