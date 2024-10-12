from typing import List, Dict
from aiohttp import web

from openapi_server.models.iticr400_response import Iticr400Response
from openapi_server.models.iticr401_response import Iticr401Response
from openapi_server.models.iticr404_response import Iticr404Response
from openapi_server.models.iticr500_response import Iticr500Response
from openapi_server.models.iticr502_response import Iticr502Response
from openapi_server.models.iticr503_response import Iticr503Response
from openapi_server.models.iticr504_response import Iticr504Response
from openapi_server.models.iticr_request import IticrRequest
from openapi_server import util


async def iticr(request: web.Request, body=None) -> web.Response:
    """ITI Certificate

    API to verify ITI Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = IticrRequest.from_dict(body)
    return web.Response(status=200)
