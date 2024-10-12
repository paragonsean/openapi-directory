from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.store_data_store_interface import StoreDataStoreInterface
from openapi_server import util


async def store_store_repository_v1_get_list_get(request: web.Request, ) -> web.Response:
    """store/storeViews

    Retrieve list of all stores


    """
    return web.Response(status=200)
