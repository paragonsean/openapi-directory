from typing import List, Dict
from aiohttp import web

from openapi_server.models.ercer400_response import Ercer400Response
from openapi_server.models.ercer401_response import Ercer401Response
from openapi_server.models.ercer404_response import Ercer404Response
from openapi_server.models.ercer500_response import Ercer500Response
from openapi_server.models.ercer502_response import Ercer502Response
from openapi_server.models.ercer503_response import Ercer503Response
from openapi_server.models.ercer504_response import Ercer504Response
from openapi_server.models.ercer_request import ErcerRequest
from openapi_server import util


async def ercer(request: web.Request, body=None) -> web.Response:
    """Registration Certificate of Establishment Employing Contract Labour

    API to verify Registration Certificate of Establishment Employing Contract Labour.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ErcerRequest.from_dict(body)
    return web.Response(status=200)


async def pfdaw(request: web.Request, body=None) -> web.Response:
    """Permission/ Certificate for Well

    API to verify Permission/ Certificate for Well.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ErcerRequest.from_dict(body)
    return web.Response(status=200)


async def tpcer(request: web.Request, body=None) -> web.Response:
    """Permission/ Certificate for Transportation (Petroleum Products, Water etc.)

    API to verify Permission/ Certificate for Transportation (Petroleum Products, Water etc.).

    :param body: Request format
    :type body: dict | bytes

    """
    body = ErcerRequest.from_dict(body)
    return web.Response(status=200)
