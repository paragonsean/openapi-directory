from typing import List, Dict
from aiohttp import web

from openapi_server.models.kecer400_response import Kecer400Response
from openapi_server.models.kecer401_response import Kecer401Response
from openapi_server.models.kecer404_response import Kecer404Response
from openapi_server.models.kecer500_response import Kecer500Response
from openapi_server.models.kecer502_response import Kecer502Response
from openapi_server.models.kecer503_response import Kecer503Response
from openapi_server.models.kecer504_response import Kecer504Response
from openapi_server.models.kecer_request import KecerRequest
from openapi_server.models.tapcn_request import TapcnRequest
from openapi_server.models.tdlcs_request import TdlcsRequest
from openapi_server import util


async def kecer(request: web.Request, body=None) -> web.Response:
    """Khatha Extract / Certificate

    API to verify Khatha Extract / Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = KecerRequest.from_dict(body)
    return web.Response(status=200)


async def tapcn(request: web.Request, body=None) -> web.Response:
    """New Tap Connection

    API to verify New Tap Connection.

    :param body: Request format
    :type body: dict | bytes

    """
    body = TapcnRequest.from_dict(body)
    return web.Response(status=200)


async def tdlcs(request: web.Request, body=None) -> web.Response:
    """Trade License/ Certificate

    API to verify Trade License/ Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = TdlcsRequest.from_dict(body)
    return web.Response(status=200)


async def ugdcn(request: web.Request, body=None) -> web.Response:
    """Jalanidhi - New UGD Connection

    API to verify Jalanidhi - New UGD Connection.

    :param body: Request format
    :type body: dict | bytes

    """
    body = TapcnRequest.from_dict(body)
    return web.Response(status=200)
