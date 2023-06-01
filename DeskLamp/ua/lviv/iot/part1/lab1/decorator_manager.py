"""
Module: My Decorators

This module provides two decorators for measuring execution time and converting output to tuples.
"""
import time


def measure_execution_time(method):
    """
    Decorator function to measure the execution time of a method.

    Args:
        method (function): The method to be measured.

    Returns:
        function: The wrapped method.

    """

    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that measures the execution time of the method.

        Args:
            self (object): The object instance.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            object: The result of the method.

        """

        start_time = time.time()
        result = method(self, *args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Method '{method.__name__}' execution time: {execution_time} seconds")
        return result

    return wrapper


def convert_output_to_tuple(method):
    """
    Decorator function to convert the output of a method to a tuple if it is a list.

    Args:
        method (function): The method to be decorated.

    Returns:
        function: The wrapped method.

    """

    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that converts the output to a tuple if it is a list.

        Args:
            self (object): The object instance.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            object: The result of the method.

        """

        result = method(self, *args, **kwargs)
        if isinstance(result, list):
            return tuple(result)
        return result

    return wrapper
