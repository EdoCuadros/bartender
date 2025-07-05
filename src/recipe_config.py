"""
Python program to configure the recipes and component ports.

DRINKS: Dictionary that states the cocktail components and the time the pump of each component
        is active.

PUMPS: Dictionary that states the port number of each pump.
"""
import json
import os

from interface import CoctelEnum, DataCoctel

RECIPE_FILE = os.path.join(os.path.dirname(__file__), '..', 'recipes.json')

with open(RECIPE_FILE, 'r') as f:
    DRINKS: dict[CoctelEnum, DataCoctel] = DataCoctel(json.load(f))

STATUS_FILE = os.path.join(os.path.dirname(__file__), '..', 'states.json')

with open(STATUS_FILE, 'r') as f:
    INGREDIENT_STATUS = json.load(f)
