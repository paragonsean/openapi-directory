from typing import List, Dict
from aiohttp import web

from openapi_server.models.mrcer400_response import Mrcer400Response
from openapi_server.models.mrcer401_response import Mrcer401Response
from openapi_server.models.mrcer404_response import Mrcer404Response
from openapi_server.models.mrcer500_response import Mrcer500Response
from openapi_server.models.mrcer502_response import Mrcer502Response
from openapi_server.models.mrcer503_response import Mrcer503Response
from openapi_server.models.mrcer504_response import Mrcer504Response
from openapi_server.models.mrcer_request import MrcerRequest
from openapi_server import util


async def mrcer(request: web.Request, body=None) -> web.Response:
    """Merit Certificate

    API to verify Merit Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = MrcerRequest.from_dict(body)
    return web.Response(status=200)
