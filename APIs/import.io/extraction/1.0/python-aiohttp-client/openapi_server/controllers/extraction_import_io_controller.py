from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.query_response import QueryResponse
from openapi_server import util


async def extractor_extractor_id_get(request: web.Request, extractor_id, url) -> web.Response:
    """Query by extractor endpoint, adhoc runs only.

    

    :param extractor_id: extractorId
    :type extractor_id: str
    :param url: url
    :type url: str

    """
    return web.Response(status=200)
