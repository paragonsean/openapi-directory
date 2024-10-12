from typing import List, Dict
from aiohttp import web

from openapi_server.models.rdcer400_response import Rdcer400Response
from openapi_server.models.rdcer401_response import Rdcer401Response
from openapi_server.models.rdcer404_response import Rdcer404Response
from openapi_server.models.rdcer500_response import Rdcer500Response
from openapi_server.models.rdcer502_response import Rdcer502Response
from openapi_server.models.rdcer503_response import Rdcer503Response
from openapi_server.models.rdcer504_response import Rdcer504Response
from openapi_server.models.rdcer_request import RdcerRequest
from openapi_server.models.ror1b_request import Ror1bRequest
from openapi_server import util


async def rdcer(request: web.Request, body=None) -> web.Response:
    """Copy of Registered Deed

    API to verify Copy of Registered Deed.

    :param body: Request format
    :type body: dict | bytes

    """
    body = RdcerRequest.from_dict(body)
    return web.Response(status=200)


async def ror1b(request: web.Request, body=None) -> web.Response:
    """Records of Rights

    API to verify Records of Rights.

    :param body: Request format
    :type body: dict | bytes

    """
    body = Ror1bRequest.from_dict(body)
    return web.Response(status=200)
