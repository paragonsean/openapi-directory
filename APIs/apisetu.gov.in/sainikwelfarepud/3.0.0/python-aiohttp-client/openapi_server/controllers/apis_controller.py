from typing import List, Dict
from aiohttp import web

from openapi_server.models.dpcer400_response import Dpcer400Response
from openapi_server.models.dpcer401_response import Dpcer401Response
from openapi_server.models.dpcer404_response import Dpcer404Response
from openapi_server.models.dpcer500_response import Dpcer500Response
from openapi_server.models.dpcer502_response import Dpcer502Response
from openapi_server.models.dpcer503_response import Dpcer503Response
from openapi_server.models.dpcer504_response import Dpcer504Response
from openapi_server.models.dpcer_request import DpcerRequest
from openapi_server import util


async def dpcer(request: web.Request, body=None) -> web.Response:
    """Dependency Certificate

    API to verify Dependency Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = DpcerRequest.from_dict(body)
    return web.Response(status=200)
