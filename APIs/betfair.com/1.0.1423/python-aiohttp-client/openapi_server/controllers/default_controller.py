from typing import List, Dict
from aiohttp import web

from openapi_server.models.all_request_types_example import AllRequestTypesExample
from openapi_server.models.all_response_types_example import AllResponseTypesExample
from openapi_server import util


async def request_post(request: web.Request, body) -> web.Response:
    """request_post

    This is a socket protocol delimited by CRLF (not http)

    :param body: Requests are sent to socket
    :type body: dict | bytes

    """
    body = AllRequestTypesExample.from_dict(body)
    return web.Response(status=200)
