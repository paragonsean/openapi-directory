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
from openapi_server.models.regrii_request import RegriiRequest
from openapi_server import util


async def rdcer(request: web.Request, body=None) -> web.Response:
    """Copy of Registered Deed

    API to verify Copy of Registered Deed.

    :param body: Request format
    :type body: dict | bytes

    """
    body = RdcerRequest.from_dict(body)
    return web.Response(status=200)


async def regrii(request: web.Request, body=None) -> web.Response:
    """ROR Register 2

    API to verify ROR Register 2.

    :param body: Request format
    :type body: dict | bytes

    """
    body = RegriiRequest.from_dict(body)
    return web.Response(status=200)


async def rmcer(request: web.Request, body=None) -> web.Response:
    """Marriage Certificate

    API to verify Marriage Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = RegriiRequest.from_dict(body)
    return web.Response(status=200)
