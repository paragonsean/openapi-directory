from typing import List, Dict
from aiohttp import web

from openapi_server.models.statistics import Statistics
from openapi_server import util


async def retrieve_current_neo_statistics(request: web.Request, ) -> web.Response:
    """Get the Near Earth Object data set totals

    retrieveCurrentNeoStatistics


    """
    return web.Response(status=200)
