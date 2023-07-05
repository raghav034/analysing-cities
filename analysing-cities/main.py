""" This file is responsible for managing the project and calling all the files to accept user input, extract and
process the data, create and display the heatmap for the given factor, and create and display the graph for the
cities in the given province with respect to the given factor"""
import doctest
import map_creation
import userinput
import graph
import classes


def runner() -> None:
    """The main runner function. Is responsible for calling all files and their functions
    to accept the user input, compute the data and create
    and display the heatmap and graph.
    """

    # Accepting the factor to be compared and the province for the graph.
    # Filtering the input.
    factor = userinput.get_factor(wrong_factor=False)
    province = userinput.get_province(wrong_province=False)

    tree = classes.load_full_tree(factor, classes.DATA)

    # Get province indexes from tree

    # dictionary that contains province and index
    province_indices = tree.get_province_indices()

    # Get cities in the province which stores city name and index

    # dictionary that contains city names and values for factor in provinces
    cities = tree.get_city_index(province)

    # Creation of Map of provinces

    map_creation.map_creation(province_indices, factor)

    # Get data for cities in province
    graph.graphing(cities, factor, province)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runner()
    import python_ta
    doctest.testmod()
    python_ta.check_all(config={
        'max-line-length': 120,
        'max-nested-blocks': 4,
        'extra-imports': ['map_creation', 'userinput', 'graph', 'classes'],
    })
