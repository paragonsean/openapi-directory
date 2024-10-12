from typing import List, Dict
from aiohttp import web

from openapi_server.models.analyze_a_recipe_search_query200_response import AnalyzeARecipeSearchQuery200Response
from openapi_server.models.analyze_recipe_instructions200_response import AnalyzeRecipeInstructions200Response
from openapi_server.models.classify_cuisine200_response import ClassifyCuisine200Response
from openapi_server.models.compute_glycemic_load200_response import ComputeGlycemicLoad200Response
from openapi_server.models.compute_glycemic_load_request import ComputeGlycemicLoadRequest
from openapi_server.models.convert_amounts200_response import ConvertAmounts200Response
from openapi_server.models.create_recipe_card200_response import CreateRecipeCard200Response
from openapi_server.models.extract_recipe_from_website200_response import ExtractRecipeFromWebsite200Response
from openapi_server.models.generate_meal_plan200_response_meals_inner import GenerateMealPlan200ResponseMealsInner
from openapi_server.models.get_analyzed_recipe_instructions200_response import GetAnalyzedRecipeInstructions200Response
from openapi_server.models.get_random_recipes200_response import GetRandomRecipes200Response
from openapi_server.models.get_recipe_equipment_by_id200_response import GetRecipeEquipmentByID200Response
from openapi_server.models.get_recipe_information_bulk200_response_inner import GetRecipeInformationBulk200ResponseInner
from openapi_server.models.get_recipe_ingredients_by_id200_response import GetRecipeIngredientsByID200Response
from openapi_server.models.get_recipe_nutrition_widget_by_id200_response import GetRecipeNutritionWidgetByID200Response
from openapi_server.models.get_recipe_price_breakdown_by_id200_response import GetRecipePriceBreakdownByID200Response
from openapi_server.models.get_recipe_taste_by_id200_response import GetRecipeTasteByID200Response
from openapi_server.models.guess_nutrition_by_dish_name200_response import GuessNutritionByDishName200Response
from openapi_server.models.parse_ingredients200_response_inner import ParseIngredients200ResponseInner
from openapi_server.models.quick_answer200_response import QuickAnswer200Response
from openapi_server.models.search_grocery_products200_response_products_inner import SearchGroceryProducts200ResponseProductsInner
from openapi_server.models.search_recipes200_response import SearchRecipes200Response
from openapi_server.models.search_recipes200_response_results_inner import SearchRecipes200ResponseResultsInner
from openapi_server.models.search_recipes_by_ingredients200_response_inner import SearchRecipesByIngredients200ResponseInner
from openapi_server.models.summarize_recipe200_response import SummarizeRecipe200Response
from openapi_server import util


async def analyze_a_recipe_search_query(request: web.Request, q) -> web.Response:
    """Analyze a Recipe Search Query

    Parse a recipe search query to find out its intention.

    :param q: The recipe search query.
    :type q: str

    """
    return web.Response(status=200)


async def analyze_recipe_instructions(request: web.Request, content_type=None) -> web.Response:
    """Analyze Recipe Instructions

    This endpoint allows you to break down instructions into atomic steps. Furthermore, each step will contain the ingredients and equipment required. Additionally, all ingredients and equipment from the recipe&#39;s instructions will be extracted independently of the step they&#39;re used in.

    :param content_type: The content type.
    :type content_type: str

    """
    return web.Response(status=200)


async def autocomplete_recipe_search(request: web.Request, query=None, number=None) -> web.Response:
    """Autocomplete Recipe Search

    Autocomplete a partial input to suggest possible recipe names.

    :param query: The (natural language) search query.
    :type query: str
    :param number: The maximum number of items to return (between 1 and 100). Defaults to 10.
    :type number: int

    """
    return web.Response(status=200)


async def classify_cuisine(request: web.Request, content_type=None) -> web.Response:
    """Classify Cuisine

    Classify the recipe&#39;s cuisine.

    :param content_type: The content type.
    :type content_type: str

    """
    return web.Response(status=200)


async def compute_glycemic_load(request: web.Request, body, language=None) -> web.Response:
    """Compute Glycemic Load

    Retrieve the glycemic index for a list of ingredients and compute the individual and total glycemic load.

    :param body: 
    :type body: dict | bytes
    :param language: The language of the input. Either &#39;en&#39; or &#39;de&#39;.
    :type language: str

    """
    body = ComputeGlycemicLoadRequest.from_dict(body)
    return web.Response(status=200)


async def convert_amounts(request: web.Request, ingredient_name, source_amount, source_unit, target_unit) -> web.Response:
    """Convert Amounts

    Convert amounts like \&quot;2 cups of flour to grams\&quot;.

    :param ingredient_name: The ingredient which you want to convert.
    :type ingredient_name: str
    :param source_amount: The amount from which you want to convert, e.g. the 2.5 in \&quot;2.5 cups of flour to grams\&quot;.
    :type source_amount: 
    :param source_unit: The unit from which you want to convert, e.g. the grams in \&quot;2.5 cups of flour to grams\&quot;. You can also use \&quot;piece\&quot;, e.g. \&quot;3.4 oz tomatoes to piece\&quot;
    :type source_unit: str
    :param target_unit: The unit to which you want to convert, e.g. the grams in \&quot;2.5 cups of flour to grams\&quot;. You can also use \&quot;piece\&quot;, e.g. \&quot;3.4 oz tomatoes to piece\&quot;
    :type target_unit: str

    """
    return web.Response(status=200)


async def create_recipe_card(request: web.Request, content_type=None) -> web.Response:
    """Create Recipe Card

    Generate a recipe card for a recipe.

    :param content_type: The content type.
    :type content_type: str

    """
    return web.Response(status=200)


async def equipment_by_id_image(request: web.Request, id) -> web.Response:
    """Equipment by ID Image

    Visualize a recipe&#39;s equipment list as an image.

    :param id: The recipe id.
    :type id: 

    """
    return web.Response(status=200)


async def extract_recipe_from_website(request: web.Request, url, force_extraction=None, analyze=None, include_nutrition=None, include_taste=None) -> web.Response:
    """Extract Recipe from Website

    This endpoint lets you extract recipe data such as title, ingredients, and instructions from any properly formatted Website.

    :param url: The URL of the recipe page.
    :type url: str
    :param force_extraction: If true, the extraction will be triggered whether we already know the recipe or not. Use this only if information is missing as this operation is slower.
    :type force_extraction: bool
    :param analyze: If true, the recipe will be analyzed and classified resolving in more data such as cuisines, dish types, and more.
    :type analyze: bool
    :param include_nutrition: Include nutrition data in the recipe information. Nutrition data is per serving. If you want the nutrition data for the entire recipe, just multiply by the number of servings.
    :type include_nutrition: bool
    :param include_taste: Whether taste data should be added to correctly parsed ingredients.
    :type include_taste: bool

    """
    return web.Response(status=200)


async def get_analyzed_recipe_instructions(request: web.Request, id, step_breakdown=None) -> web.Response:
    """Get Analyzed Recipe Instructions

    Get an analyzed breakdown of a recipe&#39;s instructions. Each step is enriched with the ingredients and equipment required.

    :param id: The item&#39;s id.
    :type id: int
    :param step_breakdown: Whether to break down the recipe steps even more.
    :type step_breakdown: bool

    """
    return web.Response(status=200)


async def get_random_recipes(request: web.Request, limit_license=None, tags=None, number=None) -> web.Response:
    """Get Random Recipes

    Find random (popular) recipes. If you need to filter recipes by diet, nutrition etc. you might want to consider using the complex recipe search endpoint and set the sort request parameter to random.

    :param limit_license: Whether the recipes should have an open license that allows display with proper attribution.
    :type limit_license: bool
    :param tags: The tags (can be diets, meal types, cuisines, or intolerances) that the recipe must have.
    :type tags: str
    :param number: The maximum number of items to return (between 1 and 100). Defaults to 10.
    :type number: int

    """
    return web.Response(status=200)


async def get_recipe_equipment_by_id(request: web.Request, id) -> web.Response:
    """Equipment by ID

    Get a recipe&#39;s equipment list.

    :param id: The item&#39;s id.
    :type id: int

    """
    return web.Response(status=200)


async def get_recipe_information(request: web.Request, id, include_nutrition=None) -> web.Response:
    """Get Recipe Information

    Use a recipe id to get full information about a recipe, such as ingredients, nutrition, diet and allergen information, etc.

    :param id: The item&#39;s id.
    :type id: int
    :param include_nutrition: Include nutrition data in the recipe information. Nutrition data is per serving. If you want the nutrition data for the entire recipe, just multiply by the number of servings.
    :type include_nutrition: bool

    """
    return web.Response(status=200)


async def get_recipe_information_bulk(request: web.Request, ids, include_nutrition=None) -> web.Response:
    """Get Recipe Information Bulk

    Get information about multiple recipes at once. This is equivalent to calling the Get Recipe Information endpoint multiple times, but faster.

    :param ids: A comma-separated list of recipe ids.
    :type ids: str
    :param include_nutrition: Include nutrition data in the recipe information. Nutrition data is per serving. If you want the nutrition data for the entire recipe, just multiply by the number of servings.
    :type include_nutrition: bool

    """
    return web.Response(status=200)


async def get_recipe_ingredients_by_id(request: web.Request, id) -> web.Response:
    """Ingredients by ID

    Get a recipe&#39;s ingredient list.

    :param id: The item&#39;s id.
    :type id: int

    """
    return web.Response(status=200)


async def get_recipe_nutrition_widget_by_id(request: web.Request, id) -> web.Response:
    """Nutrition by ID

    Get a recipe&#39;s nutrition data.

    :param id: The item&#39;s id.
    :type id: int

    """
    return web.Response(status=200)


async def get_recipe_price_breakdown_by_id(request: web.Request, id) -> web.Response:
    """Price Breakdown by ID

    Get a recipe&#39;s price breakdown data.

    :param id: The item&#39;s id.
    :type id: int

    """
    return web.Response(status=200)


async def get_recipe_taste_by_id(request: web.Request, id, normalize=None) -> web.Response:
    """Taste by ID

    Get a recipe&#39;s taste. The tastes supported are sweet, salty, sour, bitter, savory, and fatty.

    :param id: The item&#39;s id.
    :type id: int
    :param normalize: Normalize to the strongest taste.
    :type normalize: bool

    """
    return web.Response(status=200)


async def get_similar_recipes(request: web.Request, id, number=None, limit_license=None) -> web.Response:
    """Get Similar Recipes

    Find recipes which are similar to the given one.

    :param id: The item&#39;s id.
    :type id: int
    :param number: The maximum number of items to return (between 1 and 100). Defaults to 10.
    :type number: int
    :param limit_license: Whether the recipes should have an open license that allows display with proper attribution.
    :type limit_license: bool

    """
    return web.Response(status=200)


async def guess_nutrition_by_dish_name(request: web.Request, title) -> web.Response:
    """Guess Nutrition by Dish Name

    Estimate the macronutrients of a dish based on its title.

    :param title: The title of the dish.
    :type title: str

    """
    return web.Response(status=200)


async def ingredients_by_id_image_0(request: web.Request, id, measure=None) -> web.Response:
    """Ingredients by ID Image

    Visualize a recipe&#39;s ingredient list.

    :param id: The recipe id.
    :type id: 
    :param measure: Whether the the measures should be &#39;us&#39; or &#39;metric&#39;.
    :type measure: str

    """
    return web.Response(status=200)


async def parse_ingredients(request: web.Request, content_type=None, language=None) -> web.Response:
    """Parse Ingredients

    Extract an ingredient from plain text.

    :param content_type: The content type.
    :type content_type: str
    :param language: The language of the input. Either &#39;en&#39; or &#39;de&#39;.
    :type language: str

    """
    return web.Response(status=200)


async def price_breakdown_by_id_image(request: web.Request, id) -> web.Response:
    """Price Breakdown by ID Image

    Visualize a recipe&#39;s price breakdown.

    :param id: The recipe id.
    :type id: 

    """
    return web.Response(status=200)


async def quick_answer(request: web.Request, q) -> web.Response:
    """Quick Answer

    Answer a nutrition related natural language question.

    :param q: The nutrition related question.
    :type q: str

    """
    return web.Response(status=200)


async def recipe_nutrition_by_id_image(request: web.Request, id) -> web.Response:
    """Recipe Nutrition by ID Image

    Visualize a recipe&#39;s nutritional information as an image.

    :param id: The recipe id.
    :type id: 

    """
    return web.Response(status=200)


async def recipe_nutrition_label_image(request: web.Request, id, show_optional_nutrients=None, show_zero_values=None, show_ingredients=None) -> web.Response:
    """Recipe Nutrition Label Image

    Get a recipe&#39;s nutrition label as an image.

    :param id: The recipe id.
    :type id: 
    :param show_optional_nutrients: Whether to show optional nutrients.
    :type show_optional_nutrients: bool
    :param show_zero_values: Whether to show zero values.
    :type show_zero_values: bool
    :param show_ingredients: Whether to show a list of ingredients.
    :type show_ingredients: bool

    """
    return web.Response(status=200)


async def recipe_nutrition_label_widget(request: web.Request, id, default_css=None, show_optional_nutrients=None, show_zero_values=None, show_ingredients=None) -> web.Response:
    """Recipe Nutrition Label Widget

    Get a recipe&#39;s nutrition label as an HTML widget.

    :param id: The recipe id.
    :type id: 
    :param default_css: Whether the default CSS should be added to the response.
    :type default_css: bool
    :param show_optional_nutrients: Whether to show optional nutrients.
    :type show_optional_nutrients: bool
    :param show_zero_values: Whether to show zero values.
    :type show_zero_values: bool
    :param show_ingredients: Whether to show a list of ingredients.
    :type show_ingredients: bool

    """
    return web.Response(status=200)


async def recipe_taste_by_id_image(request: web.Request, id, normalize=None, rgb=None) -> web.Response:
    """Recipe Taste by ID Image

    Get a recipe&#39;s taste as an image. The tastes supported are sweet, salty, sour, bitter, savory, and fatty.

    :param id: The recipe id.
    :type id: 
    :param normalize: Normalize to the strongest taste.
    :type normalize: bool
    :param rgb: Red, green, blue values for the chart color.
    :type rgb: str

    """
    return web.Response(status=200)


async def search_recipes(request: web.Request, query=None, cuisine=None, exclude_cuisine=None, diet=None, intolerances=None, equipment=None, include_ingredients=None, exclude_ingredients=None, type=None, instructions_required=None, fill_ingredients=None, add_recipe_information=None, add_recipe_nutrition=None, author=None, tags=None, recipe_box_id=None, title_match=None, max_ready_time=None, ignore_pantry=None, sort=None, sort_direction=None, min_carbs=None, max_carbs=None, min_protein=None, max_protein=None, min_calories=None, max_calories=None, min_fat=None, max_fat=None, min_alcohol=None, max_alcohol=None, min_caffeine=None, max_caffeine=None, min_copper=None, max_copper=None, min_calcium=None, max_calcium=None, min_choline=None, max_choline=None, min_cholesterol=None, max_cholesterol=None, min_fluoride=None, max_fluoride=None, min_saturated_fat=None, max_saturated_fat=None, min_vitamin_a=None, max_vitamin_a=None, min_vitamin_c=None, max_vitamin_c=None, min_vitamin_d=None, max_vitamin_d=None, min_vitamin_e=None, max_vitamin_e=None, min_vitamin_k=None, max_vitamin_k=None, min_vitamin_b1=None, max_vitamin_b1=None, min_vitamin_b2=None, max_vitamin_b2=None, min_vitamin_b5=None, max_vitamin_b5=None, min_vitamin_b3=None, max_vitamin_b3=None, min_vitamin_b6=None, max_vitamin_b6=None, min_vitamin_b12=None, max_vitamin_b12=None, min_fiber=None, max_fiber=None, min_folate=None, max_folate=None, min_folic_acid=None, max_folic_acid=None, min_iodine=None, max_iodine=None, min_iron=None, max_iron=None, min_magnesium=None, max_magnesium=None, min_manganese=None, max_manganese=None, min_phosphorus=None, max_phosphorus=None, min_potassium=None, max_potassium=None, min_selenium=None, max_selenium=None, min_sodium=None, max_sodium=None, min_sugar=None, max_sugar=None, min_zinc=None, max_zinc=None, offset=None, number=None, limit_license=None) -> web.Response:
    """Search Recipes

    Search through hundreds of thousands of recipes using advanced filtering and ranking. NOTE: This method combines searching by query, by ingredients, and by nutrients into one endpoint.

    :param query: The (natural language) search query.
    :type query: str
    :param cuisine: The cuisine(s) of the recipes. One or more, comma separated (will be interpreted as &#39;OR&#39;). See a full list of supported cuisines.
    :type cuisine: str
    :param exclude_cuisine: The cuisine(s) the recipes must not match. One or more, comma separated (will be interpreted as &#39;AND&#39;). See a full list of supported cuisines.
    :type exclude_cuisine: str
    :param diet: The diet for which the recipes must be suitable. See a full list of supported diets.
    :type diet: str
    :param intolerances: A comma-separated list of intolerances. All recipes returned must not contain ingredients that are not suitable for people with the intolerances entered. See a full list of supported intolerances.
    :type intolerances: str
    :param equipment: The equipment required. Multiple values will be interpreted as &#39;or&#39;. For example, value could be \&quot;blender, frying pan, bowl\&quot;.
    :type equipment: str
    :param include_ingredients: A comma-separated list of ingredients that should/must be used in the recipes.
    :type include_ingredients: str
    :param exclude_ingredients: A comma-separated list of ingredients or ingredient types that the recipes must not contain.
    :type exclude_ingredients: str
    :param type: The type of recipe. See a full list of supported meal types.
    :type type: str
    :param instructions_required: Whether the recipes must have instructions.
    :type instructions_required: bool
    :param fill_ingredients: Add information about the ingredients and whether they are used or missing in relation to the query.
    :type fill_ingredients: bool
    :param add_recipe_information: If set to true, you get more information about the recipes returned.
    :type add_recipe_information: bool
    :param add_recipe_nutrition: If set to true, you get nutritional information about each recipes returned.
    :type add_recipe_nutrition: bool
    :param author: The username of the recipe author.
    :type author: str
    :param tags: The tags (can be diets, meal types, cuisines, or intolerances) that the recipe must have.
    :type tags: str
    :param recipe_box_id: The id of the recipe box to which the search should be limited to.
    :type recipe_box_id: 
    :param title_match: Enter text that must be found in the title of the recipes.
    :type title_match: str
    :param max_ready_time: The maximum time in minutes it should take to prepare and cook the recipe.
    :type max_ready_time: 
    :param ignore_pantry: Whether to ignore typical pantry items, such as water, salt, flour, etc.
    :type ignore_pantry: bool
    :param sort: The strategy to sort recipes by. See a full list of supported sorting options.
    :type sort: str
    :param sort_direction: The direction in which to sort. Must be either &#39;asc&#39; (ascending) or &#39;desc&#39; (descending).
    :type sort_direction: str
    :param min_carbs: The minimum amount of carbohydrates in grams the recipe must have.
    :type min_carbs: 
    :param max_carbs: The maximum amount of carbohydrates in grams the recipe can have.
    :type max_carbs: 
    :param min_protein: The minimum amount of protein in grams the recipe must have.
    :type min_protein: 
    :param max_protein: The maximum amount of protein in grams the recipe can have.
    :type max_protein: 
    :param min_calories: The minimum amount of calories the recipe must have.
    :type min_calories: 
    :param max_calories: The maximum amount of calories the recipe can have.
    :type max_calories: 
    :param min_fat: The minimum amount of fat in grams the recipe must have.
    :type min_fat: 
    :param max_fat: The maximum amount of fat in grams the recipe can have.
    :type max_fat: 
    :param min_alcohol: The minimum amount of alcohol in grams the recipe must have.
    :type min_alcohol: 
    :param max_alcohol: The maximum amount of alcohol in grams the recipe can have.
    :type max_alcohol: 
    :param min_caffeine: The minimum amount of caffeine in milligrams the recipe must have.
    :type min_caffeine: 
    :param max_caffeine: The maximum amount of caffeine in milligrams the recipe can have.
    :type max_caffeine: 
    :param min_copper: The minimum amount of copper in milligrams the recipe must have.
    :type min_copper: 
    :param max_copper: The maximum amount of copper in milligrams the recipe can have.
    :type max_copper: 
    :param min_calcium: The minimum amount of calcium in milligrams the recipe must have.
    :type min_calcium: 
    :param max_calcium: The maximum amount of calcium in milligrams the recipe can have.
    :type max_calcium: 
    :param min_choline: The minimum amount of choline in milligrams the recipe must have.
    :type min_choline: 
    :param max_choline: The maximum amount of choline in milligrams the recipe can have.
    :type max_choline: 
    :param min_cholesterol: The minimum amount of cholesterol in milligrams the recipe must have.
    :type min_cholesterol: 
    :param max_cholesterol: The maximum amount of cholesterol in milligrams the recipe can have.
    :type max_cholesterol: 
    :param min_fluoride: The minimum amount of fluoride in milligrams the recipe must have.
    :type min_fluoride: 
    :param max_fluoride: The maximum amount of fluoride in milligrams the recipe can have.
    :type max_fluoride: 
    :param min_saturated_fat: The minimum amount of saturated fat in grams the recipe must have.
    :type min_saturated_fat: 
    :param max_saturated_fat: The maximum amount of saturated fat in grams the recipe can have.
    :type max_saturated_fat: 
    :param min_vitamin_a: The minimum amount of Vitamin A in IU the recipe must have.
    :type min_vitamin_a: 
    :param max_vitamin_a: The maximum amount of Vitamin A in IU the recipe can have.
    :type max_vitamin_a: 
    :param min_vitamin_c: The minimum amount of Vitamin C milligrams the recipe must have.
    :type min_vitamin_c: 
    :param max_vitamin_c: The maximum amount of Vitamin C in milligrams the recipe can have.
    :type max_vitamin_c: 
    :param min_vitamin_d: The minimum amount of Vitamin D in micrograms the recipe must have.
    :type min_vitamin_d: 
    :param max_vitamin_d: The maximum amount of Vitamin D in micrograms the recipe can have.
    :type max_vitamin_d: 
    :param min_vitamin_e: The minimum amount of Vitamin E in milligrams the recipe must have.
    :type min_vitamin_e: 
    :param max_vitamin_e: The maximum amount of Vitamin E in milligrams the recipe can have.
    :type max_vitamin_e: 
    :param min_vitamin_k: The minimum amount of Vitamin K in micrograms the recipe must have.
    :type min_vitamin_k: 
    :param max_vitamin_k: The maximum amount of Vitamin K in micrograms the recipe can have.
    :type max_vitamin_k: 
    :param min_vitamin_b1: The minimum amount of Vitamin B1 in milligrams the recipe must have.
    :type min_vitamin_b1: 
    :param max_vitamin_b1: The maximum amount of Vitamin B1 in milligrams the recipe can have.
    :type max_vitamin_b1: 
    :param min_vitamin_b2: The minimum amount of Vitamin B2 in milligrams the recipe must have.
    :type min_vitamin_b2: 
    :param max_vitamin_b2: The maximum amount of Vitamin B2 in milligrams the recipe can have.
    :type max_vitamin_b2: 
    :param min_vitamin_b5: The minimum amount of Vitamin B5 in milligrams the recipe must have.
    :type min_vitamin_b5: 
    :param max_vitamin_b5: The maximum amount of Vitamin B5 in milligrams the recipe can have.
    :type max_vitamin_b5: 
    :param min_vitamin_b3: The minimum amount of Vitamin B3 in milligrams the recipe must have.
    :type min_vitamin_b3: 
    :param max_vitamin_b3: The maximum amount of Vitamin B3 in milligrams the recipe can have.
    :type max_vitamin_b3: 
    :param min_vitamin_b6: The minimum amount of Vitamin B6 in milligrams the recipe must have.
    :type min_vitamin_b6: 
    :param max_vitamin_b6: The maximum amount of Vitamin B6 in milligrams the recipe can have.
    :type max_vitamin_b6: 
    :param min_vitamin_b12: The minimum amount of Vitamin B12 in micrograms the recipe must have.
    :type min_vitamin_b12: 
    :param max_vitamin_b12: The maximum amount of Vitamin B12 in micrograms the recipe can have.
    :type max_vitamin_b12: 
    :param min_fiber: The minimum amount of fiber in grams the recipe must have.
    :type min_fiber: 
    :param max_fiber: The maximum amount of fiber in grams the recipe can have.
    :type max_fiber: 
    :param min_folate: The minimum amount of folate in micrograms the recipe must have.
    :type min_folate: 
    :param max_folate: The maximum amount of folate in micrograms the recipe can have.
    :type max_folate: 
    :param min_folic_acid: The minimum amount of folic acid in micrograms the recipe must have.
    :type min_folic_acid: 
    :param max_folic_acid: The maximum amount of folic acid in micrograms the recipe can have.
    :type max_folic_acid: 
    :param min_iodine: The minimum amount of iodine in micrograms the recipe must have.
    :type min_iodine: 
    :param max_iodine: The maximum amount of iodine in micrograms the recipe can have.
    :type max_iodine: 
    :param min_iron: The minimum amount of iron in milligrams the recipe must have.
    :type min_iron: 
    :param max_iron: The maximum amount of iron in milligrams the recipe can have.
    :type max_iron: 
    :param min_magnesium: The minimum amount of magnesium in milligrams the recipe must have.
    :type min_magnesium: 
    :param max_magnesium: The maximum amount of magnesium in milligrams the recipe can have.
    :type max_magnesium: 
    :param min_manganese: The minimum amount of manganese in milligrams the recipe must have.
    :type min_manganese: 
    :param max_manganese: The maximum amount of manganese in milligrams the recipe can have.
    :type max_manganese: 
    :param min_phosphorus: The minimum amount of phosphorus in milligrams the recipe must have.
    :type min_phosphorus: 
    :param max_phosphorus: The maximum amount of phosphorus in milligrams the recipe can have.
    :type max_phosphorus: 
    :param min_potassium: The minimum amount of potassium in milligrams the recipe must have.
    :type min_potassium: 
    :param max_potassium: The maximum amount of potassium in milligrams the recipe can have.
    :type max_potassium: 
    :param min_selenium: The minimum amount of selenium in micrograms the recipe must have.
    :type min_selenium: 
    :param max_selenium: The maximum amount of selenium in micrograms the recipe can have.
    :type max_selenium: 
    :param min_sodium: The minimum amount of sodium in milligrams the recipe must have.
    :type min_sodium: 
    :param max_sodium: The maximum amount of sodium in milligrams the recipe can have.
    :type max_sodium: 
    :param min_sugar: The minimum amount of sugar in grams the recipe must have.
    :type min_sugar: 
    :param max_sugar: The maximum amount of sugar in grams the recipe can have.
    :type max_sugar: 
    :param min_zinc: The minimum amount of zinc in milligrams the recipe must have.
    :type min_zinc: 
    :param max_zinc: The maximum amount of zinc in milligrams the recipe can have.
    :type max_zinc: 
    :param offset: The number of results to skip (between 0 and 900).
    :type offset: int
    :param number: The maximum number of items to return (between 1 and 100). Defaults to 10.
    :type number: int
    :param limit_license: Whether the recipes should have an open license that allows display with proper attribution.
    :type limit_license: bool

    """
    return web.Response(status=200)


async def search_recipes_by_ingredients(request: web.Request, ingredients=None, number=None, limit_license=None, ranking=None, ignore_pantry=None) -> web.Response:
    """Search Recipes by Ingredients

     Ever wondered what recipes you can cook with the ingredients you have in your fridge or pantry? This endpoint lets you find recipes that either maximize the usage of ingredients you have at hand (pre shopping) or minimize the ingredients that you don&#39;t currently have (post shopping).         

    :param ingredients: A comma-separated list of ingredients that the recipes should contain.
    :type ingredients: str
    :param number: The maximum number of items to return (between 1 and 100). Defaults to 10.
    :type number: int
    :param limit_license: Whether the recipes should have an open license that allows display with proper attribution.
    :type limit_license: bool
    :param ranking: Whether to maximize used ingredients (1) or minimize missing ingredients (2) first.
    :type ranking: 
    :param ignore_pantry: Whether to ignore typical pantry items, such as water, salt, flour, etc.
    :type ignore_pantry: bool

    """
    return web.Response(status=200)


async def search_recipes_by_nutrients(request: web.Request, min_carbs=None, max_carbs=None, min_protein=None, max_protein=None, min_calories=None, max_calories=None, min_fat=None, max_fat=None, min_alcohol=None, max_alcohol=None, min_caffeine=None, max_caffeine=None, min_copper=None, max_copper=None, min_calcium=None, max_calcium=None, min_choline=None, max_choline=None, min_cholesterol=None, max_cholesterol=None, min_fluoride=None, max_fluoride=None, min_saturated_fat=None, max_saturated_fat=None, min_vitamin_a=None, max_vitamin_a=None, min_vitamin_c=None, max_vitamin_c=None, min_vitamin_d=None, max_vitamin_d=None, min_vitamin_e=None, max_vitamin_e=None, min_vitamin_k=None, max_vitamin_k=None, min_vitamin_b1=None, max_vitamin_b1=None, min_vitamin_b2=None, max_vitamin_b2=None, min_vitamin_b5=None, max_vitamin_b5=None, min_vitamin_b3=None, max_vitamin_b3=None, min_vitamin_b6=None, max_vitamin_b6=None, min_vitamin_b12=None, max_vitamin_b12=None, min_fiber=None, max_fiber=None, min_folate=None, max_folate=None, min_folic_acid=None, max_folic_acid=None, min_iodine=None, max_iodine=None, min_iron=None, max_iron=None, min_magnesium=None, max_magnesium=None, min_manganese=None, max_manganese=None, min_phosphorus=None, max_phosphorus=None, min_potassium=None, max_potassium=None, min_selenium=None, max_selenium=None, min_sodium=None, max_sodium=None, min_sugar=None, max_sugar=None, min_zinc=None, max_zinc=None, offset=None, number=None, random=None, limit_license=None) -> web.Response:
    """Search Recipes by Nutrients

    Find a set of recipes that adhere to the given nutritional limits. You may set limits for macronutrients (calories, protein, fat, and carbohydrate) and/or many micronutrients.

    :param min_carbs: The minimum amount of carbohydrates in grams the recipe must have.
    :type min_carbs: 
    :param max_carbs: The maximum amount of carbohydrates in grams the recipe can have.
    :type max_carbs: 
    :param min_protein: The minimum amount of protein in grams the recipe must have.
    :type min_protein: 
    :param max_protein: The maximum amount of protein in grams the recipe can have.
    :type max_protein: 
    :param min_calories: The minimum amount of calories the recipe must have.
    :type min_calories: 
    :param max_calories: The maximum amount of calories the recipe can have.
    :type max_calories: 
    :param min_fat: The minimum amount of fat in grams the recipe must have.
    :type min_fat: 
    :param max_fat: The maximum amount of fat in grams the recipe can have.
    :type max_fat: 
    :param min_alcohol: The minimum amount of alcohol in grams the recipe must have.
    :type min_alcohol: 
    :param max_alcohol: The maximum amount of alcohol in grams the recipe can have.
    :type max_alcohol: 
    :param min_caffeine: The minimum amount of caffeine in milligrams the recipe must have.
    :type min_caffeine: 
    :param max_caffeine: The maximum amount of caffeine in milligrams the recipe can have.
    :type max_caffeine: 
    :param min_copper: The minimum amount of copper in milligrams the recipe must have.
    :type min_copper: 
    :param max_copper: The maximum amount of copper in milligrams the recipe can have.
    :type max_copper: 
    :param min_calcium: The minimum amount of calcium in milligrams the recipe must have.
    :type min_calcium: 
    :param max_calcium: The maximum amount of calcium in milligrams the recipe can have.
    :type max_calcium: 
    :param min_choline: The minimum amount of choline in milligrams the recipe must have.
    :type min_choline: 
    :param max_choline: The maximum amount of choline in milligrams the recipe can have.
    :type max_choline: 
    :param min_cholesterol: The minimum amount of cholesterol in milligrams the recipe must have.
    :type min_cholesterol: 
    :param max_cholesterol: The maximum amount of cholesterol in milligrams the recipe can have.
    :type max_cholesterol: 
    :param min_fluoride: The minimum amount of fluoride in milligrams the recipe must have.
    :type min_fluoride: 
    :param max_fluoride: The maximum amount of fluoride in milligrams the recipe can have.
    :type max_fluoride: 
    :param min_saturated_fat: The minimum amount of saturated fat in grams the recipe must have.
    :type min_saturated_fat: 
    :param max_saturated_fat: The maximum amount of saturated fat in grams the recipe can have.
    :type max_saturated_fat: 
    :param min_vitamin_a: The minimum amount of Vitamin A in IU the recipe must have.
    :type min_vitamin_a: 
    :param max_vitamin_a: The maximum amount of Vitamin A in IU the recipe can have.
    :type max_vitamin_a: 
    :param min_vitamin_c: The minimum amount of Vitamin C in milligrams the recipe must have.
    :type min_vitamin_c: 
    :param max_vitamin_c: The maximum amount of Vitamin C in milligrams the recipe can have.
    :type max_vitamin_c: 
    :param min_vitamin_d: The minimum amount of Vitamin D in micrograms the recipe must have.
    :type min_vitamin_d: 
    :param max_vitamin_d: The maximum amount of Vitamin D in micrograms the recipe can have.
    :type max_vitamin_d: 
    :param min_vitamin_e: The minimum amount of Vitamin E in milligrams the recipe must have.
    :type min_vitamin_e: 
    :param max_vitamin_e: The maximum amount of Vitamin E in milligrams the recipe can have.
    :type max_vitamin_e: 
    :param min_vitamin_k: The minimum amount of Vitamin K in micrograms the recipe must have.
    :type min_vitamin_k: 
    :param max_vitamin_k: The maximum amount of Vitamin K in micrograms the recipe can have.
    :type max_vitamin_k: 
    :param min_vitamin_b1: The minimum amount of Vitamin B1 in milligrams the recipe must have.
    :type min_vitamin_b1: 
    :param max_vitamin_b1: The maximum amount of Vitamin B1 in milligrams the recipe can have.
    :type max_vitamin_b1: 
    :param min_vitamin_b2: The minimum amount of Vitamin B2 in milligrams the recipe must have.
    :type min_vitamin_b2: 
    :param max_vitamin_b2: The maximum amount of Vitamin B2 in milligrams the recipe can have.
    :type max_vitamin_b2: 
    :param min_vitamin_b5: The minimum amount of Vitamin B5 in milligrams the recipe must have.
    :type min_vitamin_b5: 
    :param max_vitamin_b5: The maximum amount of Vitamin B5 in milligrams the recipe can have.
    :type max_vitamin_b5: 
    :param min_vitamin_b3: The minimum amount of Vitamin B3 in milligrams the recipe must have.
    :type min_vitamin_b3: 
    :param max_vitamin_b3: The maximum amount of Vitamin B3 in milligrams the recipe can have.
    :type max_vitamin_b3: 
    :param min_vitamin_b6: The minimum amount of Vitamin B6 in milligrams the recipe must have.
    :type min_vitamin_b6: 
    :param max_vitamin_b6: The maximum amount of Vitamin B6 in milligrams the recipe can have.
    :type max_vitamin_b6: 
    :param min_vitamin_b12: The minimum amount of Vitamin B12 in micrograms the recipe must have.
    :type min_vitamin_b12: 
    :param max_vitamin_b12: The maximum amount of Vitamin B12 in micrograms the recipe can have.
    :type max_vitamin_b12: 
    :param min_fiber: The minimum amount of fiber in grams the recipe must have.
    :type min_fiber: 
    :param max_fiber: The maximum amount of fiber in grams the recipe can have.
    :type max_fiber: 
    :param min_folate: The minimum amount of folate in micrograms the recipe must have.
    :type min_folate: 
    :param max_folate: The maximum amount of folate in micrograms the recipe can have.
    :type max_folate: 
    :param min_folic_acid: The minimum amount of folic acid in micrograms the recipe must have.
    :type min_folic_acid: 
    :param max_folic_acid: The maximum amount of folic acid in micrograms the recipe can have.
    :type max_folic_acid: 
    :param min_iodine: The minimum amount of iodine in micrograms the recipe must have.
    :type min_iodine: 
    :param max_iodine: The maximum amount of iodine in micrograms the recipe can have.
    :type max_iodine: 
    :param min_iron: The minimum amount of iron in milligrams the recipe must have.
    :type min_iron: 
    :param max_iron: The maximum amount of iron in milligrams the recipe can have.
    :type max_iron: 
    :param min_magnesium: The minimum amount of magnesium in milligrams the recipe must have.
    :type min_magnesium: 
    :param max_magnesium: The maximum amount of magnesium in milligrams the recipe can have.
    :type max_magnesium: 
    :param min_manganese: The minimum amount of manganese in milligrams the recipe must have.
    :type min_manganese: 
    :param max_manganese: The maximum amount of manganese in milligrams the recipe can have.
    :type max_manganese: 
    :param min_phosphorus: The minimum amount of phosphorus in milligrams the recipe must have.
    :type min_phosphorus: 
    :param max_phosphorus: The maximum amount of phosphorus in milligrams the recipe can have.
    :type max_phosphorus: 
    :param min_potassium: The minimum amount of potassium in milligrams the recipe must have.
    :type min_potassium: 
    :param max_potassium: The maximum amount of potassium in milligrams the recipe can have.
    :type max_potassium: 
    :param min_selenium: The minimum amount of selenium in micrograms the recipe must have.
    :type min_selenium: 
    :param max_selenium: The maximum amount of selenium in micrograms the recipe can have.
    :type max_selenium: 
    :param min_sodium: The minimum amount of sodium in milligrams the recipe must have.
    :type min_sodium: 
    :param max_sodium: The maximum amount of sodium in milligrams the recipe can have.
    :type max_sodium: 
    :param min_sugar: The minimum amount of sugar in grams the recipe must have.
    :type min_sugar: 
    :param max_sugar: The maximum amount of sugar in grams the recipe can have.
    :type max_sugar: 
    :param min_zinc: The minimum amount of zinc in milligrams the recipe must have.
    :type min_zinc: 
    :param max_zinc: The maximum amount of zinc in milligrams the recipe can have.
    :type max_zinc: 
    :param offset: The number of results to skip (between 0 and 900).
    :type offset: int
    :param number: The maximum number of items to return (between 1 and 100). Defaults to 10.
    :type number: int
    :param random: If true, every request will give you a random set of recipes within the requested limits.
    :type random: bool
    :param limit_license: Whether the recipes should have an open license that allows display with proper attribution.
    :type limit_license: bool

    """
    return web.Response(status=200)


async def summarize_recipe(request: web.Request, id) -> web.Response:
    """Summarize Recipe

    Automatically generate a short description that summarizes key information about the recipe.

    :param id: The item&#39;s id.
    :type id: int

    """
    return web.Response(status=200)


async def visualize_equipment(request: web.Request, content_type=None, accept=None) -> web.Response:
    """Equipment Widget

    Visualize the equipment used to make a recipe.

    :param content_type: The content type.
    :type content_type: str
    :param accept: Accept header.
    :type accept: str

    """
    return web.Response(status=200)


async def visualize_price_breakdown(request: web.Request, content_type=None, accept=None, language=None) -> web.Response:
    """Price Breakdown Widget

    Visualize the price breakdown of a recipe.

    :param content_type: The content type.
    :type content_type: str
    :param accept: Accept header.
    :type accept: str
    :param language: The language of the input. Either &#39;en&#39; or &#39;de&#39;.
    :type language: str

    """
    return web.Response(status=200)


async def visualize_recipe_equipment_by_id(request: web.Request, id, default_css=None) -> web.Response:
    """Equipment by ID Widget

    Visualize a recipe&#39;s equipment list.

    :param id: The item&#39;s id.
    :type id: int
    :param default_css: Whether the default CSS should be added to the response.
    :type default_css: bool

    """
    return web.Response(status=200)


async def visualize_recipe_ingredients_by_id(request: web.Request, id, default_css=None, measure=None) -> web.Response:
    """Ingredients by ID Widget

    Visualize a recipe&#39;s ingredient list.

    :param id: The item&#39;s id.
    :type id: int
    :param default_css: Whether the default CSS should be added to the response.
    :type default_css: bool
    :param measure: Whether the the measures should be &#39;us&#39; or &#39;metric&#39;.
    :type measure: str

    """
    return web.Response(status=200)


async def visualize_recipe_nutrition(request: web.Request, content_type=None, accept=None, language=None) -> web.Response:
    """Recipe Nutrition Widget

    Visualize a recipe&#39;s nutritional information as HTML including CSS.

    :param content_type: The content type.
    :type content_type: str
    :param accept: Accept header.
    :type accept: str
    :param language: The language of the input. Either &#39;en&#39; or &#39;de&#39;.
    :type language: str

    """
    return web.Response(status=200)


async def visualize_recipe_nutrition_by_id(request: web.Request, id, default_css=None, accept=None) -> web.Response:
    """Recipe Nutrition by ID Widget

    Visualize a recipe&#39;s nutritional information as HTML including CSS.

    :param id: The item&#39;s id.
    :type id: int
    :param default_css: Whether the default CSS should be added to the response.
    :type default_css: bool
    :param accept: Accept header.
    :type accept: str

    """
    return web.Response(status=200)


async def visualize_recipe_price_breakdown_by_id(request: web.Request, id, default_css=None) -> web.Response:
    """Price Breakdown by ID Widget

    Visualize a recipe&#39;s price breakdown.

    :param id: The item&#39;s id.
    :type id: int
    :param default_css: Whether the default CSS should be added to the response.
    :type default_css: bool

    """
    return web.Response(status=200)


async def visualize_recipe_taste(request: web.Request, language=None, content_type=None, accept=None, normalize=None, rgb=None) -> web.Response:
    """Recipe Taste Widget

    Visualize a recipe&#39;s taste information as HTML including CSS. You can play around with that endpoint!

    :param language: The language of the input. Either &#39;en&#39; or &#39;de&#39;.
    :type language: str
    :param content_type: The content type.
    :type content_type: str
    :param accept: Accept header.
    :type accept: str
    :param normalize: Whether to normalize to the strongest taste.
    :type normalize: bool
    :param rgb: Red, green, blue values for the chart color.
    :type rgb: str

    """
    return web.Response(status=200)


async def visualize_recipe_taste_by_id(request: web.Request, id, normalize=None, rgb=None) -> web.Response:
    """Recipe Taste by ID Widget

    Get a recipe&#39;s taste. The tastes supported are sweet, salty, sour, bitter, savory, and fatty.

    :param id: The item&#39;s id.
    :type id: int
    :param normalize: Whether to normalize to the strongest taste.
    :type normalize: bool
    :param rgb: Red, green, blue values for the chart color.
    :type rgb: str

    """
    return web.Response(status=200)
