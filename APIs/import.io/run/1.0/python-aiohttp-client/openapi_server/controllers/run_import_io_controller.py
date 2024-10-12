from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server import util


async def extractor_extractor_id_cancel_post(request: web.Request, extractor_id) -> web.Response:
    """Cancel an existing crawl.

    

    :param extractor_id: extractorId
    :type extractor_id: str

    """
    return web.Response(status=200)


async def extractor_extractor_id_start_post(request: web.Request, extractor_id) -> web.Response:
    """Launch a crawl from an extractor that a user owns.

    

    :param extractor_id: the id of the extractor to start crawling with
    :type extractor_id: str

    """
    return web.Response(status=200)
