import requests
import pprint

API_KEY = 'dd6079b14eee42dba13099a4eeff6317'


def get_cake_recipes(api_key, query='cake'):
    """
    Define the base URL for Spoonacular API
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
        pprint.pprint(recipes_data)
        return recipes_data['results']
    else:
        # Print an error message if the request was not successful
        print(f"Error {response.status_code}: Unable to fetch recipes.")
        return None

