from typing import List, Dict
from aiohttp import web

from openapi_server.models.ctcer400_response import Ctcer400Response
from openapi_server.models.ctcer401_response import Ctcer401Response
from openapi_server.models.ctcer404_response import Ctcer404Response
from openapi_server.models.ctcer500_response import Ctcer500Response
from openapi_server.models.ctcer502_response import Ctcer502Response
from openapi_server.models.ctcer503_response import Ctcer503Response
from openapi_server.models.ctcer504_response import Ctcer504Response
from openapi_server.models.ctcer_request import CtcerRequest
from openapi_server import util


async def ctcer(request: web.Request, body=None) -> web.Response:
    """Caste Certificate

    API to verify Caste Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CtcerRequest.from_dict(body)
    return web.Response(status=200)


async def ewcer(request: web.Request, body=None) -> web.Response:
    """Economically Weaker Section Certificate

    API to verify Economically Weaker Section Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CtcerRequest.from_dict(body)
    return web.Response(status=200)


async def incer(request: web.Request, body=None) -> web.Response:
    """Income Certificate

    API to verify Income Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CtcerRequest.from_dict(body)
    return web.Response(status=200)


async def rscer(request: web.Request, body=None) -> web.Response:
    """Residence Certificate

    API to verify Residence Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CtcerRequest.from_dict(body)
    return web.Response(status=200)
