""" This file is responsible for the creation and display of the graph of the cities in the given province with
respect to the given factor"""
import matplotlib.pyplot as plt
import numpy as np
import python_ta


def graphing(cities: dict[str: float | None], factor: str, province: str) -> None:
    """Accepts a dictionary containing the city names as the keys and the factor index as the values. The function also
    accepts the factor that is being compared and the province whose cities are being compared.
    It creates a bar graph that compares each city in the given dictionary.
    """
    names = []
    values = []
    for city in cities:
        if cities[city] is None:
            continue
        names.append(city)
        values.append(cities[city])

    if names == []:
        print("No data available for the cities. Graph not generated")
    else:
        x = np.arange(len(names))
        width = 0.5

        # plot data in grouped manner of bar type
        plt.rcParams["figure.autolayout"] = True
        plt.bar(x, values, width, color='green')
        plt.xticks(x, names, rotation=90)
        plt.xlabel("Cities in " + province)
        plt.ylabel("Cost of " + factor + " factor in city (in CAD) ")
        plt.title(factor + " factor in cities in " + province)
        plt.show()


if __name__ == '__main__':
    python_ta.check_all(config={
        'max-line-length': 120,
        'max-nested-blocks': 4,
        'extra-imports': ['matplotlib.pyplot', 'numpy'],
        'allowed-io': ['graphing']
    })
