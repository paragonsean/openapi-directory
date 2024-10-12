from typing import List, Dict
from aiohttp import web

from openapi_server.models.vochse400_response import Vochse400Response
from openapi_server.models.vochse401_response import Vochse401Response
from openapi_server.models.vochse404_response import Vochse404Response
from openapi_server.models.vochse500_response import Vochse500Response
from openapi_server.models.vochse502_response import Vochse502Response
from openapi_server.models.vochse503_response import Vochse503Response
from openapi_server.models.vochse504_response import Vochse504Response
from openapi_server.models.vochse_request import VochseRequest
from openapi_server import util


async def vochse(request: web.Request, body=None) -> web.Response:
    """Vocational Higher Secondary

    API to verify Vocational Higher Secondary.

    :param body: Request format
    :type body: dict | bytes

    """
    body = VochseRequest.from_dict(body)
    return web.Response(status=200)
