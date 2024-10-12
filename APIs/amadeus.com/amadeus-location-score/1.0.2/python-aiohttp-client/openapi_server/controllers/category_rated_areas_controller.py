from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.get_category_rated_areas200_response import GetCategoryRatedAreas200Response
from openapi_server import util


async def get_category_rated_areas(request: web.Request, latitude, longitude) -> web.Response:
    """GET category rated areas

    

    :param latitude: Latitude in decimal coordinates
    :type latitude: 
    :param longitude: Longitude in decimal coordinates
    :type longitude: 

    """
    return web.Response(status=200)
