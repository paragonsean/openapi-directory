from typing import List, Dict
from aiohttp import web

from openapi_server.models.btcer400_response import Btcer400Response
from openapi_server.models.btcer401_response import Btcer401Response
from openapi_server.models.btcer404_response import Btcer404Response
from openapi_server.models.btcer500_response import Btcer500Response
from openapi_server.models.btcer502_response import Btcer502Response
from openapi_server.models.btcer503_response import Btcer503Response
from openapi_server.models.btcer504_response import Btcer504Response
from openapi_server.models.btcer_request import BtcerRequest
from openapi_server import util


async def btcer(request: web.Request, body=None) -> web.Response:
    """Birth Certificate

    API to verify Birth Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BtcerRequest.from_dict(body)
    return web.Response(status=200)


async def ctcer(request: web.Request, body=None) -> web.Response:
    """Caste Certificate

    API to verify Caste Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BtcerRequest.from_dict(body)
    return web.Response(status=200)


async def dtcer(request: web.Request, body=None) -> web.Response:
    """Death Certificate

    API to verify Death Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BtcerRequest.from_dict(body)
    return web.Response(status=200)


async def ewcer(request: web.Request, body=None) -> web.Response:
    """Economically Weaker Section Certificate

    API to verify Economically Weaker Section Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BtcerRequest.from_dict(body)
    return web.Response(status=200)


async def incer(request: web.Request, body=None) -> web.Response:
    """Income Certificate

    API to verify Income Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BtcerRequest.from_dict(body)
    return web.Response(status=200)


async def rmcer(request: web.Request, body=None) -> web.Response:
    """Marriage Certificate

    API to verify Marriage Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BtcerRequest.from_dict(body)
    return web.Response(status=200)


async def rscer(request: web.Request, body=None) -> web.Response:
    """Residence Certificate

    API to verify Residence Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BtcerRequest.from_dict(body)
    return web.Response(status=200)
