"""This file is responsible for the creation and display of the heatmap for the given factor"""
from typing import Any

import geopandas as gpd
import matplotlib.pyplot as plt
import python_ta


# Creation of Map
def map_creation(indexes: dict, factor: str) -> Any:
    """Accepts a dictionary containing the province codes as keys and their factor indexes as the values. The values
    in the dictionary is appended to the geodataframe obtained from a geojson file which contains the data to create the
    map for all provinces in Canada which is then used to create the heatmap.
    """
    canada = gpd.GeoDataFrame.from_file("georef-canada-province@public.geojson")

    # Order: AB, YT, MB, SK, NT, PE, NS, ON, QC, NU, BC, NL, NB
    # Province Indexes are appended
    for index in indexes:
        if indexes[index] is None:
            indexes[index] = 0
    canada['indexes'] = [indexes['AB'], indexes['YT'], indexes['MB'], indexes['SK'], indexes['NT'], indexes['PE'],
                         indexes['NS'], indexes['ON'], indexes['QC'], indexes['NU'], indexes['BC'], indexes['NL'],
                         indexes['NB']]

    # # # # Complex mapping
    canada.plot(column='indexes', cmap='OrRd',
                legend=True, figsize=(10, 8))
    plt.title("Heatmap for " + factor + " cost (in CAD)")
    plt.show()

    return canada


if __name__ == '__main__':
    python_ta.check_all(config={
        'max-line-length': 120,
        'max-nested-blocks': 4,
        'extra-imports': ['geopandas', 'matplotlib.pyplot', 'graph', 'classes'],
    })
