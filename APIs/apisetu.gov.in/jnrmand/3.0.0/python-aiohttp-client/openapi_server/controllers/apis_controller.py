from typing import List, Dict
from aiohttp import web

from openapi_server.models.trcer400_response import Trcer400Response
from openapi_server.models.trcer401_response import Trcer401Response
from openapi_server.models.trcer404_response import Trcer404Response
from openapi_server.models.trcer500_response import Trcer500Response
from openapi_server.models.trcer502_response import Trcer502Response
from openapi_server.models.trcer503_response import Trcer503Response
from openapi_server.models.trcer504_response import Trcer504Response
from openapi_server.models.trcer_request import TrcerRequest
from openapi_server import util


async def trcer(request: web.Request, body=None) -> web.Response:
    """Transfer Certificate

    API to verify Transfer Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = TrcerRequest.from_dict(body)
    return web.Response(status=200)
