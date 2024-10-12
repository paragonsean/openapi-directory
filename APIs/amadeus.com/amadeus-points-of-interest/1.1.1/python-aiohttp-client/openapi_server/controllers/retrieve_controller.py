from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.success1 import Success1
from openapi_server import util


async def get_point_of_interest(request: web.Request, pois_id) -> web.Response:
    """Retieve one point of interest by its Id.

    

    :param pois_id: identifier of the pois
    :type pois_id: str

    """
    return web.Response(status=200)
