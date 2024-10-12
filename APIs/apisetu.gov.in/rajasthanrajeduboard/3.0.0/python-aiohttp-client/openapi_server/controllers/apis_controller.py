from typing import List, Dict
from aiohttp import web

from openapi_server.models.hscer400_response import Hscer400Response
from openapi_server.models.hscer401_response import Hscer401Response
from openapi_server.models.hscer404_response import Hscer404Response
from openapi_server.models.hscer500_response import Hscer500Response
from openapi_server.models.hscer502_response import Hscer502Response
from openapi_server.models.hscer503_response import Hscer503Response
from openapi_server.models.hscer504_response import Hscer504Response
from openapi_server.models.hscer_request import HscerRequest
from openapi_server.models.sscer_request import SscerRequest
from openapi_server import util


async def hscer(request: web.Request, body=None) -> web.Response:
    """Class XII Marksheet

    API to verify Class XII Marksheet.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HscerRequest.from_dict(body)
    return web.Response(status=200)


async def sscer(request: web.Request, body=None) -> web.Response:
    """Class X Marksheet

    API to verify Class X Marksheet.

    :param body: Request format
    :type body: dict | bytes

    """
    body = SscerRequest.from_dict(body)
    return web.Response(status=200)
