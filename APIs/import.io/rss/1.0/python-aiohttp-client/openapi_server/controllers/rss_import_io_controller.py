from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server import util


async def extractor_extractor_id_runs_get(request: web.Request, extractor_id) -> web.Response:
    """Get a feed of the runs performed on an extractor

    

    :param extractor_id: The id of the extractor to start get the crawl run data
    :type extractor_id: str

    """
    return web.Response(status=200)
