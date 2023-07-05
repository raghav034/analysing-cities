"""File that helps us read data from the Numbeo website"""

import csv
import requests
from bs4 import BeautifulSoup
import python_ta


def get_list_cities() -> dict:
    """Return a dictionary with all the cities on Numbeo as a key and the corresponding province as a value,
        if it is provided. Make the value an empty string if no province information is provided"""
    r = requests.get('https://www.numbeo.com/cost-of-living/country_result.jsp?country=Canada')
    # print(r.text)
    soup = BeautifulSoup(r.content, 'html.parser')
    list_cities_unfiltered = soup.find_all('option')
    list_cities = {}  # City Name: Key, Province Name Value (empty string if no province)
    for i in range(1, len(list_cities_unfiltered)):
        city_unfiltered = list_cities_unfiltered[i]
        city_with_province = city_unfiltered.text
        if ',' in city_with_province:
            lst = city_with_province.split(',')
            list_cities[lst[0]] = lst[1]
        else:
            list_cities[city_with_province] = ''
    return list_cities


def open_url(city_names: dict) -> dict:
    """Return a dict with city and valid URLs on Numbeo as key-value pairs"""
    url_dict = {}
    for city in city_names:
        city_url = get_url_format(city)
        if city_names[city] == '':
            url = 'https://www.numbeo.com/cost-of-living/in/' + city_url
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            if 'Cannot find city id' in soup.title.text:
                url = 'https://www.numbeo.com/cost-of-living/in/' + city_url + '-' + 'Canada'
            url_dict[(city, '')] = url
        else:
            url = 'https://www.numbeo.com/cost-of-living/in/' + city_url
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            if 'Cannot find city id' in soup.title.text:
                url = 'https://www.numbeo.com/cost-of-living/in/' + city_url + '-' + 'Canada'
            if 'Cannot find city id' in soup.title.text:
                url = 'https://www.numbeo.com/cost-of-living/in/' + city_url + '-' + city_names[city].lstrip()
            if 'Cannot find city id' in soup.title.text:
                url = 'https://www.numbeo.com/cost-of-living/in/' + city_url + '-' + city_names[
                    city].lstrip() + '-' + 'Canada'
            url_dict[(city, city_names[city].lstrip())] = url
    return url_dict


def get_url_format(city: str) -> str:
    """Helper function that reformats the city name into a format that is used when opening URLs on Numbeo"""
    city_url = ''
    word = ''
    for letter in city:
        if letter.isalpha():
            word = word + letter
        else:
            if city_url == '':  # First word
                city_url += word
            else:
                city_url = city_url + '-' + word
            word = ''
    if city_url == '':  # Last Word
        city_url += word
    else:
        city_url = city_url + '-' + word
    return city_url


def match_city_province(cities: dict) -> dict:
    """
    Return a dictionary to match each city with the province it belongs to
    """
    return_dict = {}
    for city in cities:
        c = 0
        if cities[city] == '':
            with open('canadacities.csv') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    city_csv = row[1]
                    province_csv = row[2]
                    if city == city_csv:
                        return_dict[city] = province_csv
                        c = 1
                        break
            if c == 0:
                pass
        else:
            return_dict[city] = cities[city]
    return return_dict


if __name__ == '__main__':
    python_ta.check_all(config={
        'max-line-length': 120,
        'max-nested-blocks': 4,
        'extra-imports': ['requests', 'bs4', 'csv'],
        'allowed-io': ['match_city_province']
    })
