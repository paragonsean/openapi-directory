from typing import List, Dict
from aiohttp import web

from openapi_server.models.micer400_response import Micer400Response
from openapi_server.models.micer401_response import Micer401Response
from openapi_server.models.micer404_response import Micer404Response
from openapi_server.models.micer500_response import Micer500Response
from openapi_server.models.micer502_response import Micer502Response
from openapi_server.models.micer503_response import Micer503Response
from openapi_server.models.micer504_response import Micer504Response
from openapi_server.models.micer_request import MicerRequest
from openapi_server import util


async def micer(request: web.Request, body=None) -> web.Response:
    """Migration Certificate

    API to verify Migration Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = MicerRequest.from_dict(body)
    return web.Response(status=200)


async def pvcer(request: web.Request, body=None) -> web.Response:
    """Provisional Certificate

    API to verify Provisional Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = MicerRequest.from_dict(body)
    return web.Response(status=200)
