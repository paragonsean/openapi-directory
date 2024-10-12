from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_city import JsonCity
from openapi_server import util


async def resource10_city_geo_id_get_city_get(request: web.Request, geo_id) -> web.Response:
    """Get a city by its unique geoId.

    Get a city by its unique geoId.

    :param geo_id: the city&#39;s geoId
    :type geo_id: str

    """
    return web.Response(status=200)
