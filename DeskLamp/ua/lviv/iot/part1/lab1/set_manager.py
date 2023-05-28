class SetManager:
    def __init__(self, regular_manager, color_set):
        """
        Initialize a SetManager object.
        Args:
            regular_manager (LightManager): The regular manager object.
            color_set (set): The set of colors common to all light objects.
        """
        self.regular_manager = regular_manager
        self.color_set = color_set
        self.current_obj = 0  # Index of the current object in LightManager
        self.current_set = None  # Iterator for the set of the current object

    def __iter__(self):
        """
        Return an iterator over the elements in the set of each object in the LightManager.
        """
        self.current_obj = 0  # Reset the current object index
        return self

    def __next__(self):
        """
        Return the next element in the SetManager iterator.
        Raises:
            StopIteration: If there are no more elements to iterate over.
        """
        if self.current_set is None or self.current_obj >= len(self.regular_manager):
            raise StopIteration  # No more elements to iterate over

        if self.current_set is None:
            # First time iterating over the current object's set
            self.current_set = iter(self.regular_manager[self.current_obj])

        try:
            return next(self.current_set)
        except StopIteration:
            # Move to the next object in LightManager
            self.current_obj += 1
            if self.current_obj < len(self.regular_manager):
                self.current_set = iter(self.regular_manager[self.current_obj])
                return next(self.current_set)
            else:
                raise StopIteration

    def __len__(self):
        """
        Return the length of the SetManager iterator, which is the product of the lengths of sets in the LightManager.
        """
        length = 0
        for obj in self.regular_manager:
            length += len(obj)
        return length

    def __getitem__(self, index):
        """
        Return the element at the given index in the SetManager iterator.
        Args:
            index (int): The index of the element.
        Returns:
            Any: The element at the index.
        """
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")

        for obj in self.regular_manager:
            set_length = len(obj)
            if index < set_length:
                return obj[index]
            index -= set_length
