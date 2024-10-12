from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_version_number_additional_data_ext_get(request: web.Request, version_number, ext, geometries, geometries_zoom=None) -> web.Response:
    """Additional Data

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param ext: Expected response format.
    :type ext: str
    :param geometries: Comma separated list of geometry UUIDs, previously retrieved from an Search API request.
    :type geometries: str
    :param geometries_zoom: Defines the precision of the geometries.
    :type geometries_zoom: int

    """
    return web.Response(status=200)
