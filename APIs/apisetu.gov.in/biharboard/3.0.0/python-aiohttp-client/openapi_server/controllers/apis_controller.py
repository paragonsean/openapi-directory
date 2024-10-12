from typing import List, Dict
from aiohttp import web

from openapi_server.models.sscer400_response import Sscer400Response
from openapi_server.models.sscer401_response import Sscer401Response
from openapi_server.models.sscer404_response import Sscer404Response
from openapi_server.models.sscer500_response import Sscer500Response
from openapi_server.models.sscer502_response import Sscer502Response
from openapi_server.models.sscer503_response import Sscer503Response
from openapi_server.models.sscer504_response import Sscer504Response
from openapi_server.models.sscer_request import SscerRequest
from openapi_server import util


async def sscer(request: web.Request, body=None) -> web.Response:
    """Class X Marksheet

    API to verify Class X Marksheet.

    :param body: Request format
    :type body: dict | bytes

    """
    body = SscerRequest.from_dict(body)
    return web.Response(status=200)


async def svcer(request: web.Request, body=None) -> web.Response:
    """Class X Provisional Certificate

    API to verify Class X Provisional Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = SscerRequest.from_dict(body)
    return web.Response(status=200)
