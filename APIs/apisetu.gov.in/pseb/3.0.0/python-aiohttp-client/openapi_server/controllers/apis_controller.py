from typing import List, Dict
from aiohttp import web

from openapi_server.models.cemst400_response import Cemst400Response
from openapi_server.models.cemst401_response import Cemst401Response
from openapi_server.models.cemst404_response import Cemst404Response
from openapi_server.models.cemst500_response import Cemst500Response
from openapi_server.models.cemst502_response import Cemst502Response
from openapi_server.models.cemst503_response import Cemst503Response
from openapi_server.models.cemst504_response import Cemst504Response
from openapi_server.models.cemst_request import CemstRequest
from openapi_server import util


async def cemst(request: web.Request, body=None) -> web.Response:
    """Class VIII Marksheet

    API to verify Class VIII Marksheet.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CemstRequest.from_dict(body)
    return web.Response(status=200)


async def cfmst(request: web.Request, body=None) -> web.Response:
    """Class V Marksheet

    API to verify Class V Marksheet.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CemstRequest.from_dict(body)
    return web.Response(status=200)


async def hscer(request: web.Request, body=None) -> web.Response:
    """Class XII Marksheet

    API to verify Class XII Marksheet.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CemstRequest.from_dict(body)
    return web.Response(status=200)


async def micer(request: web.Request, body=None) -> web.Response:
    """Migration Certificate

    API to verify Migration Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CemstRequest.from_dict(body)
    return web.Response(status=200)


async def sscer(request: web.Request, body=None) -> web.Response:
    """Class X Marksheet

    API to verify Class X Marksheet.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CemstRequest.from_dict(body)
    return web.Response(status=200)
