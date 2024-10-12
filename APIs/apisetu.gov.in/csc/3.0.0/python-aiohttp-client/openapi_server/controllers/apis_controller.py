from typing import List, Dict
from aiohttp import web

from openapi_server.models.skcer400_response import Skcer400Response
from openapi_server.models.skcer401_response import Skcer401Response
from openapi_server.models.skcer404_response import Skcer404Response
from openapi_server.models.skcer500_response import Skcer500Response
from openapi_server.models.skcer502_response import Skcer502Response
from openapi_server.models.skcer503_response import Skcer503Response
from openapi_server.models.skcer504_response import Skcer504Response
from openapi_server.models.skcer_request import SkcerRequest
from openapi_server import util


async def skcer(request: web.Request, body=None) -> web.Response:
    """Skill Certificate

    API to verify Skill Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = SkcerRequest.from_dict(body)
    return web.Response(status=200)
