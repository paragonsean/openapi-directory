from typing import List, Dict
from aiohttp import web

from openapi_server.models.lpgsv400_response import Lpgsv400Response
from openapi_server.models.lpgsv401_response import Lpgsv401Response
from openapi_server.models.lpgsv404_response import Lpgsv404Response
from openapi_server.models.lpgsv500_response import Lpgsv500Response
from openapi_server.models.lpgsv502_response import Lpgsv502Response
from openapi_server.models.lpgsv503_response import Lpgsv503Response
from openapi_server.models.lpgsv504_response import Lpgsv504Response
from openapi_server.models.lpgsv_request import LpgsvRequest
from openapi_server import util


async def lpgsv(request: web.Request, body=None) -> web.Response:
    """LPG Subscription Voucher

    API to verify LPG Subscription Voucher.

    :param body: Request format
    :type body: dict | bytes

    """
    body = LpgsvRequest.from_dict(body)
    return web.Response(status=200)


async def lpgtv(request: web.Request, body=None) -> web.Response:
    """Termination Voucher

    API to verify Termination Voucher.

    :param body: Request format
    :type body: dict | bytes

    """
    body = LpgsvRequest.from_dict(body)
    return web.Response(status=200)
