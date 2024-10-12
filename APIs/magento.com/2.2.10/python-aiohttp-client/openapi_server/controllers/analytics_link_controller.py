from typing import List, Dict
from aiohttp import web

from openapi_server.models.analytics_data_link_interface import AnalyticsDataLinkInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def analytics_link_provider_v1_get_get(request: web.Request, ) -> web.Response:
    """analytics/link

    


    """
    return web.Response(status=200)
