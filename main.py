"""Lu02.A08"""
import json
from typing import Dict, Any


def load_recipe(json_string: str) -> Dict[str, Any]:
    """
    Wandelt einen JSON-String in ein Python-Dictionary um.

    :param json_string: Der JSON-kodierte String des Rezepts.
    :return: Ein Dictionary, das das Rezept repräsentiert.
    """
    return json.loads(json_string)


def adjust_recipe(original_recipe: Dict[str, Any], new_servings: int) -> Dict[str, Any]:
    """
    Passt das Rezept für eine neue Anzahl von Personen an.

    :param original_recipe: Ein Dictionary, das das ursprüngliche Rezept enthält.
    :param new_servings: Die neue Anzahl an Portionen.
    :return: Ein Dictionary, das das angepasste Rezept enthält.
    """
    original_servings = original_recipe['servings']
    ingredient_multiplier = new_servings / original_servings

    adjusted_ingredients = {
        ingredient: round(amount * ingredient_multiplier)
        for ingredient, amount in original_recipe['ingredients'].items()
    }

    return {
        'title': original_recipe['title'],
        'ingredients': adjusted_ingredients,
        'servings': new_servings
    }


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json_string = (
        '{"title": "Spaghetti Bolognese", '
        '"ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, '
        '"servings": 4}'
    )

    # Rezept laden
    loaded_recipe = load_recipe(recipe_json_string)

    # Neue Anzahl an Personen
    new_serving_count = 2

    # Rezept anpassen
    adjusted_recipe = adjust_recipe(loaded_recipe, new_serving_count)

    # Angepasstes Rezept als JSON-String ausgeben
    adjusted_recipe_json = json.dumps(adjusted_recipe, indent=4)
    print(adjusted_recipe_json)
