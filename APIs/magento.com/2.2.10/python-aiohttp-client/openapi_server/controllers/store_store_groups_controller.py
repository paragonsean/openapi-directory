from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.store_data_group_interface import StoreDataGroupInterface
from openapi_server import util


async def store_group_repository_v1_get_list_get(request: web.Request, ) -> web.Response:
    """store/storeGroups

    Retrieve list of all groups


    """
    return web.Response(status=200)
