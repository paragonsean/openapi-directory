from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_usage_list import ApiUsageList
from openapi_server import util


async def get_api_usage_plans_v2(request: web.Request, ) -> web.Response:
    """Get API Isage

    Returns prediction usage on a monthly basis for the current calendar month and future months. Each apiusage object in the response corresponds to a calendar month in your plan.


    """
    return web.Response(status=200)
