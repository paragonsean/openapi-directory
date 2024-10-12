from typing import List, Dict
from aiohttp import web

from openapi_server.models.epfsc400_response import Epfsc400Response
from openapi_server.models.epfsc401_response import Epfsc401Response
from openapi_server.models.epfsc404_response import Epfsc404Response
from openapi_server.models.epfsc500_response import Epfsc500Response
from openapi_server.models.epfsc502_response import Epfsc502Response
from openapi_server.models.epfsc503_response import Epfsc503Response
from openapi_server.models.epfsc504_response import Epfsc504Response
from openapi_server.models.epfsc_request import EpfscRequest
from openapi_server.models.pecer_request import PecerRequest
from openapi_server.models.uncrd_request import UncrdRequest
from openapi_server import util


async def epfsc(request: web.Request, body=None) -> web.Response:
    """Scheme Certificate

    API to verify Scheme Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = EpfscRequest.from_dict(body)
    return web.Response(status=200)


async def pecer(request: web.Request, body=None) -> web.Response:
    """Pension Certificate

    API to verify Pension Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = PecerRequest.from_dict(body)
    return web.Response(status=200)


async def uncrd(request: web.Request, body=None) -> web.Response:
    """UAN Card

    API to verify UAN Card.

    :param body: Request format
    :type body: dict | bytes

    """
    body = UncrdRequest.from_dict(body)
    return web.Response(status=200)
