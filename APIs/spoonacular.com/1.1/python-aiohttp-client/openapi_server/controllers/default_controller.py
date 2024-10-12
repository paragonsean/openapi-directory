from typing import List, Dict
from aiohttp import web

from openapi_server.models.analyze_recipe_request import AnalyzeRecipeRequest
from openapi_server.models.analyze_recipe_request1 import AnalyzeRecipeRequest1
from openapi_server.models.search_restaurants200_response import SearchRestaurants200Response
from openapi_server import util


async def analyze_recipe(request: web.Request, body, language=None, include_nutrition=None, include_taste=None) -> web.Response:
    """Analyze Recipe

    This endpoint allows you to send raw recipe information, such as title, servings, and ingredients, to then see what we compute (badges, diets, nutrition, and more). This is useful if you have your own recipe data and want to enrich it with our semantic analysis.

    :param body: Example request body.
    :type body: dict | bytes
    :param language: The input language, either \&quot;en\&quot; or \&quot;de\&quot;.
    :type language: str
    :param include_nutrition: Whether nutrition data should be added to correctly parsed ingredients.
    :type include_nutrition: bool
    :param include_taste: Whether taste data should be added to correctly parsed ingredients.
    :type include_taste: bool

    """
    body = AnalyzeRecipeRequest.from_dict(body)
    return web.Response(status=200)


async def create_recipe_card_get(request: web.Request, id, mask=None, background_image=None, background_color=None, font_color=None) -> web.Response:
    """Create Recipe Card

    Generate a recipe card for a recipe.

    :param id: The recipe id.
    :type id: 
    :param mask: The mask to put over the recipe image (\&quot;ellipseMask\&quot;, \&quot;diamondMask\&quot;, \&quot;starMask\&quot;, \&quot;heartMask\&quot;, \&quot;potMask\&quot;, \&quot;fishMask\&quot;).
    :type mask: str
    :param background_image: The background image (\&quot;none\&quot;,\&quot;background1\&quot;, or \&quot;background2\&quot;).
    :type background_image: str
    :param background_color: The background color for the recipe card as a hex-string.
    :type background_color: str
    :param font_color: The font color for the recipe card as a hex-string.
    :type font_color: str

    """
    return web.Response(status=200)


async def search_restaurants(request: web.Request, query=None, lat=None, lng=None, distance=None, budget=None, cuisine=None, min_rating=None, is_open=None, sort=None, page=None) -> web.Response:
    """Search Restaurants

    Search through thousands of restaurants (in North America) by location, cuisine, budget, and more.

    :param query: The search query.
    :type query: str
    :param lat: The latitude of the user&#39;s location.
    :type lat: 
    :param lng: The longitude of the user&#39;s location.\&quot;.
    :type lng: 
    :param distance: The distance around the location in miles.
    :type distance: 
    :param budget: The user&#39;s budget for a meal in USD.
    :type budget: 
    :param cuisine: The cuisine of the restaurant.
    :type cuisine: str
    :param min_rating: The minimum rating of the restaurant between 0 and 5.
    :type min_rating: 
    :param is_open: Whether the restaurant must be open at the time of search.
    :type is_open: bool
    :param sort: How to sort the results, one of the following &#39;cheapest&#39;, &#39;fastest&#39;, &#39;rating&#39;, &#39;distance&#39; or the default &#39;relevance&#39;.
    :type sort: str
    :param page: The page number of results.
    :type page: 

    """
    return web.Response(status=200)
