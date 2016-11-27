#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" pet task"""

import pet

class Dog(pet.Pet):
    """ Subclass from pet"""

    def __init__(self, has_shots = False, args):

        """ dog class and pet subclass

        Args:
            has_shots, (boolean, optional) defaults to false
            dictionary(string): arbitrary

        Attributes: dict = args

    """
    self.has_shots = has_shots
    self.args = pet.Pet.__init__(self, **args)
    
