from typing import List, Dict
from aiohttp import web

from openapi_server.models.predictions200_response import Predictions200Response
from openapi_server.models.predictions400_response import Predictions400Response
from openapi_server import util


async def predictions(request: web.Request, year=None) -> web.Response:
    """Get predictions for a given year

    Get all predictions for a given year.

    :param year: A calendar year
    :type year: int

    """
    return web.Response(status=200)
