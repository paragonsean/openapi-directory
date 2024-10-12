from typing import List, Dict
from aiohttp import web

from openapi_server.models.labrp400_response import Labrp400Response
from openapi_server.models.labrp401_response import Labrp401Response
from openapi_server.models.labrp404_response import Labrp404Response
from openapi_server.models.labrp500_response import Labrp500Response
from openapi_server.models.labrp502_response import Labrp502Response
from openapi_server.models.labrp503_response import Labrp503Response
from openapi_server.models.labrp504_response import Labrp504Response
from openapi_server.models.labrp_request import LabrpRequest
from openapi_server import util


async def labrp(request: web.Request, body=None) -> web.Response:
    """Clinical Laboratory Report

    API to verify Clinical Laboratory Report.

    :param body: Request format
    :type body: dict | bytes

    """
    body = LabrpRequest.from_dict(body)
    return web.Response(status=200)
