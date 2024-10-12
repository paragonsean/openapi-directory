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
from openapi_server.models.ewcer_request import EwcerRequest
from openapi_server.models.obcer_request import ObcerRequest
from openapi_server.models.rscer_request import RscerRequest
from openapi_server.models.shcer_request import ShcerRequest
from openapi_server import util


async def btcer(request: web.Request, body=None) -> web.Response:
    """Birth Certificate

    API to verify Birth Certificate.

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
    body = EwcerRequest.from_dict(body)
    return web.Response(status=200)


async def obcer(request: web.Request, body=None) -> web.Response:
    """OBC Certificate

    API to verify OBC Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ObcerRequest.from_dict(body)
    return web.Response(status=200)


async def racer(request: web.Request, body=None) -> web.Response:
    """Rural Area Certificate

    API to verify Rural Area Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = EwcerRequest.from_dict(body)
    return web.Response(status=200)


async def rscer(request: web.Request, body=None) -> web.Response:
    """Residence Certificate

    API to verify Residence Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = RscerRequest.from_dict(body)
    return web.Response(status=200)


async def shcer(request: web.Request, body=None) -> web.Response:
    """SC/ST  Certificate

    API to verify SC/ST  Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ShcerRequest.from_dict(body)
    return web.Response(status=200)
