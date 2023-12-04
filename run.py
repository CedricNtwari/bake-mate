from flask import Flask, render_template
from config import API_KEY
import requests

app = Flask(__name__)

FOOD2FORK_API_URL = 'https://food2fork.ca/api/recipe/search/'


def search_cake_recipes(api_key, query='cake'):
    params = {
        'page': 1,
        'query': query,
    }

    headers = {
        'Authorization': f'Token {api_key}',
    }

    try:
        response = requests.get(FOOD2FORK_API_URL, params=params, headers=headers)

        if response.status_code == 200:
            recipes_data = response.json()

            if 'error' in recipes_data:
                error_message = recipes_data['error']
                print(f"Error in API response: {error_message}")
                return None

            recipes = recipes_data.get('results', [])
            return recipes
        else:
            print(f"Error {response.status_code}: Unable to fetch recipes. {response.content}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


@app.route('/')
def index():
    cake_recipes = search_cake_recipes(API_KEY)

    if cake_recipes:
        return render_template('index.html', recipes=cake_recipes)
    else:
        return "Error fetching recipes."


if __name__ == '__main__':
    app.run(debug=True)
