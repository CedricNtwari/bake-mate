## BakeMate

BakeMate is your culinary assistant, seamlessly connecting to a recipe API with ease to deliver a customised experience.

It leverages the Flask web framework to provide a smooth user interface for exploring and managing recipes. Additionally, the application utilizes the Ninja template engine for rendering dynamic content.

### Inspiration

Inspired by a personal challenge, this app is a testament to the everyday struggle of home bakers. The idea came from my wife, who often had to rely on a little bit of speculation. Many recipes describe ingredients in a way that doesn’t always align with what she had in her cupboard. 

BakeMate was born out of a desire to simplify this process, offering a solution for ingredient adjustments with precision.

### Functionality

It facilitates ingredient substitution, allowing you to easily change quantities to match what you have available. 
For instance, if a recipe calls for 250g of an ingredient but you have 100g on hand, BakeMate guides you through the perfect ingredient adjustment for your baking projects.

### Credits

- **Food2fork API**: Acknowledgment to Food2fork API (https://food2fork.ca/#Search-Recipes) for their comprehensive food-related API that enhances the recipe retrieval and exploration experience in BakeMate.


### Acknowledgements

- I would like to express my gratitude to my mentor,Adegbenga Adeye, the Code Institute, and everyone who has supported me on my journey to becoming a full-stack software developer. The warmth and encouragement I've received have been truly wonderful. Thank you!


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

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
