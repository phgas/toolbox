import random
import json
import time


def measure_exec_time(func):
    """
    A decorator to measure the execution time of a function.

    Parameters:
        func (Callable): The function whose execution time is to be measured.

    Returns:
        Callable: The wrapped function that includes time measurement.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f}s to run.")
        return result
    return wrapper


def get_random_phone(country: str, prefix: bool = False) -> str:
    """
    Generates a random phone number for the specified country.

    Parameters:
        country (str): The country for which the phone number is to be generated. 
        prefix (bool, optional): Flag to include the country's prefix. Defaults to True.

    Returns:
        str: The randomly generated phone number.
    """
    with open('phone_providers.json', 'r') as file:
        content = json.load(file)[country]

    country_prefix = content['country_prefix']
    provider_prefix = random.choice(content['provider_prefix'])
    random_digits = ''.join(random.sample("0123456789", 7))

    if prefix == True:
        random_phone = f"{country_prefix}{provider_prefix[1:]}{random_digits}"
    else:
        random_phone = f"{provider_prefix}{random_digits}"

    return random_phone


if __name__ == "__main__":
    # Demonstrating the usage of @measure_exec_time decorator.
    @measure_exec_time
    def test():
        for i in range(0, 10000000):
            continue
    test()

    # Demonstrating the usage of get_random_phone function.
    random_phone = get_random_phone(country="AT")
    print(random_phone)
