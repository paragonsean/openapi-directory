from typing import List, Dict
from aiohttp import web

from openapi_server.models.autocomplete_menu_item_search200_response import AutocompleteMenuItemSearch200Response
from openapi_server.models.get_menu_item_information200_response import GetMenuItemInformation200Response
from openapi_server.models.search_menu_items200_response import SearchMenuItems200Response
from openapi_server import util


async def autocomplete_menu_item_search(request: web.Request, query, number=None) -> web.Response:
    """Autocomplete Menu Item Search

    Generate suggestions for menu items based on a (partial) query. The matches will be found by looking in the title only.

    :param query: The (partial) search query.
    :type query: str
    :param number: The number of results to return (between 1 and 25).
    :type number: 

    """
    return web.Response(status=200)


async def get_menu_item_information(request: web.Request, id) -> web.Response:
    """Get Menu Item Information

    Use a menu item id to get all available information about a menu item, such as nutrition.

    :param id: The item&#39;s id.
    :type id: int

    """
    return web.Response(status=200)


async def menu_item_nutrition_by_id_image(request: web.Request, id) -> web.Response:
    """Menu Item Nutrition by ID Image

    Visualize a menu item&#39;s nutritional information as HTML including CSS.

    :param id: The menu item id.
    :type id: 

    """
    return web.Response(status=200)


async def menu_item_nutrition_label_image(request: web.Request, id, show_optional_nutrients=None, show_zero_values=None, show_ingredients=None) -> web.Response:
    """Menu Item Nutrition Label Image

    Visualize a menu item&#39;s nutritional label information as an image.

    :param id: The menu item id.
    :type id: 
    :param show_optional_nutrients: Whether to show optional nutrients.
    :type show_optional_nutrients: bool
    :param show_zero_values: Whether to show zero values.
    :type show_zero_values: bool
    :param show_ingredients: Whether to show a list of ingredients.
    :type show_ingredients: bool

    """
    return web.Response(status=200)


async def menu_item_nutrition_label_widget(request: web.Request, id, default_css=None, show_optional_nutrients=None, show_zero_values=None, show_ingredients=None) -> web.Response:
    """Menu Item Nutrition Label Widget

    Visualize a menu item&#39;s nutritional label information as HTML including CSS.

    :param id: The menu item id.
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


async def search_menu_items(request: web.Request, query=None, min_calories=None, max_calories=None, min_carbs=None, max_carbs=None, min_protein=None, max_protein=None, min_fat=None, max_fat=None, add_menu_item_information=None, offset=None, number=None) -> web.Response:
    """Search Menu Items

    Search over 115,000 menu items from over 800 fast food and chain restaurants. For example, McDonald&#39;s Big Mac or Starbucks Mocha.

    :param query: The (natural language) search query.
    :type query: str
    :param min_calories: The minimum amount of calories the menu item must have.
    :type min_calories: 
    :param max_calories: The maximum amount of calories the menu item can have.
    :type max_calories: 
    :param min_carbs: The minimum amount of carbohydrates in grams the menu item must have.
    :type min_carbs: 
    :param max_carbs: The maximum amount of carbohydrates in grams the menu item can have.
    :type max_carbs: 
    :param min_protein: The minimum amount of protein in grams the menu item must have.
    :type min_protein: 
    :param max_protein: The maximum amount of protein in grams the menu item can have.
    :type max_protein: 
    :param min_fat: The minimum amount of fat in grams the menu item must have.
    :type min_fat: 
    :param max_fat: The maximum amount of fat in grams the menu item can have.
    :type max_fat: 
    :param add_menu_item_information: If set to true, you get more information about the menu items returned.
    :type add_menu_item_information: bool
    :param offset: The number of results to skip (between 0 and 900).
    :type offset: int
    :param number: The maximum number of items to return (between 1 and 100). Defaults to 10.
    :type number: int

    """
    return web.Response(status=200)


async def visualize_menu_item_nutrition_by_id(request: web.Request, id, default_css=None, accept=None) -> web.Response:
    """Menu Item Nutrition by ID Widget

    Visualize a menu item&#39;s nutritional information as HTML including CSS.

    :param id: The item&#39;s id.
    :type id: int
    :param default_css: Whether the default CSS should be added to the response.
    :type default_css: bool
    :param accept: Accept header.
    :type accept: str

    """
    return web.Response(status=200)
