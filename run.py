from flask import Flask, render_template, request
from config import API_KEY
import requests

app = Flask(__name__, static_url_path='/static')

FOOD2FORK_API_URL = 'https://food2fork.ca/api/recipe/search/'


def search_cake_recipes(api_key, query='cake', page=1):
    """
    Search for cake recipes using the food2fork.ca API.

    Parameters:
    - api_key (str): The food2fork.ca API key.
    - query (str): The query term for recipe search (default is 'cake').
    - page (int): The page number for pagination (default is 1).

    Returns:
    - list or None: A list of dictionaries representing the recipes,
    or None if the request fails.
    """
    # Define parameters for the API request
    params = {
        'page': page,
        'query': query,
    }
    # Define headers for the API request
    headers = {
        'Authorization': f'Token {api_key}',
    }
    # Make a GET request to the Food2Fork API
    try:
        response = requests.get(
            FOOD2FORK_API_URL,  # API endpoint URL
            params=params,  # Pass the parameters
            headers=headers  # Pass the headers

        )

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON data from the response
            recipes_data = response.json()

            # Check if the API response contains an error
            if 'error' in recipes_data:
                error_message = recipes_data['error']
                print(f"Error in API response: {error_message}")
                return None

            # Extract the list of recipes from the response data
            recipes = recipes_data.get('results', [])
            return recipes
        else:
            # Print an error message if the API request was not successful
            print(
                f"Error {response.status_code}: "
                f"Unable to fetch recipes. {response.content}")
            return None

    # Handle exceptions
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


@app.route('/')
def index():
    """
    Route to display a list of cake recipes on the index page.
    Returns:
    - Renders the 'index.html' template
    with the fetched recipes, or displays an error message
    if fetching recipes fails.
    """
    # Call the function to search for cake recipes using the Food2Fork API
    cake_recipes = search_cake_recipes(API_KEY)
    # Set a default value for 'page' if it is None
    page = 1

    # Check if cake recipes were successfully retrieve
    if cake_recipes:
        # Determine if there are more recipes by checking
        # the length of the list
        has_more_recipes = len(cake_recipes) > 0
        # Render the 'index.html' template with recipe data
        # and pagination information
        return render_template(
            'index.html',
            recipes=cake_recipes,
            page=page,
            has_more_recipes=has_more_recipes
        )
    else:
        # Return an error message if fetching recipes fails
        return "Error fetching recipes."


@app.route('/ingredient/<pk>')
def show_ingredients(pk):
    # Use the API response data directly
    recipes = search_cake_recipes(API_KEY)  # Adjust as needed
    ingredients = None

    # Find the recipe with the specified 'pk'
    for recipe in recipes:
        if str(recipe['pk']) == pk:
            ingredients = recipe.get('ingredients', [])
            break

    return render_template('ingredient.html', ingredients=ingredients)


# Route to handle loading more recipes
@app.route('/load-more', methods=['GET'])
def load_more():
    # Get the 'page' parameter from the form submission
    page = int(request.args.get('page', 1))
    cake_recipes = search_cake_recipes(API_KEY, page=page)

    if cake_recipes:
        return render_template('index.html', recipes=cake_recipes, page=page)
    else:
        return "Error fetching more recipes."


if __name__ == '__main__':
    app.run(debug=True)
