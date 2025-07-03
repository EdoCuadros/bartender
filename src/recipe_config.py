"""
Python program to configure the recipes and component ports.

DRINKS: Dictionary that states the cocktail components and the time the pump of each component
        is active.

PUMPS: Dictionary that states the port number of each pump.
"""
import json
import os

RECIPE_FILE = os.path.join(os.path.dirname(__file__), '..', 'recipes.json')

with open(RECIPE_FILE, 'r') as f:
    DRINKS = json.load(f)

