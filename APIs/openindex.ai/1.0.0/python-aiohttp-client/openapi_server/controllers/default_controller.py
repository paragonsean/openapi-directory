from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.query_request import QueryRequest
from openapi_server.models.query_response import QueryResponse
from openapi_server import util


async def query_query_post(request: web.Request, body) -> web.Response:
    """Query

    Accepts search query objects array each with query and optional filter. Break down complex questions into sub-questions. Refine results by criteria, e.g. time / source, don&#39;t do this often. Split queries if ResponseTooLargeError occurs.

    :param body: 
    :type body: dict | bytes

    """
    body = QueryRequest.from_dict(body)
    return web.Response(status=200)
