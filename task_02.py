#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" tool that takes shopping data and calculates"""

from data import FRUIT

def get_cost_per_item(shoplist):
    """calculator for each item

    Args:
        shoplist (dict) : item name and identification number

    Returns:
        cost of each item

    Examples:
    >>> print shoplist
    {'lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}
    >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet':
    {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
    112.800000000001
    """
    return {key: FRUIT[key] * shoplist[key] for key in shoplist.iterkeys()
            if key in FRUIT}

    """ calculator for the total cost

    Args:
        shoplist: item name and id

    Returns:
        total cost

    """
    Item_list = get_cost_per_item(shoplist)
    return sum([value for value in Item_list.itervalues()]) 
