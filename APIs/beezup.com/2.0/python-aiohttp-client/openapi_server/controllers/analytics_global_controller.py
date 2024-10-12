from typing import List, Dict
from aiohttp import web

from openapi_server.models.analytics_index import AnalyticsIndex
from openapi_server.models.analytics_store_index import AnalyticsStoreIndex
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server import util


async def analytics_index(request: web.Request, ) -> web.Response:
    """Get the Analytics API operation index

    


    """
    return web.Response(status=200)


async def analytics_store_index(request: web.Request, store_id) -> web.Response:
    """Get the Analytics API operation index for one store

    

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)
