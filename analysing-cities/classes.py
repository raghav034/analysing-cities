"""This document contains the list of classes that we will be using in our project. It includes an abstract node
and tree, and it also includes the classes specific to each data type
"""
from __future__ import annotations
from typing import Optional

import python_ta
# from python_ta.contracts import check_contracts
from price_data import DATA

CITIES = {'Kenora', 'Vancouver', 'Joliette', 'Spruce Grove', 'Armstrong', 'Smithers', 'Toronto', 'Brandon',
          'Medicine Hat', 'Airdrie', 'Terrace', 'Rouyn-Noranda', 'Windsor', 'Montmagny', 'Maple Ridge', 'Belleville',
          'Saanich', 'Calgary', 'Halifax', 'Langley', 'Moncton', 'Peterborough', 'Brampton', 'Orillia', 'Cornwall',
          'Gander', 'High Level', 'La Ronge', 'Wolfville', 'Hinton', 'Parksville', 'Chilliwack', 'Flin Flon',
          'Victoriaville', 'Campbell River', 'Annapolis Valley', 'Trois-Rivieres', 'Sundre', 'Banff', 'Iqaluit',
          'Bathurst', 'Cranbrook', 'Hearst', 'Courtenay', 'Sept-Iles', 'Longueuil', 'Vernon', 'Selkirk', 'Cochrane',
          'Winnipeg', 'Edmonton', 'Burlington', 'Kitchener', 'Fort Frances', 'Marmora', 'Bridgewater', 'Castlegar',
          'Red Deer', 'Fredericton', 'Yorkton', 'Victoria', 'Cobourg', 'Timmins', 'Fort Saskatchewan', 'Thunder Bay',
          'Baie-Comeau', 'Sechelt', 'Nanaimo', 'Kamloops', 'Cold Lake', 'North Bay', 'Prince George', 'Sarnia',
          'Innisfil', 'Slave Lake', 'Whistler', 'Squamish', 'Salaberry-de-Valleyfield', 'Grimsby', 'Oakville',
          'Whitecourt', 'Saint John', 'Sydney', 'Lethbridge', 'New Westminster', 'Gibsons', 'Inuvik', 'Quesnel',
          'Hay River', 'Williams Lake', 'North Vancouver', 'Golden', 'Milton', 'Bowen Island', 'Fort St John',
          'Saguenay', 'Parry Sound', 'Stratford', 'Port Alberni', 'Coquitlam', 'Jasper', 'Cambridge', 'Okotoks',
          'Welland', 'Brossard', 'Summerside', 'Granby', 'Peace River', 'Oshawa', 'Pincher Creek', 'Niagara Falls',
          'Châteauguay', 'Sudbury', 'Morden', 'Mississauga', 'Port Hawkesbury', 'Whitby', 'Corner Brook',
          'Drummondville', 'Waterloo', 'Laval', 'Dawson Creek', 'Ottawa', 'Fort Erie', 'Comox', 'Aurora', 'La Dore',
          'Newmarket', 'Owen Sound', 'Yellowknife', 'Amherst', 'Ajax', 'Hamilton', 'Guelph', 'Kelowna',
          'Richmond Hill', 'Stephenville', 'Surrey', 'Richmond', 'Saskatoon', 'Campbellton', 'Kirkland Lake', 'Creston',
          'Port Coquitlam', 'Digby', 'Simcoe', 'Vaughan', 'Summerland', 'Abbotsford', 'Charlottetown',
          'Edmundston', 'Ladner', 'Truro', 'Fort Nelson', 'Nakusp', 'Prince Albert', 'Brantford', 'Mackenzie',
          'Bowmanville', 'Camrose', 'Regina', 'Leamington', 'Salmon Arm', 'Quebec City', 'Canmore', 'Montreal',
          'Powell River', 'Mascouche', 'Whitehorse', 'Elliot Lake', 'Gatineau', 'Grande Prairie', 'Labrador City',
          'Gravelbourg', 'Lloydminster', 'Burnaby', 'Markham', 'Swift Current', 'Sherbrooke', 'Pickering', 'Thompson',
          'London', 'Barrie', 'Estevan', 'Penticton', 'Sainte-Adele', 'Woodstock', 'Orangeville', 'Kingston',
          'Prince Rupert', 'Delta', 'Antigonish'}

PROVINCES = {'PE', 'QC', 'NT', 'SK', 'AB', 'MB', 'YT', 'NL', 'NU', 'ON', 'NS', 'NB', 'BC'}


# @check_contracts
class AbstractNode:
    """This is an abstract version of a node within our tree containing the data for a given factor. It will be
    customised for a given node for each factor we are considering

    Instance Attributes:
        - region_name: this is the name of the region this node is referring to. It can be a city,
        country, or province in Canada.
        - region_type: this is whether it is a city, or province, or country
        - data: a dictionary containing the name of a sub-factor for a factor and its respective aggregate value
        - city_index: a value containing the average price for that city for a given facto

    Representation Invariants:
        - self.region_type in {'city', 'province', 'country'}
        - not self.region_type == 'city' or self.region_name in CITIES
        - not self.region_type == 'province' or self.region_name in PROVINCES
        - not self.region_type == 'country' or self.region_name == 'Canada'
        - city_index is None or self.region_type == 'city'
    """

    region_name: str
    region_type: str
    data: dict[str, Optional[float]]
    city_index: Optional[float]

    def __init__(self, region_name: str, region_type: str) -> None:
        """Initialising an instance of a node for our trees containing the data
        """

        self.region_name = region_name
        self.region_type = region_type
        self.data = {}
        self.city_index = None

    def add_city_data(self) -> None:
        """Add values to the data instance for each node. This function will change based on the factor we are observing
        """
        raise NotImplementedError

    def calculate_city_index(self) -> None:
        """Calculate the index for a city's quality for a given factor.
        """
        raise NotImplementedError


# @check_contracts
class FoodNode(AbstractNode):
    """A node containing food data for a food tree"""

    def __init__(self, region_name: str, region_type: str) -> None:
        """Initialiser for a food node.
        """
        super().__init__(region_name, region_type)

    def add_city_data(self) -> None:
        """Create a dictionary of the relevant food data for a given city

        Preconditions:
            - self.region_type = 'city'
            - self.region_name in CITIES
        """

        prices = {}
        for key in DATA:
            city = key[0]
            if city == self.region_name:
                prices = DATA[key]

        # calculate restaurant data
        one_meal = prices['Meal, Inexpensive Restaurant']
        two_meal = prices['Meal for 2 People, Mid-range Restaurant, Three-course']
        mcmeal = prices['McMeal at McDonalds (or Equivalent Combo Meal)']

        if one_meal is not None and two_meal is not None and mcmeal is not None:
            sum_meal_price = prices['Meal, Inexpensive Restaurant'] + \
                prices['Meal for 2 People, Mid-range Restaurant, Three-course'] + \
                prices['McMeal at McDonalds (or Equivalent Combo Meal)']
            average_meal_price = sum_meal_price / 3
            self.data['Restaurants'] = average_meal_price
        elif one_meal and two_meal:
            sum_prices = one_meal + two_meal
            average_price = sum_prices / 2
            self.data['Restaurants'] = average_price
        elif one_meal and mcmeal:
            sum_prices = one_meal + mcmeal
            average_price = sum_prices / 2
            self.data['Restaurants'] = average_price
        elif two_meal and mcmeal:
            sum_prices = two_meal + mcmeal
            average_price = sum_prices / 2
            self.data['Restaurants'] = average_price
        else:
            self.data['Restaurants'] = None

        # calculate supermarket data
        milk = prices['Milk (regular), (1 liter)']
        bread = prices['Loaf of Fresh White Bread (500g)']

        if milk is not None and bread is not None and prices['Eggs (regular) (12)'] is not None and \
                prices['Water (1.5 liter bottle)'] is not None:
            sum_market_price = prices['Milk (regular), (1 liter)'] + prices['Loaf of Fresh White Bread (500g)'] + \
                prices['Eggs (regular) (12)'] + prices['Water (1.5 liter bottle)']
            average_market_price = sum_market_price / 4
            self.data['Markets'] = average_market_price
        elif milk and bread and prices['Eggs (regular) (12)']:
            sum_prices = milk + bread + prices['Eggs (regular) (12)']
            average_price = sum_prices / 3
            self.data['Markets'] = average_price
        elif bread and prices['Eggs (regular) (12)'] and prices['Water (1.5 liter bottle)']:
            sum_prices = bread + prices['Eggs (regular) (12)'] + prices['Water (1.5 liter bottle)']
            average_price = sum_prices / 3
            self.data['Markets'] = average_price
        elif milk and bread and prices['Water (1.5 liter bottle)']:
            sum_prices = milk + bread + prices['Water (1.5 liter bottle)']
            average_price = sum_prices / 3
            self.data['Markets'] = average_price
        elif milk and prices['Eggs (regular) (12)'] and prices['Water (1.5 liter bottle)']:
            sum_prices = milk + prices['Eggs (regular) (12)'] + prices['Water (1.5 liter bottle)']
            average_price = sum_prices / 3
            self.data['Markets'] = average_price
        else:
            self.data['Markets'] = None

    def calculate_city_index(self) -> None:
        """Calculate an index for a food node showing the quality of the city with respect to food

        Preconditions:
            - self.region_name in CITIES
            - self.region_type == 'city'
            - self.data != {}
        """

        restaurants = self.data['Restaurants']
        markets = self.data['Markets']

        if restaurants is not None and markets is not None:
            sum_prices = self.data['Restaurants'] + self.data['Markets']
            average_price = sum_prices / 2
            self.city_index = average_price
        elif restaurants is not None and markets is None:
            average_price = restaurants
            self.city_index = average_price
        elif restaurants is None and markets is not None:
            average_price = markets
            self.city_index = average_price


# @check_contracts
class TransportationNode(AbstractNode):
    """A node containing transportation data for a transportation tree"""

    def __init__(self, region_name: str, region_type: str) -> None:
        """Initialiser for a Transportation Node"""
        super().__init__(region_name, region_type)

    def add_city_data(self) -> None:
        """Create a dictionary of the relevant food data for a given city

        Preconditions:
            - self.region_type = 'city'
            - self.region_name in CITIES
        """

        prices = {}
        for key in DATA:
            city = key[0]
            if city == self.region_name:
                prices = DATA[key]

        # adding gasoline data
        self.data['Gasoline'] = prices['Gasoline (1 liter)']

        # adding taxi fare data
        self.data['Taxi Price per Km for 1 Km'] = prices['Taxi 1km (Normal Tariff)']

        # adding public transportation data
        self.data['One-way Ticket (Local Transport)'] = prices['One-way Ticket (Local Transport)']

    def calculate_city_index(self) -> None:
        """Calculate an index for a transportation node showing the quality of the city with respect to transportation

        Preconditions:
            - self.region_name in CITIES
            - self.region_type == 'city'
            - self.data != {}
        """

        gasoline = self.data['Gasoline']
        taxi = self.data['Taxi Price per Km for 1 Km']
        local_transport = self.data['One-way Ticket (Local Transport)']

        if gasoline is not None and taxi is not None and local_transport is not None:
            sum_prices = self.data['Gasoline'] + self.data['Taxi Price per Km for 1 Km'] + \
                self.data['One-way Ticket (Local Transport)']
            average_price = sum_prices / 3
            self.city_index = average_price
        elif gasoline and taxi:
            sum_prices = gasoline + taxi
            average_price = sum_prices / 2
            self.city_index = average_price
        elif taxi and local_transport:
            sum_prices = taxi + local_transport
            average_price = sum_prices / 2
            self.city_index = average_price
        elif gasoline and local_transport:
            sum_prices = gasoline + local_transport
            average_price = sum_prices / 2
            self.city_index = average_price


# @check_contracts
class HousingNode(AbstractNode):
    """A node containing housing data for a housing tree"""

    def __init__(self, region_name: str, region_type: str) -> None:
        """Initialiser for a housing node.
        """
        super().__init__(region_name, region_type)

    def add_city_data(self) -> None:
        """Create a dictionary of the relevant housing data for a given city

        Preconditions:
            - self.region_type = 'city'
            - self.region_name in CITIES
        """

        prices = {}
        for key in DATA:
            city = key[0]
            if city == self.region_name:
                prices = DATA[key]

        # calculate housing data
        self.data['Basic Utilities'] = \
            prices['Basic (Electricity, Heating, Cooling, Water, Garbage) for 85m2 Apartment']
        self.data['Rent for 1 Bedroom'] = prices['Apartment (1 bedroom) in City Centre']
        self.data['Buying Price for 1 Bedroom Apartment'] = \
            prices['Price per Square Meter to Buy Apartment in City Centre']

    def calculate_city_index(self) -> None:
        """Calculate an index for a housing node showing the quality of the city with respect to housing.

        Preconditions:
            - self.region_name in CITIES
            - self.region_type == 'city'
            - self.data != {}
        """

        utilities = self.data['Basic Utilities']
        rent = self.data['Rent for 1 Bedroom']
        purchase = self.data['Buying Price for 1 Bedroom Apartment']

        if utilities is not None and rent is not None and purchase is not None:
            sum_prices = self.data['Basic Utilities'] + self.data['Rent for 1 Bedroom'] + \
                self.data['Buying Price for 1 Bedroom Apartment']
            average_price = sum_prices / 3
            self.city_index = average_price
        elif utilities and rent:
            sum_prices = utilities + rent
            average_price = sum_prices / 2
            self.city_index = average_price
        elif rent and purchase:
            sum_prices = rent + purchase
            average_price = sum_prices / 2
            self.city_index = average_price
        elif utilities and purchase:
            sum_prices = utilities + purchase
            average_price = sum_prices / 2
            self.city_index = average_price


# @check_contracts
class LeisureNode(AbstractNode):
    """A node containing leisure data for a leisure tree"""

    def __init__(self, region_name: str, region_type: str) -> None:
        """Initialiser for a leisure node.
        """
        super().__init__(region_name, region_type)

    def add_city_data(self) -> None:
        """Create a dictionary of the relevant leisure data for a given city

        Preconditions:
            - self.region_type = 'city'
            - self.region_name in CITIES
        """

        prices = {}
        for key in DATA:
            city = key[0]
            if city == self.region_name:
                prices = DATA[key]

        # calculate leisure data
        self.data['Fitness Club Fee'] = prices['Fitness Club, Monthly Fee for 1 Adult']
        self.data['Cinema'] = prices['Cinema, International Release, 1 Seat']
        self.data['Jean Prices'] = prices['1 Pair of Jeans (Levis 501 or Similar)']

    def calculate_city_index(self) -> None:
        """Calculate an index for a housing node showing the quality of the city with respect to housing.

        Preconditions:
            - self.region_name in CITIES
            - self.region_type == 'city'
            - self.data != {}
        """

        fitness = self.data['Fitness Club Fee']
        cinema = self.data['Cinema']
        jeans = self.data['Jean Prices']

        if fitness is not None and cinema is not None and jeans is not None:
            sum_prices = fitness + cinema + jeans
            average_price = sum_prices / 3
            self.city_index = average_price
        elif fitness and cinema:
            sum_prices = fitness + cinema
            average_price = sum_prices / 2
            self.city_index = average_price
        elif fitness and jeans:
            sum_prices = fitness + jeans
            average_price = sum_prices / 2
            self.city_index = average_price
        elif jeans and cinema:
            sum_prices = cinema + jeans
            average_price = sum_prices / 2
            self.city_index = average_price


# @check_contracts
class Tree:
    """This is a tree containing data for each factor for a given city. It will be
    customised based on the factor

    Instance Attributes:
        - root: this is the node of the current region, the type of which will change based on the factor
        - subtrees: this is a dictionary where the key is the name of the region within the current region and the
        value is another tree where the root node is a node for the region in the key
        - factor: a string stating what factor the tree is for
        - index: average index for a given factor for this whole region

    Representation Invariants:
        - self.factor in {'food', 'housing', 'transportation', 'leisure'}
        - all(key == self.subtrees[key].root.region_name for key in self.subtrees)
        - not self.root.region_type == 'city' or self.index == self.root.city_index
        - not self.factor == 'food' or isinstance(self.root, FoodNode)
        - not self.factor == 'housing' or isinstance(self.root, HousingNode)
        - not self.factor == 'transportation' or isinstance(self.root, TransportationNode)
        - not self.factor == 'leisure' or isinstance(self.root, LeisureNode)
    """

    root: AbstractNode
    subtrees: dict[str, Tree]
    factor: str
    index: Optional[float]

    def __init__(self, root: AbstractNode, factor: str) -> None:
        """Initialising a new AbstractTree
        """
        self.root = root
        self.subtrees = {}
        self.factor = factor
        self.index = None

    def load_subtree_from_data(self, data: dict[tuple, dict]) -> None:
        """Adds each province as a subtree and all the cities under that province as subtrees of the province
        using the data, which is a dictionary containing the city name and a province in a tuple as the key, with
        the corresponding value being another dictionary for which the key is a factor name and the value is the price.

        Preconditions:
            - all(key[1] in PROVINCES for key in data)
            - all(key[0] in CITIES for key in data)
        """

        for key in data:
            if key[1].lstrip() in self.subtrees:
                current_tree = self.subtrees[key[1].lstrip()]
                current_tree._add_subtree(key[0], 'city')
                self.update_index()
            elif key[1].lstrip() == 'New Brunswick' and 'NB' in self.subtrees:
                current_tree = self.subtrees['NB']
                current_tree._add_subtree(key[0], 'city')
                self.update_index()
            elif key[1].lstrip() == 'New Brunswick' and 'NB' not in self.subtrees:
                self._add_subtree('NB', 'province')
                current_tree = self.subtrees['NB']
                current_tree._add_subtree(key[0], 'city')
                self.update_index()
            elif key[1].lstrip() == 'Ontario' and 'ON' in self.subtrees:
                current_tree = self.subtrees['ON']
                current_tree._add_subtree(key[0], 'city')
                self.update_index()
            elif key[1].lstrip() == 'Ontario' and 'ON' not in self.subtrees:
                self._add_subtree('ON', 'province')
                current_tree = self.subtrees['ON']
                current_tree._add_subtree(key[0], 'city')
                self.update_index()
            elif key[1].lstrip() not in self.subtrees:
                self._add_subtree(key[1].lstrip(), 'province')
                current_tree = self.subtrees[key[1].lstrip()]
                current_tree._add_subtree(key[0], 'city')
                self.update_index()

    def _add_subtree(self, region_name: str, region_type: str) -> None:
        """This is a private function that will add a subtree to a function for a given region_name and region_type

        Preconditions:
            - not self.root.region_type == 'country' or region_type == 'province'
            - not self.root.region_type == 'province' or region_type == 'city'
            - not region_type == 'province' or region_name in PROVINCES
            - not region_type == 'city' or region_name in CITIES
        """

        new_node = creating_new_node(self.factor, region_name, region_type)
        new_tree = Tree(new_node, self.factor)
        self.subtrees[new_tree.root.region_name] = new_tree

    def update_index(self) -> None:
        """
        This is a function that will recursively update the index of the tree and all its subtrees and leafs,
        showcasing each region's quality with respect to a given factor.
        """

        if self.subtrees == {}:
            self.root.calculate_city_index()
            self.index = self.root.city_index
        else:
            sum_so_far = 0
            count_so_far = 0
            for subtree in self.subtrees:
                self.subtrees[subtree].update_index()
                if self.subtrees[subtree].index is not None:
                    sum_so_far += self.subtrees[subtree].index
                    count_so_far += 1

            if count_so_far != 0:
                average = sum_so_far / count_so_far
                self.index = average

    def get_province_indices(self) -> dict[str, float]:
        """
        Return a dictionary where the keys are each province and the values are the corresponding
        indices for the province in the given factor tree

        Preconditions:
            - self.root.region_type == 'country'
            - {subtree in PROVINCES for subtree in self.subtrees}
        """

        return_dict = {}
        for subtree in self.subtrees:
            return_dict[self.subtrees[subtree].root.region_name] = self.subtrees[subtree].index
        return return_dict

    def get_city_index(self, province: str) -> dict[str, float]:
        """
        Return a dictionary where the keys are each city inside a province provided by the user and the values
        are the corresponding indices for the city in the current factor tree

        Preconditions:
            - province in PROVINCES
            - self.root.region_type = 'country'
        """
        subtree = self.subtrees[province]
        return_dict = {}
        for subsubtree in subtree.subtrees:
            return_dict[subsubtree] = subtree.subtrees[subsubtree].index
        return return_dict

    def __str__(self) -> str:
        """Return a string representation of this tree.
        """
        return self._str_indented(0)

    def _str_indented(self, depth: int) -> str:
        """Return an indented string representation of this tree.

        The indentation level is specified by the <depth> parameter.

        Preconditions:
            - depth >= 0
        """
        move_desc = f'{self.root.region_name} -> {self.index}\n'
        str_so_far = '  ' * depth + move_desc
        for subtree in self.subtrees.values():
            str_so_far += subtree._str_indented(depth + 1)
        return str_so_far


# @check_contracts
def load_full_tree(factor: str, data: dict[tuple, dict[str, float]]) -> Tree:
    """
    This is a function that will load a full tree for a given factor based on the data in the form of a dictionary.
    It will then return this tree.

    Preconditions:
        - factor in {'food', 'transportation', 'leisure', 'housing}
        - all(key[1] in PROVINCES for key in data)
        - all(key[0] in CITIES for key in data)
    """
    root_node = creating_new_node(factor, 'Canada', 'country')
    new_tree = Tree(root_node, factor)
    new_tree.load_subtree_from_data(data)

    return new_tree


# @check_contracts
def creating_new_node(factor: str, region_name: str, region_type: str) -> AbstractNode:
    """
    This is a helper function that creates a new node based on the factor, the region name, and the region type.
    It returns this node.

    Preconditions:
        - factor in {'food', 'transportation', 'leisure', 'housing'}
        - not region_type == 'province' or region_name in PROVINCES
        - not region_type == 'city' or region_name in CITIES
        - not region_type == 'country' or region_name == 'Canada'
    """
    new_node = None
    if factor == 'food':
        new_node = FoodNode(region_name, region_type)
    elif factor == 'transportation':
        new_node = TransportationNode(region_name, region_type)
    elif factor == 'housing':
        new_node = HousingNode(region_name, region_type)
    elif factor == 'leisure':
        new_node = LeisureNode(region_name, region_type)

    if region_type == 'city':
        new_node.add_city_data()

    return new_node


if __name__ == '__main__':
    python_ta.check_all(config={
        'max-line-length': 120,
        'max-nested-blocks': 4,
        'extra-imports': ['price_data', 'userinput', 'graph', 'classes'],
        'disable': ['too-many-branches']
    })
