from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server import util


async def brands_brands(request: web.Request, ) -> web.Response:
    """Gets a list of Brands.

    No Documentation Found.


    """
    return web.Response(status=200)
