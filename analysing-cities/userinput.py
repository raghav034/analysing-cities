"""This file is responsible for accepting the factor to be compared between provinces and cities from the user and also
accept the province whose cities are to be compared"""
from tkinter import simpledialog

import python_ta


# from python_ta.contracts import check_contracts


# @check_contracts
def get_factor(wrong_factor: bool) -> str:
    """Creates a simple UI to accept the factor which will be compared between the province and the cities which will
    be illustrated in the heatmap and graph respectively. If the given input is not in the given list of factors,
    the function is run again with the wrong_factor bool set to true. A new UI is created which tells the user that
    the given province code must be in the given list with a new entry box to accept the input.
    """
    if wrong_factor is False:
        factor = simpledialog.askstring(title="Heatmap Data",
                                        prompt="Enter the factor you want to compare between the provinces"
                                               " (Food, Transportation, Housing or Leisure)")
        factor = factor.lower()

        if factor not in ['food', 'transportation', 'housing', 'leisure']:
            return get_factor(True)
    else:
        factor = simpledialog.askstring(title="Heatmap Data",
                                        prompt="Factor to be compared must be in the given list"
                                               " (Food, Transportation, Housing or Leisure)")
        factor = factor.lower()

        if factor not in ['food', 'transportation', 'housing', 'leisure']:
            return get_factor(True)

    return factor


# @check_contracts
def get_province(wrong_province: bool) -> str:
    """Creates a simple UI to accept the province whose cities will be compared in the graph
    If the given input is not a province code in Canada, the function is run again with the wrong_province bool set to
    true. A new UI is created which tells the user that the given province code must be in the given list with a new
    entry box to accept the input.
    """
    if wrong_province is False:
        province = simpledialog.askstring(title="Graph Data",
                                          prompt="Enter the province code of the cities you want to compare (AB, YT, "
                                                 "MB, SK, NT, PE, NS, ON, QC, NU, BC, NL, NB)")
        province = province.upper()

        if province not in ['AB', 'YT', 'MB', 'SK', 'NT', 'PE', 'NS', 'ON', 'QC', 'NU', 'BC', 'NL', 'NB']:
            return get_province(True)
    else:
        province = simpledialog.askstring(title="Graph Data",
                                          prompt="Province code must be in the given list (AB, YT, MB, SK, "
                                                 "NT, PE, NS, ON, QC, NU, BC, NL, NB)")

        province = province.upper()

        if province not in ['AB', 'YT', 'MB', 'SK', 'NT', 'PE', 'NS', 'ON', 'QC', 'NU', 'BC', 'NL', 'NB']:
            return get_province(True)

    return province


if __name__ == '__main__':
    python_ta.check_all(config={
        'max-line-length': 120,
        'max-nested-blocks': 4,
        'extra-imports': ['tkinter'],
    })
