from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.success1 import Success1
from openapi_server import util


async def get_location_safety_ranking(request: web.Request, safety_rated_location_id) -> web.Response:
    """Retieve safety information of a location by its Id.

    

    :param safety_rated_location_id: identifier of the location
    :type safety_rated_location_id: str

    """
    return web.Response(status=200)
