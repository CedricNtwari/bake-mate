from flask import Flask, render_template, request, jsonify, redirect
from werkzeug.utils import escape
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__, static_url_path='/static')

FOOD2FORK_API_URL = 'https://food2fork.ca/api/recipe/search/'

# Retrieve API key from environment variable
api_key = os.environ.get("API_KEY")


def search_cake_recipes(api_key, query='cake', page=1):
    """
    Search for cake recipes using the food2fork.ca API.

    Parameters:
    - api_key (str): The food2fork.ca API key.
    - query (str): The query term for recipe search (default is 'cake').§
    - page (int): The page number for pagination (default is 1).

    Returns:
    - tuple or None: A tuple containing a list of dictionaries representing
    the recipes and the total number of recipes,
    or None if the request fails.
    """
    params = {
        'page': page,
        'query': query,
    }
    headers = {
        'Authorization': f'Token {api_key}',
    }
    try:
        response = requests.get(
            FOOD2FORK_API_URL,
            params=params,
            headers=headers
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
            total_recipes = recipes_data.get('count', 0)           
            return recipes, total_recipes
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
    cake_recipes, total_recipes = search_cake_recipes(api_key)
    page = 1

    if cake_recipes:
        has_more_recipes = len(cake_recipes) > 0
        return render_template(
            'index.html',
            recipes=cake_recipes,
            page=page,
            has_more_recipes=has_more_recipes,
            total_recipes=total_recipes
        )
    else:
        # Return an error message if fetching recipes fails
        return "Error fetching recipes."


@app.route('/ingredient/<int:pk>')
def show_ingredients(pk):
    # Use the API response data directly
    recipes, total_recipes = search_cake_recipes(api_key)
    ingredients = None

    # Check if recipes is not None before iterating
    if recipes is not None:
        # Find the recipe with the specified 'pk'
        for recipe in recipes:
            print(f"Recipe PK: {recipe.get('pk')}")
            if recipe.get('pk') == pk:
                ingredients = recipe.get('ingredients', [])
                break

    print(f"Selected Ingredients: {ingredients}")
    return render_template('ingredient.html', ingredients=ingredients, total_recipes=total_recipes)


# Route to handle search
@app.route('/search')
def search():
    # Get the search query from the request parameters
    query = request.args.get('query', '')

    # Validate user input (allow only letters and spaces)
    if not query.replace(" ", "").isalpha() or not query.strip():
        return render_template('invalid_input.html', query=escape(query))

    # Call the function to search for recipes using the Food2Fork API
    cake_recipes, total_recipes = search_cake_recipes(api_key, query=query)
    page = 1

    if cake_recipes:
        has_more_recipes = len(cake_recipes) > 0
        return render_template(
            'search_results.html',
            recipes=cake_recipes,
            page=page,
            has_more_recipes=has_more_recipes,
            total_recipes=total_recipes,
            query=query  # Pass the query to be displayed in the template
        )
    else:
        return render_template('invalid_input.html', query=escape(query))


# Route to handle loading more recipes
@app.route('/load-more', methods=['GET'])
def load_more():
    try:
        page = int(request.args.get('page', 1))
        cake_recipes, total_recipes = search_cake_recipes(api_key, page=page)

        if cake_recipes:
            if len(cake_recipes) > 0:
                # Check if there are more recipes beyond the current page
                has_more_recipes = total_recipes > page

                # Update the page number for the next load
                next_page = page + 1
                return render_template(
                    'index.html',
                    recipes=cake_recipes,
                    page=next_page,
                    has_more_recipes=has_more_recipes
                )
            else:
                # Return a response indicating no more recipes to load
                return jsonify({'message': 'No more recipes to load'})

    except Exception as e:
        print(f"An error occurred: {e}")
        # Redirect the user to the previous page with an error message
        prev_page = max(1, page - 1)
        return redirect(f'/load-more?page={prev_page}&error=true')


# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error_404.html'), 404


# General error handler for other HTTP error codes
@app.errorhandler(500)
def internal_server_error(e):
    return "Internal Server Error", 500


# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
