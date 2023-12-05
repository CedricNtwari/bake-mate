from flask import Flask, render_template, request
from config import API_KEY
import requests

app = Flask(__name__)

FOOD2FORK_API_URL = 'https://food2fork.ca/api/recipe/search/'


def search_cake_recipes(api_key, query='cake', page=1):
    params = {
        'page': page,
        'query': query,
    }

    headers = {
        'Authorization': f'Token {api_key}',
    }

    try:
        response = requests.get(
            FOOD2FORK_API_URL, params=params, headers=headers)

        if response.status_code == 200:
            recipes_data = response.json()

            if 'error' in recipes_data:
                error_message = recipes_data['error']
                print(f"Error in API response: {error_message}")
                return None

            recipes = recipes_data.get('results', [])
            return recipes
        else:
            print(
                f"Error {response.status_code}: "
                f"Unable to fetch recipes. {response.content}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


@app.route('/')
def index():
    cake_recipes = search_cake_recipes(API_KEY)
    # Set a default value for 'page' if it is None
    page = 1
    if cake_recipes:
        has_more_recipes = len(cake_recipes) > 0
        return render_template(
            'index.html',
            recipes=cake_recipes,
            page=page,
            has_more_recipes=has_more_recipes
        )
    else:
        return "Error fetching recipes."


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
