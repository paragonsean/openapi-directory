from typing import List, Dict
from aiohttp import web

from openapi_server.models.licer400_response import Licer400Response
from openapi_server.models.licer401_response import Licer401Response
from openapi_server.models.licer404_response import Licer404Response
from openapi_server.models.licer500_response import Licer500Response
from openapi_server.models.licer502_response import Licer502Response
from openapi_server.models.licer503_response import Licer503Response
from openapi_server.models.licer504_response import Licer504Response
from openapi_server.models.licer_request import LicerRequest
from openapi_server import util


async def licer(request: web.Request, body=None) -> web.Response:
    """Insurance Policy - Life

    API to verify Insurance Policy - Life.

    :param body: Request format
    :type body: dict | bytes

    """
    body = LicerRequest.from_dict(body)
    return web.Response(status=200)
