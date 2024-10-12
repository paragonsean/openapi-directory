from typing import List, Dict
from aiohttp import web

from openapi_server.models.autocomplete_product_search200_response import AutocompleteProductSearch200Response
from openapi_server.models.classify_grocery_product200_response import ClassifyGroceryProduct200Response
from openapi_server.models.classify_grocery_product_bulk200_response_inner import ClassifyGroceryProductBulk200ResponseInner
from openapi_server.models.classify_grocery_product_bulk_request_inner import ClassifyGroceryProductBulkRequestInner
from openapi_server.models.classify_grocery_product_request import ClassifyGroceryProductRequest
from openapi_server.models.get_comparable_products200_response import GetComparableProducts200Response
from openapi_server.models.get_product_information200_response import GetProductInformation200Response
from openapi_server.models.search_grocery_products200_response import SearchGroceryProducts200Response
from openapi_server.models.search_grocery_products_by_upc200_response import SearchGroceryProductsByUPC200Response
from openapi_server import util


async def autocomplete_product_search(request: web.Request, query, number=None) -> web.Response:
    """Autocomplete Product Search

    Generate suggestions for grocery products based on a (partial) query. The matches will be found by looking in the title only.

    :param query: The (partial) search query.
    :type query: str
    :param number: The number of results to return (between 1 and 25).
    :type number: int

    """
    return web.Response(status=200)


async def classify_grocery_product(request: web.Request, body, locale=None) -> web.Response:
    """Classify Grocery Product

    This endpoint allows you to match a packaged food to a basic category, e.g. a specific brand of milk to the category milk.

    :param body: 
    :type body: dict | bytes
    :param locale: The display name of the returned category, supported is en_US (for American English) and en_GB (for British English).
    :type locale: str

    """
    body = ClassifyGroceryProductRequest.from_dict(body)
    return web.Response(status=200)


async def classify_grocery_product_bulk(request: web.Request, body, locale=None) -> web.Response:
    """Classify Grocery Product Bulk

    Provide a set of product jsons, get back classified products.

    :param body: 
    :type body: list | bytes
    :param locale: The display name of the returned category, supported is en_US (for American English) and en_GB (for British English).
    :type locale: str

    """
    body = [ClassifyGroceryProductBulkRequestInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def get_comparable_products(request: web.Request, upc) -> web.Response:
    """Get Comparable Products

    Find comparable products to the given one.

    :param upc: The UPC of the product for which you want to find comparable products.
    :type upc: 

    """
    return web.Response(status=200)


async def get_product_information(request: web.Request, id) -> web.Response:
    """Get Product Information

    Use a product id to get full information about a product, such as ingredients, nutrition, etc. The nutritional information is per serving.

    :param id: The item&#39;s id.
    :type id: int

    """
    return web.Response(status=200)


async def product_nutrition_by_id_image(request: web.Request, id) -> web.Response:
    """Product Nutrition by ID Image

    Visualize a product&#39;s nutritional information as an image.

    :param id: The id of the product.
    :type id: 

    """
    return web.Response(status=200)


async def product_nutrition_label_image(request: web.Request, id, show_optional_nutrients=None, show_zero_values=None, show_ingredients=None) -> web.Response:
    """Product Nutrition Label Image

    Get a product&#39;s nutrition label as an image.

    :param id: The product id.
    :type id: 
    :param show_optional_nutrients: Whether to show optional nutrients.
    :type show_optional_nutrients: bool
    :param show_zero_values: Whether to show zero values.
    :type show_zero_values: bool
    :param show_ingredients: Whether to show a list of ingredients.
    :type show_ingredients: bool

    """
    return web.Response(status=200)


async def product_nutrition_label_widget(request: web.Request, id, default_css=None, show_optional_nutrients=None, show_zero_values=None, show_ingredients=None) -> web.Response:
    """Product Nutrition Label Widget

    Get a product&#39;s nutrition label as an HTML widget.

    :param id: The product id.
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


async def search_grocery_products(request: web.Request, query=None, min_calories=None, max_calories=None, min_carbs=None, max_carbs=None, min_protein=None, max_protein=None, min_fat=None, max_fat=None, add_product_information=None, offset=None, number=None) -> web.Response:
    """Search Grocery Products

    Search packaged food products, such as frozen pizza or Greek yogurt.

    :param query: The (natural language) search query.
    :type query: str
    :param min_calories: The minimum amount of calories the product must have.
    :type min_calories: 
    :param max_calories: The maximum amount of calories the product can have.
    :type max_calories: 
    :param min_carbs: The minimum amount of carbohydrates in grams the product must have.
    :type min_carbs: 
    :param max_carbs: The maximum amount of carbohydrates in grams the product can have.
    :type max_carbs: 
    :param min_protein: The minimum amount of protein in grams the product must have.
    :type min_protein: 
    :param max_protein: The maximum amount of protein in grams the product can have.
    :type max_protein: 
    :param min_fat: The minimum amount of fat in grams the product must have.
    :type min_fat: 
    :param max_fat: The maximum amount of fat in grams the product can have.
    :type max_fat: 
    :param add_product_information: If set to true, you get more information about the products returned.
    :type add_product_information: bool
    :param offset: The number of results to skip (between 0 and 900).
    :type offset: int
    :param number: The maximum number of items to return (between 1 and 100). Defaults to 10.
    :type number: int

    """
    return web.Response(status=200)


async def search_grocery_products_by_upc(request: web.Request, upc) -> web.Response:
    """Search Grocery Products by UPC

    Get information about a packaged food using its UPC.

    :param upc: The product&#39;s UPC.
    :type upc: 

    """
    return web.Response(status=200)


async def visualize_product_nutrition_by_id(request: web.Request, id, default_css=None, accept=None) -> web.Response:
    """Product Nutrition by ID Widget

    Visualize a product&#39;s nutritional information as HTML including CSS.

    :param id: The item&#39;s id.
    :type id: int
    :param default_css: Whether the default CSS should be added to the response.
    :type default_css: bool
    :param accept: Accept header.
    :type accept: str

    """
    return web.Response(status=200)
