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


async def lhcer(request: web.Request, body=None) -> web.Response:
    """Legal Heir Certificate

    API to verify Legal Heir Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CtcerRequest.from_dict(body)
    return web.Response(status=200)


async def obcer(request: web.Request, body=None) -> web.Response:
    """OBC Certificate

    API to verify OBC Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CtcerRequest.from_dict(body)
    return web.Response(status=200)


async def ror1b(request: web.Request, body=None) -> web.Response:
    """Records of Rights

    API to verify Records of Rights.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CtcerRequest.from_dict(body)
    return web.Response(status=200)


async def slcer(request: web.Request, body=None) -> web.Response:
    """Solvency Certificate

    API to verify Solvency Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CtcerRequest.from_dict(body)
    return web.Response(status=200)
