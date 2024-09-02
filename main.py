"""LU02.A08"""
import json

from typing import Dict, Any


def load_recipe(json_string: str) -> Dict[str, Any]:
    """
    Wandelt einen JSON-String in ein Python-Dictionary um.

    :param json_string: Der JSON-kodierte String des Rezepts.
    :return: Ein Dictionary, das das Rezept repräsentiert.
    """
    return json.loads(json_string)


def adjust_recipe(recipe: Dict[str, Any], new_servings: int) -> Dict[str, Any]:
    """
    Passt das Rezept für eine neue Anzahl von Personen an.

    :param recipe: Ein Dictionary, das das ursprüngliche Rezept enthält.
    :param new_servings: Die neue Anzahl an Portionen.
    :return: Ein Dictionary, das das angepasste Rezept enthält.
    """
    original_servings = recipe['servings']
    ingredient_multiplier = new_servings / original_servings

    new_ingredients = {
        ingredient: round(amount * ingredient_multiplier)
        for ingredient, amount in recipe['ingredients'].items()
    }

    return {
        'title': recipe['title'],
        'ingredients': new_ingredients,
        'servings': new_servings
    }


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'

    # Rezept laden
    recipe = load_recipe(recipe_json)

    # Neue Anzahl an Personen
    new_servings = 2

    # Rezept anpassen
    adjusted_recipe = adjust_recipe(recipe, new_servings)

    # Angepasstes Rezept als JSON-String ausgeben
    adjusted_recipe_json = json.dumps(adjusted_recipe, indent=4)
    print(adjusted_recipe_json)
