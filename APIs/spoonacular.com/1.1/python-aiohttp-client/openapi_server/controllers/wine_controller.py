from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_dish_pairing_for_wine200_response import GetDishPairingForWine200Response
from openapi_server.models.get_wine_description200_response import GetWineDescription200Response
from openapi_server.models.get_wine_pairing200_response import GetWinePairing200Response
from openapi_server.models.get_wine_recommendation200_response import GetWineRecommendation200Response
from openapi_server import util


async def get_dish_pairing_for_wine(request: web.Request, wine) -> web.Response:
    """Dish Pairing for Wine

    Find a dish that goes well with a given wine.

    :param wine: The type of wine that should be paired, e.g. \&quot;merlot\&quot;, \&quot;riesling\&quot;, or \&quot;malbec\&quot;.
    :type wine: str

    """
    return web.Response(status=200)


async def get_wine_description(request: web.Request, wine) -> web.Response:
    """Wine Description

    Get a simple description of a certain wine, e.g. \&quot;malbec\&quot;, \&quot;riesling\&quot;, or \&quot;merlot\&quot;.

    :param wine: The name of the wine that should be paired, e.g. \&quot;merlot\&quot;, \&quot;riesling\&quot;, or \&quot;malbec\&quot;.
    :type wine: str

    """
    return web.Response(status=200)


async def get_wine_pairing(request: web.Request, food, max_price=None) -> web.Response:
    """Wine Pairing

    Find a wine that goes well with a food. Food can be a dish name (\&quot;steak\&quot;), an ingredient name (\&quot;salmon\&quot;), or a cuisine (\&quot;italian\&quot;).

    :param food: The food to get a pairing for. This can be a dish (\&quot;steak\&quot;), an ingredient (\&quot;salmon\&quot;), or a cuisine (\&quot;italian\&quot;).
    :type food: str
    :param max_price: The maximum price for the specific wine recommendation in USD.
    :type max_price: 

    """
    return web.Response(status=200)


async def get_wine_recommendation(request: web.Request, wine, max_price=None, min_rating=None, number=None) -> web.Response:
    """Wine Recommendation

    Get a specific wine recommendation (concrete product) for a given wine type, e.g. \&quot;merlot\&quot;.

    :param wine: The type of wine to get a specific product recommendation for.
    :type wine: str
    :param max_price: The maximum price for the specific wine recommendation in USD.
    :type max_price: 
    :param min_rating: The minimum rating of the recommended wine between 0 and 1. For example, 0.8 equals 4 out of 5 stars.
    :type min_rating: 
    :param number: The number of wine recommendations expected (between 1 and 100).
    :type number: 

    """
    return web.Response(status=200)
