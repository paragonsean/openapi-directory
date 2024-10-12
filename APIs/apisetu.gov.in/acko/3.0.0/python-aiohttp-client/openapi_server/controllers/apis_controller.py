from typing import List, Dict
from aiohttp import web

from openapi_server.models.cripc400_response import Cripc400Response
from openapi_server.models.cripc401_response import Cripc401Response
from openapi_server.models.cripc404_response import Cripc404Response
from openapi_server.models.cripc500_response import Cripc500Response
from openapi_server.models.cripc502_response import Cripc502Response
from openapi_server.models.cripc503_response import Cripc503Response
from openapi_server.models.cripc504_response import Cripc504Response
from openapi_server.models.cripc_request import CripcRequest
from openapi_server import util


async def cripc(request: web.Request, body=None) -> web.Response:
    """Insurance Policy - Car

    API to verify Insurance Policy - Car.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CripcRequest.from_dict(body)
    return web.Response(status=200)


async def hlipc(request: web.Request, body=None) -> web.Response:
    """Insurance Policy - Health

    API to verify Insurance Policy - Health.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CripcRequest.from_dict(body)
    return web.Response(status=200)


async def twipc(request: web.Request, body=None) -> web.Response:
    """Insurance Policy - Two Wheeler

    API to verify Insurance Policy - Two Wheeler.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CripcRequest.from_dict(body)
    return web.Response(status=200)
