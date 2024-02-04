## BakeMate

BakeMate is your culinary assistant, seamlessly connecting to a recipe API with ease to deliver a customised experience.

It leverages the Flask web framework to provide a smooth user interface for exploring and managing recipes. Additionally, the application utilizes the Ninja template engine for rendering dynamic content.

![BakeMate Platform](/images/Screenshot.png)

### Inspiration

Inspired by a personal challenge, this app is a testament to the everyday struggle of home bakers. The idea came from my wife, who often had to rely on a little bit of speculation. Many recipes describe ingredients in a way that doesn’t always align with what she had in her cupboard. 

BakeMate was born out of a desire to simplify this process, offering a solution for ingredient adjustments with precision.

## Features

1. **Recipe Search:** Users can search for cake recipes using the Food2Fork API. The search can be initiated from the home page or through a dedicated search route.

2. **Recipe Display:** The app displays a list of cake recipes on the home page, along with details such as recipe names and images. Users can view additional recipes by clicking on the "Load More" button.

3. **Ingredient Details:** Users can view the details of a specific recipe, including the list of ingredients. The ingredients are displayed on a dedicated page accessible through the `/ingredient/<int:pk>` route.

4. **Search Functionality:** Users can perform searches based on a query term, and the app will retrieve and display relevant cake recipes.

5. **Pagination:** The app supports pagination, allowing users to load more recipes beyond the initial set.

6. **Error Handling:** Custom error handlers are implemented for 404 (page not found) and 500 (internal server error) HTTP status codes.

7. **Deployment to Heroku:** The app is set up for deployment on Heroku, ensuring accessibility to a wider audience. It utilizes environment variables for sensitive information like the API key.

8. **Responsive Design:** The app is designed to be responsive, ensuring a good user experience on different screen sizes.


### Functionality

It facilitates ingredient substitution, allowing you to easily change quantities to match what you have available. 
For instance, if a recipe calls for 250g of an ingredient but you have 100g on hand, BakeMate guides you through the perfect ingredient adjustment for your baking projects.

### Credits

- **Food2fork API**: Acknowledgment to Food2fork API (https://food2fork.ca/#Search-Recipes) for their comprehensive food-related API that enhances the recipe retrieval and exploration experience in BakeMate.


## Deployment

This project is hosted on Heroku.

- The live link can be found here: <https://bake-mate-deploy-3337af864966.herokuapp.com/>.

## Testing

- Tested in different browsers: Chrome, Firefox, Safari.
- The website is responsive and functions on all screen sizes using devtools device toolbar.
- All features work well, are readable, and easy to understand.

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal

---

Happy coding!
