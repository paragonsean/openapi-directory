from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def crr_operation_results_get(request: web.Request, api_version, azure_region, subscription_id, operation_id) -> web.Response:
    """crr_operation_results_get

    

    :param api_version: Client Api Version.
    :type api_version: str
    :param azure_region: Azure region to hit Api
    :type azure_region: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param operation_id: 
    :type operation_id: str

    """
    return web.Response(status=200)
