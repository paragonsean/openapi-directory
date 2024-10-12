from typing import List, Dict
from aiohttp import web

from openapi_server.models.hvcer400_response import Hvcer400Response
from openapi_server.models.hvcer401_response import Hvcer401Response
from openapi_server.models.hvcer404_response import Hvcer404Response
from openapi_server.models.hvcer500_response import Hvcer500Response
from openapi_server.models.hvcer502_response import Hvcer502Response
from openapi_server.models.hvcer503_response import Hvcer503Response
from openapi_server.models.hvcer504_response import Hvcer504Response
from openapi_server.models.hvcer_request import HvcerRequest
from openapi_server import util


async def hvcer(request: web.Request, body=None) -> web.Response:
    """Class XII Provisional Certificate

    API to verify Class XII Provisional Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HvcerRequest.from_dict(body)
    return web.Response(status=200)


async def svcer(request: web.Request, body=None) -> web.Response:
    """Class X Provisional Certificate

    API to verify Class X Provisional Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HvcerRequest.from_dict(body)
    return web.Response(status=200)
