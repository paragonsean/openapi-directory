from typing import List, Dict
from aiohttp import web

from openapi_server.models.categories_response import CategoriesResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def merchants_v1_category_get(request: web.Request, ) -> web.Response:
    """Returns a list of all merchant categories for contactless and cash back merchants (example:  Airline, Retail, etc.). 

    Returns a list of all merchant categories for contactless and cash back merchants (example:  Airline, Retail, etc.). 


    """
    return web.Response(status=200)
