from typing import List, Dict
from aiohttp import web

from openapi_server.models.tdcer400_response import Tdcer400Response
from openapi_server.models.tdcer401_response import Tdcer401Response
from openapi_server.models.tdcer404_response import Tdcer404Response
from openapi_server.models.tdcer500_response import Tdcer500Response
from openapi_server.models.tdcer502_response import Tdcer502Response
from openapi_server.models.tdcer503_response import Tdcer503Response
from openapi_server.models.tdcer504_response import Tdcer504Response
from openapi_server.models.tdcer_request import TdcerRequest
from openapi_server import util


async def tdcer(request: web.Request, body=None) -> web.Response:
    """TDS Certificate

    API to verify TDS Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = TdcerRequest.from_dict(body)
    return web.Response(status=200)
