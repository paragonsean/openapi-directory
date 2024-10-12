from typing import List, Dict
from aiohttp import web

from openapi_server.models.egcer400_response import Egcer400Response
from openapi_server.models.egcer401_response import Egcer401Response
from openapi_server.models.egcer404_response import Egcer404Response
from openapi_server.models.egcer500_response import Egcer500Response
from openapi_server.models.egcer502_response import Egcer502Response
from openapi_server.models.egcer503_response import Egcer503Response
from openapi_server.models.egcer504_response import Egcer504Response
from openapi_server.models.egcer_request import EgcerRequest
from openapi_server import util


async def egcer(request: web.Request, body=None) -> web.Response:
    """Economically Backward In General Caste Certificate

    API to verify Economically Backward In General Caste Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = EgcerRequest.from_dict(body)
    return web.Response(status=200)


async def ewcer(request: web.Request, body=None) -> web.Response:
    """Economically Weaker Section Certificate

    API to verify Economically Weaker Section Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = EgcerRequest.from_dict(body)
    return web.Response(status=200)


async def incer(request: web.Request, body=None) -> web.Response:
    """Income Certificate

    API to verify Income Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = EgcerRequest.from_dict(body)
    return web.Response(status=200)


async def lhcer(request: web.Request, body=None) -> web.Response:
    """Legal Heir Certificate

    API to verify Legal Heir Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = EgcerRequest.from_dict(body)
    return web.Response(status=200)


async def obcer(request: web.Request, body=None) -> web.Response:
    """OBC Certificate

    API to verify OBC Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = EgcerRequest.from_dict(body)
    return web.Response(status=200)


async def rscer(request: web.Request, body=None) -> web.Response:
    """Residence Certificate

    API to verify Residence Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = EgcerRequest.from_dict(body)
    return web.Response(status=200)


async def shcer(request: web.Request, body=None) -> web.Response:
    """SC/ST  Certificate

    API to verify SC/ST  Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = EgcerRequest.from_dict(body)
    return web.Response(status=200)
