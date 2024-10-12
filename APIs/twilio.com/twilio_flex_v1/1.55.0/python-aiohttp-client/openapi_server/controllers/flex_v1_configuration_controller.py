from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_configuration import FlexV1Configuration
from openapi_server import util


async def fetch_configuration(request: web.Request, ui_version=None) -> web.Response:
    """fetch_configuration

    

    :param ui_version: The Pinned UI version of the Configuration resource to fetch.
    :type ui_version: str

    """
    return web.Response(status=200)
