from flask import Flask, render_template
import requests
from config import API_KEY

app = Flask(__name__)

# Route to display a list of cake recipes
@app.route('/')
def index():
    # Fetch cake recipes using the Spoonacular API
    cake_recipes = get_cake_recipes(API_KEY)

    if cake_recipes:
        # Render the 'index.html' template with the fetched recipes
        return render_template('index.html', recipes=cake_recipes)
    else:
        # Display an error message if fetching recipes fails
        return "Error fetching recipes."


# Route to display the ingredients of a specific recipe
@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    # Fetch recipe ingredients using the Spoonacular API for a specific recipe ID
    recipe_ingredients = get_recipe_ingredients(API_KEY, recipe_id)

    if recipe_ingredients:
        # Render the 'recipe.html' template with the fetched ingredients
        return render_template('recipe.html', ingredients=recipe_ingredients)
    else:
        # Display an error message if fetching recipe ingredients fails
        return "Error fetching recipe ingredients."




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
        
        # Extract the list of recipes from the response, default to an empty list if not present
        recipes = recipes_data.get('results', [])

        # Fetch image URLs for each recipe
        for recipe in recipes:
            image_url = get_recipe_image(api_key, recipe['id'])
            recipe['image'] = image_url

        return recipes
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


def get_recipe_image(api_key, recipe_id):
    """
    Fetch the image URL for a specific recipe from the Spoonacular API.

    Parameters:
    - api_key (str): The Spoonacular API key.
    - recipe_id (int): The ID of the recipe for which to fetch the image.

    Returns:
    - str or None: The image URL of the recipe, or None if the request fails.
    """
    base_url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {
        'apiKey': api_key,
    }

    # Make a GET request to the Spoonacular API
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        recipe_data = response.json()
        
        # Extract the image URL from the response, default to an empty string if not present
        image_url = recipe_data.get('image', '')
        return image_url
    else:
        # Print an error message if the request was not successful
        print(f"Error {response.status_code}: Unable to fetch recipe image.")
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


# Run the Flask app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)