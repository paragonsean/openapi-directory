from typing import List, Dict
from aiohttp import web

from openapi_server.models.createorchangestoreconfiguration_request1 import CreateorchangestoreconfigurationRequest1
from openapi_server.models.savestoreconfig1 import Savestoreconfig1
from openapi_server.models.storeconfig1 import Storeconfig1
from openapi_server import util


async def createorchangestoreconfiguration(request: web.Request, accept, content_type, body) -> web.Response:
    """Create or change store configuration

    Create or change store configuration data.

    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateorchangestoreconfigurationRequest1.from_dict(body)
    return web.Response(status=200)


async def retrievestoreconfiguration(request: web.Request, content_type, accept) -> web.Response:
    """Retrieve store configuration

    Get store configuration data.

    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str

    """
    return web.Response(status=200)
