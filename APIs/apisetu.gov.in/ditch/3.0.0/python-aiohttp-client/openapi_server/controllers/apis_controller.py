from typing import List, Dict
from aiohttp import web

from openapi_server.models.incer400_response import Incer400Response
from openapi_server.models.incer401_response import Incer401Response
from openapi_server.models.incer404_response import Incer404Response
from openapi_server.models.incer500_response import Incer500Response
from openapi_server.models.incer502_response import Incer502Response
from openapi_server.models.incer503_response import Incer503Response
from openapi_server.models.incer504_response import Incer504Response
from openapi_server.models.incer_request import IncerRequest
from openapi_server.models.sicrd_request import SicrdRequest
from openapi_server import util


async def incer(request: web.Request, body=None) -> web.Response:
    """Income Certificate

    API to verify Income Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = IncerRequest.from_dict(body)
    return web.Response(status=200)


async def rmcer(request: web.Request, body=None) -> web.Response:
    """Marriage Certificate

    API to verify Marriage Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = IncerRequest.from_dict(body)
    return web.Response(status=200)


async def rscer(request: web.Request, body=None) -> web.Response:
    """Residence Certificate

    API to verify Residence Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = IncerRequest.from_dict(body)
    return web.Response(status=200)


async def sicrd(request: web.Request, body=None) -> web.Response:
    """Senior Citizen Identity Card/ Certificate

    API to verify Senior Citizen Identity Card/ Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = SicrdRequest.from_dict(body)
    return web.Response(status=200)
