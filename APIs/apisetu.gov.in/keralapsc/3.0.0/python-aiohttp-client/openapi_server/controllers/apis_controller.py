from typing import List, Dict
from aiohttp import web

from openapi_server.models.otcer400_response import Otcer400Response
from openapi_server.models.otcer401_response import Otcer401Response
from openapi_server.models.otcer404_response import Otcer404Response
from openapi_server.models.otcer500_response import Otcer500Response
from openapi_server.models.otcer502_response import Otcer502Response
from openapi_server.models.otcer503_response import Otcer503Response
from openapi_server.models.otcer504_response import Otcer504Response
from openapi_server.models.otcer_request import OtcerRequest
from openapi_server import util


async def otcer(request: web.Request, body=None) -> web.Response:
    """OTV Certificate

    API to verify OTV Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = OtcerRequest.from_dict(body)
    return web.Response(status=200)
