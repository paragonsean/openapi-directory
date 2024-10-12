from typing import List, Dict
from aiohttp import web

from openapi_server.models.autocomplete_ingredient_search200_response_inner import AutocompleteIngredientSearch200ResponseInner
from openapi_server.models.compute_ingredient_amount200_response import ComputeIngredientAmount200Response
from openapi_server.models.get_ingredient_information200_response import GetIngredientInformation200Response
from openapi_server.models.get_ingredient_substitutes200_response import GetIngredientSubstitutes200Response
from openapi_server.models.ingredient_search200_response import IngredientSearch200Response
from openapi_server.models.map_ingredients_to_grocery_products200_response_inner import MapIngredientsToGroceryProducts200ResponseInner
from openapi_server.models.map_ingredients_to_grocery_products_request import MapIngredientsToGroceryProductsRequest
from openapi_server import util


async def autocomplete_ingredient_search(request: web.Request, query=None, number=None, meta_information=None, intolerances=None, language=None) -> web.Response:
    """Autocomplete Ingredient Search

    Autocomplete the entry of an ingredient.

    :param query: The (natural language) search query.
    :type query: str
    :param number: The maximum number of items to return (between 1 and 100). Defaults to 10.
    :type number: int
    :param meta_information: Whether to return more meta information about the ingredients.
    :type meta_information: bool
    :param intolerances: A comma-separated list of intolerances. All recipes returned must not contain ingredients that are not suitable for people with the intolerances entered. See a full list of supported intolerances.
    :type intolerances: str
    :param language: The language of the input. Either &#39;en&#39; or &#39;de&#39;.
    :type language: str

    """
    return web.Response(status=200)


async def compute_ingredient_amount(request: web.Request, id, nutrient, target, unit=None) -> web.Response:
    """Compute Ingredient Amount

    Compute the amount you need of a certain ingredient for a certain nutritional goal. For example, how much pineapple do you have to eat to get 10 grams of protein?

    :param id: The id of the ingredient you want the amount for.
    :type id: 
    :param nutrient: The target nutrient. See a list of supported nutrients.
    :type nutrient: str
    :param target: The target number of the given nutrient.
    :type target: 
    :param unit: The target unit.
    :type unit: str

    """
    return web.Response(status=200)


async def get_ingredient_information(request: web.Request, id, amount=None, unit=None) -> web.Response:
    """Get Ingredient Information

    Use an ingredient id to get all available information about an ingredient, such as its image and supermarket aisle.

    :param id: The item&#39;s id.
    :type id: int
    :param amount: The amount of this ingredient.
    :type amount: 
    :param unit: The unit for the given amount.
    :type unit: str

    """
    return web.Response(status=200)


async def get_ingredient_substitutes(request: web.Request, ingredient_name) -> web.Response:
    """Get Ingredient Substitutes

    Search for substitutes for a given ingredient.

    :param ingredient_name: The name of the ingredient you want to replace.
    :type ingredient_name: str

    """
    return web.Response(status=200)


async def get_ingredient_substitutes_by_id(request: web.Request, id) -> web.Response:
    """Get Ingredient Substitutes by ID

    Search for substitutes for a given ingredient.

    :param id: The item&#39;s id.
    :type id: int

    """
    return web.Response(status=200)


async def ingredient_search(request: web.Request, query=None, add_children=None, min_protein_percent=None, max_protein_percent=None, min_fat_percent=None, max_fat_percent=None, min_carbs_percent=None, max_carbs_percent=None, meta_information=None, intolerances=None, sort=None, sort_direction=None, offset=None, number=None, language=None) -> web.Response:
    """Ingredient Search

    Search for simple whole foods (e.g. fruits, vegetables, nuts, grains, meat, fish, dairy etc.).

    :param query: The (natural language) search query.
    :type query: str
    :param add_children: Whether to add children of found foods.
    :type add_children: bool
    :param min_protein_percent: The minimum percentage of protein the food must have (between 0 and 100).
    :type min_protein_percent: 
    :param max_protein_percent: The maximum percentage of protein the food can have (between 0 and 100).
    :type max_protein_percent: 
    :param min_fat_percent: The minimum percentage of fat the food must have (between 0 and 100).
    :type min_fat_percent: 
    :param max_fat_percent: The maximum percentage of fat the food can have (between 0 and 100).
    :type max_fat_percent: 
    :param min_carbs_percent: The minimum percentage of carbs the food must have (between 0 and 100).
    :type min_carbs_percent: 
    :param max_carbs_percent: The maximum percentage of carbs the food can have (between 0 and 100).
    :type max_carbs_percent: 
    :param meta_information: Whether to return more meta information about the ingredients.
    :type meta_information: bool
    :param intolerances: A comma-separated list of intolerances. All recipes returned must not contain ingredients that are not suitable for people with the intolerances entered. See a full list of supported intolerances.
    :type intolerances: str
    :param sort: The strategy to sort recipes by. See a full list of supported sorting options.
    :type sort: str
    :param sort_direction: The direction in which to sort. Must be either &#39;asc&#39; (ascending) or &#39;desc&#39; (descending).
    :type sort_direction: str
    :param offset: The number of results to skip (between 0 and 900).
    :type offset: int
    :param number: The maximum number of items to return (between 1 and 100). Defaults to 10.
    :type number: int
    :param language: The language of the input. Either &#39;en&#39; or &#39;de&#39;.
    :type language: str

    """
    return web.Response(status=200)


async def ingredients_by_id_image(request: web.Request, id, measure=None) -> web.Response:
    """Ingredients by ID Image

    Visualize a recipe&#39;s ingredient list.

    :param id: The recipe id.
    :type id: 
    :param measure: Whether the the measures should be &#39;us&#39; or &#39;metric&#39;.
    :type measure: str

    """
    return web.Response(status=200)


async def map_ingredients_to_grocery_products(request: web.Request, body) -> web.Response:
    """Map Ingredients to Grocery Products

    Map a set of ingredients to products you can buy in the grocery store.

    :param body: 
    :type body: dict | bytes

    """
    body = MapIngredientsToGroceryProductsRequest.from_dict(body)
    return web.Response(status=200)


async def visualize_ingredients(request: web.Request, content_type=None, language=None, accept=None) -> web.Response:
    """Ingredients Widget

    Visualize ingredients of a recipe. You can play around with that endpoint!

    :param content_type: The content type.
    :type content_type: str
    :param language: The language of the input. Either &#39;en&#39; or &#39;de&#39;.
    :type language: str
    :param accept: Accept header.
    :type accept: str

    """
    return web.Response(status=200)
