from typing import List, Dict
from aiohttp import web

from openapi_server.models.alltr400_response import Alltr400Response
from openapi_server.models.alltr401_response import Alltr401Response
from openapi_server.models.alltr404_response import Alltr404Response
from openapi_server.models.alltr500_response import Alltr500Response
from openapi_server.models.alltr502_response import Alltr502Response
from openapi_server.models.alltr503_response import Alltr503Response
from openapi_server.models.alltr504_response import Alltr504Response
from openapi_server.models.alltr_request import AlltrRequest
from openapi_server import util


async def alltr(request: web.Request, body=None) -> web.Response:
    """Allotment Letter

    API to verify Allotment Letter.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlltrRequest.from_dict(body)
    return web.Response(status=200)


async def bknoc(request: web.Request, body=None) -> web.Response:
    """NOC For Banks

    API to verify NOC For Banks.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlltrRequest.from_dict(body)
    return web.Response(status=200)


async def bpcer(request: web.Request, body=None) -> web.Response:
    """Building Plan

    API to verify Building Plan.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlltrRequest.from_dict(body)
    return web.Response(status=200)


async def cfltr(request: web.Request, body=None) -> web.Response:
    """Confirmatory Letter

    API to verify Confirmatory Letter.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlltrRequest.from_dict(body)
    return web.Response(status=200)


async def lcsag(request: web.Request, body=None) -> web.Response:
    """Lease cum Sale Agreement

    API to verify Lease cum Sale Agreement.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlltrRequest.from_dict(body)
    return web.Response(status=200)


async def pscer(request: web.Request, body=None) -> web.Response:
    """Possession Certificate

    API to verify Possession Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlltrRequest.from_dict(body)
    return web.Response(status=200)


async def psnoc(request: web.Request, body=None) -> web.Response:
    """NOC for New Power Supply

    API to verify NOC for New Power Supply.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlltrRequest.from_dict(body)
    return web.Response(status=200)


async def wtrbl(request: web.Request, body=None) -> web.Response:
    """Water Bill/ Connection

    API to verify Water Bill/ Connection.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlltrRequest.from_dict(body)
    return web.Response(status=200)
