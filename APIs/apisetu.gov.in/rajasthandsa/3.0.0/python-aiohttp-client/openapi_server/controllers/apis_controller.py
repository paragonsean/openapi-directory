from typing import List, Dict
from aiohttp import web

from openapi_server.models.dpicr400_response import Dpicr400Response
from openapi_server.models.dpicr401_response import Dpicr401Response
from openapi_server.models.dpicr404_response import Dpicr404Response
from openapi_server.models.dpicr500_response import Dpicr500Response
from openapi_server.models.dpicr502_response import Dpicr502Response
from openapi_server.models.dpicr503_response import Dpicr503Response
from openapi_server.models.dpicr504_response import Dpicr504Response
from openapi_server.models.dpicr_request import DpicrRequest
from openapi_server import util


async def dpicr(request: web.Request, body=None) -> web.Response:
    """Disabled Person Identity Card/ Certificate

    API to verify Disabled Person Identity Card/ Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = DpicrRequest.from_dict(body)
    return web.Response(status=200)
