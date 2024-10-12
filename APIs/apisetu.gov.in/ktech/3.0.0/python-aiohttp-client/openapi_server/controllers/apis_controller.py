from typing import List, Dict
from aiohttp import web

from openapi_server.models.cocer400_response import Cocer400Response
from openapi_server.models.cocer401_response import Cocer401Response
from openapi_server.models.cocer404_response import Cocer404Response
from openapi_server.models.cocer500_response import Cocer500Response
from openapi_server.models.cocer502_response import Cocer502Response
from openapi_server.models.cocer503_response import Cocer503Response
from openapi_server.models.cocer504_response import Cocer504Response
from openapi_server.models.cocer_request import CocerRequest
from openapi_server import util


async def cocer(request: web.Request, body=None) -> web.Response:
    """Company Related Certificate

    API to verify Company Related Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CocerRequest.from_dict(body)
    return web.Response(status=200)


async def rfcer(request: web.Request, body=None) -> web.Response:
    """Registration Certificate of Firm/ Company

    API to verify Registration Certificate of Firm/ Company.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CocerRequest.from_dict(body)
    return web.Response(status=200)
