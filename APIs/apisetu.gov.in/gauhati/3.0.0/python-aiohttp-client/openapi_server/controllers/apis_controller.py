from typing import List, Dict
from aiohttp import web

from openapi_server.models.socer400_response import Socer400Response
from openapi_server.models.socer401_response import Socer401Response
from openapi_server.models.socer404_response import Socer404Response
from openapi_server.models.socer500_response import Socer500Response
from openapi_server.models.socer502_response import Socer502Response
from openapi_server.models.socer503_response import Socer503Response
from openapi_server.models.socer504_response import Socer504Response
from openapi_server.models.socer_request import SocerRequest
from openapi_server import util


async def socer(request: web.Request, body=None) -> web.Response:
    """Educational/ Exam Registration Certificate

    API to verify Educational/ Exam Registration Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = SocerRequest.from_dict(body)
    return web.Response(status=200)
