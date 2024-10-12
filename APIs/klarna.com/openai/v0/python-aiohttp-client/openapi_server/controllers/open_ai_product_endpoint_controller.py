from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_response import ProductResponse
from openapi_server import util


async def products_using_get(request: web.Request, q, size=None, budget=None) -> web.Response:
    """API for fetching Klarna product information

    

    :param q: A precise query that matches one very small category or product that needs to be searched for to find the products the user is looking for. If the user explicitly stated what they want, use that as a query. The query is as specific as possible to the product name or category mentioned by the user in its singular form, and don&#39;t contain any clarifiers like latest, newest, cheapest, budget, premium, expensive or similar. The query is always taken from the latest topic, if there is a new topic a new query is started.
    :type q: str
    :param size: number of products returned
    :type size: int
    :param budget: maximum price of the matching product in local currency, filters results
    :type budget: int

    """
    return web.Response(status=200)
