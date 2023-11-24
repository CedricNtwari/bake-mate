import requests
import pprint
from config import API_KEY


def get_cake_recipes(api_key, query='cake'):
    """
    Define the base URL for Spoonacular API

    Parameters:
    - api_key (str): The Spoonacular API key.
    - query (str): The query term for recipe search (default is 'cake').

    Returns:
    - list or None: A list of dictionaries representing the recipes, or None if the request fails.
    """
    base_url = 'https://api.spoonacular.com/recipes/search'
    # Set up parameters for the API request
    params = {
        'apiKey': api_key,
        'query': query,
        'type': 'cake',
        'number': 5  # number of recipes to retrieve
    }

    # Make a GET request to the Spoonacular API
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        recipes_data = response.json()
        # Return the 'results' part of the response, which contains recipe data
        return recipes_data['results']
    else:
        # Print an error message if the request was not successful
        print(f"Error {response.status_code}: Unable to fetch recipes.")
        return None


def get_recipe_ingredients(api_key, recipe_id):
    """
    Retrieve recipe ingredients for a given recipe ID from the Spoonacular API.

    Parameters:
    - api_key (str): The Spoonacular API key.
    - recipe_id (int): The ID of the recipe for which ingredients are to be retrieved.

    Returns:
    - list or None: A list of dictionaries representing the ingredients, or None if the request fails.
    """
    # The URL for fetching recipe ingredients using the Spoonacular API
    base_url = f'https://api.spoonacular.com/recipes/{recipe_id}/ingredientWidget.json'
    
    # Set up parameters for the API request
    params = {
        'apiKey': api_key,
    }

    # Make a GET request to the Spoonacular API
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        ingredients_data = response.json()
        # Return the 'ingredients' part of the response, which contains ingredient data
        return ingredients_data['ingredients']
    else:
        # Print an error message if the request was not successful
        print(f"Error {response.status_code}: Unable to fetch recipe ingredients.")
        return None


# Example usage
cake_recipes = get_cake_recipes(API_KEY)

if cake_recipes:
    for i, recipe in enumerate(cake_recipes, 1):
        print(f"\nRecipe {i}: {recipe['title']}")
        print(f"Ready in {recipe['readyInMinutes']} minutes")
        print(f"Servings: {recipe['servings']}")
        print(f"Link: {recipe['sourceUrl']}")

        # Get and print ingredients for each recipe
        recipe_ingredients = get_recipe_ingredients(API_KEY, recipe['id'])
        if recipe_ingredients:
            print("Ingredients:")
            for ingredient in recipe_ingredients:
                print(f"- {ingredient['name']} ({ingredient['amount']['us']['value']} {ingredient['amount']['us']['unit']})")
