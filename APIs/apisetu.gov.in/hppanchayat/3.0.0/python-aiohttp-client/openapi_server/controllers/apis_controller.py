from typing import List, Dict
from aiohttp import web

from openapi_server.models.fmcer400_response import Fmcer400Response
from openapi_server.models.fmcer401_response import Fmcer401Response
from openapi_server.models.fmcer404_response import Fmcer404Response
from openapi_server.models.fmcer500_response import Fmcer500Response
from openapi_server.models.fmcer502_response import Fmcer502Response
from openapi_server.models.fmcer503_response import Fmcer503Response
from openapi_server.models.fmcer504_response import Fmcer504Response
from openapi_server.models.fmcer_request import FmcerRequest
from openapi_server import util


async def fmcer(request: web.Request, body=None) -> web.Response:
    """Family Membership Certificate

    API to verify Family Membership Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = FmcerRequest.from_dict(body)
    return web.Response(status=200)
