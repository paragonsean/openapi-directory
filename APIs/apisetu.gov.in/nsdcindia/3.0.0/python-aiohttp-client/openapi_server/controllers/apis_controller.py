from typing import List, Dict
from aiohttp import web

from openapi_server.models.escer400_response import Escer400Response
from openapi_server.models.escer401_response import Escer401Response
from openapi_server.models.escer404_response import Escer404Response
from openapi_server.models.escer500_response import Escer500Response
from openapi_server.models.escer502_response import Escer502Response
from openapi_server.models.escer503_response import Escer503Response
from openapi_server.models.escer504_response import Escer504Response
from openapi_server.models.escer_request import EscerRequest
from openapi_server.models.skcer_request import SkcerRequest
from openapi_server import util


async def escer(request: web.Request, body=None) -> web.Response:
    """Executive Skill Enhancement Certificate

    API to verify Executive Skill Enhancement Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = EscerRequest.from_dict(body)
    return web.Response(status=200)


async def skcer(request: web.Request, body=None) -> web.Response:
    """Skill Certificate

    API to verify Skill Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = SkcerRequest.from_dict(body)
    return web.Response(status=200)
