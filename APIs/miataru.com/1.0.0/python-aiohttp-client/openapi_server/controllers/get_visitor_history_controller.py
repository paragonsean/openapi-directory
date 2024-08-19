from typing import List, Dict
from aiohttp import web

from openapi_server.models.miataru_get_visitor_history_request import MiataruGetVisitorHistoryRequest
from openapi_server.models.miataru_get_visitor_history_response import MiataruGetVisitorHistoryResponse
from openapi_server import util


async def get_visitor_history(request: web.Request, body) -> web.Response:
    """get_visitor_history

    Visitor History is stored on the server with every request to the location or location history information of a device. There is a server-side setting that controls up to how many Visitors the server is storing in the Visitor History before it removes the oldest one. To request the Visitor History of a particular device the client sends the following POST request to the GetVisitorHistory service URL.

    :param body: the complex JSON formatted datastructure to get the visitor history of one device
    :type body: dict | bytes

    """
    body = MiataruGetVisitorHistoryRequest.from_dict(body)
    return web.Response(status=200)
