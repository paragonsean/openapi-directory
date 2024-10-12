from typing import List, Dict
from aiohttp import web

from openapi_server.models.chcer400_response import Chcer400Response
from openapi_server.models.chcer401_response import Chcer401Response
from openapi_server.models.chcer404_response import Chcer404Response
from openapi_server.models.chcer500_response import Chcer500Response
from openapi_server.models.chcer502_response import Chcer502Response
from openapi_server.models.chcer503_response import Chcer503Response
from openapi_server.models.chcer504_response import Chcer504Response
from openapi_server.models.chcer_request import ChcerRequest
from openapi_server import util


async def chcer(request: web.Request, body=None) -> web.Response:
    """Character Certificate

    API to verify Character Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def dmcer(request: web.Request, body=None) -> web.Response:
    """Domicile Certificate

    API to verify Domicile Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def dpcer(request: web.Request, body=None) -> web.Response:
    """Dependency Certificate

    API to verify Dependency Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def incer(request: web.Request, body=None) -> web.Response:
    """Income Certificate

    API to verify Income Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def rscer(request: web.Request, body=None) -> web.Response:
    """Residence Certificate

    API to verify Residence Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def shcer(request: web.Request, body=None) -> web.Response:
    """SC/ST  Certificate

    API to verify SC/ST  Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)
