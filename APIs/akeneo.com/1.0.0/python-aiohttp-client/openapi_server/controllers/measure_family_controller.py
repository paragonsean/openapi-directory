from typing import List, Dict
from aiohttp import web

from openapi_server.models.measure_families import MeasureFamilies
from openapi_server.models.measure_families_get200_response import MeasureFamiliesGet200Response
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def measure_families_get(request: web.Request, code) -> web.Response:
    """Get a measure family

    This endpoint allows you to get the information about a given measure family.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def measure_families_get_list(request: web.Request, ) -> web.Response:
    """Get list of measure familiy

    This endpoint allows you to get a list of measure families. Measure families are paginated and sorted by code.


    """
    return web.Response(status=200)
