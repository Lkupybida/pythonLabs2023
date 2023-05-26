import time


def measure_execution_time(method):
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = method(self, *args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Method '{method.__name__}' execution time: {execution_time} seconds")
        return result

    return wrapper


def convert_output_to_tuple(method):
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if isinstance(result, list):
            return tuple(result)
        return result

    return wrapper
