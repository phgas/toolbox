import random
import json


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
    random_phone = get_random_phone(country="AT")
    print(random_phone)
