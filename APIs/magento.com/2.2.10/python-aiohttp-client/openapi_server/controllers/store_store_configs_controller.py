from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.store_data_store_config_interface import StoreDataStoreConfigInterface
from openapi_server import util


async def store_store_config_manager_v1_get_store_configs_get(request: web.Request, store_codes=None) -> web.Response:
    """store/storeConfigs

    

    :param store_codes: 
    :type store_codes: List[str]

    """
    return web.Response(status=200)
