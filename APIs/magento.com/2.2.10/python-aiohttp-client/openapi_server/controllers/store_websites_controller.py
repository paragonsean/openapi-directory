from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.store_data_website_interface import StoreDataWebsiteInterface
from openapi_server import util


async def store_website_repository_v1_get_list_get(request: web.Request, ) -> web.Response:
    """store/websites

    Retrieve list of all websites


    """
    return web.Response(status=200)
