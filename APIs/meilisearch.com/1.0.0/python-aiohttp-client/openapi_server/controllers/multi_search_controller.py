from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_one_or_more_indexes_request import SearchOneOrMoreIndexesRequest
from openapi_server import util


async def search_one_or_more_indexes(request: web.Request, body=None) -> web.Response:
    """Search one or more indexes

    Search one or more indexes

    :param body: 
    :type body: dict | bytes

    """
    body = SearchOneOrMoreIndexesRequest.from_dict(body)
    return web.Response(status=200)
