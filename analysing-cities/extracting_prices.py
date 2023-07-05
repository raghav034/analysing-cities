"""This file is used to extract cities from the selected url"""
from typing import Optional
import python_ta
from bs4 import BeautifulSoup
import requests
import read_data_with_dict

# dictionary with relevant factors and their row numbers/indices
DATAPOINT_INDICES = {'Meal, Inexpensive Restaurant': 0, 'Meal for 2 People, Mid-range Restaurant, Three-course': 1,
                     'McMeal at McDonalds (or Equivalent Combo Meal)': 2, 'Milk (regular), (1 liter)': 8,
                     'Loaf of Fresh White Bread (500g)': 9, 'Eggs (regular) (12)': 11, 'Water (1.5 liter bottle)': 22,
                     'Gasoline (1 liter)': 32, 'Taxi 1km (Normal Tariff)': 30, 'One-way Ticket (Local Transport)': 27,
                     'Apartment (1 bedroom) in City Centre': 47,
                     'Price per Square Meter to Buy Apartment in City Centre': 51,
                     'Basic (Electricity, Heating, Cooling, Water, Garbage) for 85m2 Apartment': 35,
                     'Cinema, International Release, 1 Seat': 40, 'Fitness Club, Monthly Fee for 1 Adult': 38,
                     '1 Pair of Jeans (Levis 501 or Similar)': 43}

CITIES_AND_PROVINCES = read_data_with_dict.match_city_province(read_data_with_dict.get_list_cities())


def extract_prices(url: str) -> Optional[dict]:
    """A function that takes a url from numbeo and returns a dictionary with the keys as factors and values as prices.
    """

    # extracting data from the website for one given cite about cost of living factors
    source = requests.get(url).text

    soup = BeautifulSoup(source, 'lxml')

    table = soup.find('table', class_='data_wide_table new_bar_table')

    # extracting price information
    if table is not None:

        prices = table.find_all('span', class_='first_currency')
        new_prices = []

        # making price information readable
        for price in prices:
            new_price = price.text[:len(price) - 4]
            if ',' in new_price:
                new_price = new_price.replace(',', '')
            new_prices.append(new_price)

        # creating a dictionary to showcase data
        final_data = {}

        for factor in DATAPOINT_INDICES:
            if new_prices[DATAPOINT_INDICES[factor]] == '':
                final_data[factor] = None
            else:
                final_data[factor] = float(new_prices[DATAPOINT_INDICES[factor]])

        return final_data
    else:
        return None


def extract_all_prices() -> dict[tuple, dict]:
    """Function that will extract price information for all cities and return a dictionary where the key is a tuple
    with the city name and province and the value being a dictionary with the factor and corresponding price"""

    dict_urls = read_data_with_dict.open_url(read_data_with_dict.get_list_cities())

    data = {}

    for city in dict_urls:
        prices = extract_prices(dict_urls[city])
        # to remove cities with no price data
        if prices is not None and city[0] in CITIES_AND_PROVINCES:
            new_city = (city[0], CITIES_AND_PROVINCES[city[0]])
            data[new_city] = prices

    return data


if __name__ == '__main__':
    python_ta.check_all(config={
        'max-line-length': 120,
        'max-nested-blocks': 4,
        'extra-imports': ['requests', 'bs4', 'read_data_with_dict'],
    })
