from typing import List, Dict
from aiohttp import web

from openapi_server.models.pecer400_response import Pecer400Response
from openapi_server.models.pecer401_response import Pecer401Response
from openapi_server.models.pecer404_response import Pecer404Response
from openapi_server.models.pecer500_response import Pecer500Response
from openapi_server.models.pecer502_response import Pecer502Response
from openapi_server.models.pecer503_response import Pecer503Response
from openapi_server.models.pecer504_response import Pecer504Response
from openapi_server.models.pecer_request import PecerRequest
from openapi_server import util


async def pecer(request: web.Request, body=None) -> web.Response:
    """Pension Certificate

    API to verify Pension Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = PecerRequest.from_dict(body)
    return web.Response(status=200)


async def prfnd(request: web.Request, body=None) -> web.Response:
    """Provident Fund

    API to verify Provident Fund.

    :param body: Request format
    :type body: dict | bytes

    """
    body = PecerRequest.from_dict(body)
    return web.Response(status=200)
