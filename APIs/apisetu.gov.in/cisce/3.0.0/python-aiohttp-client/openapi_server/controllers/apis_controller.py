from typing import List, Dict
from aiohttp import web

from openapi_server.models.hpcer400_response import Hpcer400Response
from openapi_server.models.hpcer401_response import Hpcer401Response
from openapi_server.models.hpcer404_response import Hpcer404Response
from openapi_server.models.hpcer500_response import Hpcer500Response
from openapi_server.models.hpcer502_response import Hpcer502Response
from openapi_server.models.hpcer503_response import Hpcer503Response
from openapi_server.models.hpcer504_response import Hpcer504Response
from openapi_server.models.hpcer_request import HpcerRequest
from openapi_server import util


async def hpcer(request: web.Request, body=None) -> web.Response:
    """Class XII Passing Certificate

    API to verify Class XII Passing Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def hscer(request: web.Request, body=None) -> web.Response:
    """Class XII Marksheet

    API to verify Class XII Marksheet.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def hsmgr(request: web.Request, body=None) -> web.Response:
    """Class XII Migration Certificate

    API to verify Class XII Migration Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def spcer(request: web.Request, body=None) -> web.Response:
    """Class X Passing Certificate

    API to verify Class X Passing Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def sscer(request: web.Request, body=None) -> web.Response:
    """Class X Marksheet

    API to verify Class X Marksheet.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)
