from typing import List, Dict
from aiohttp import web

from openapi_server.models.sslcr400_response import Sslcr400Response
from openapi_server.models.sslcr401_response import Sslcr401Response
from openapi_server.models.sslcr404_response import Sslcr404Response
from openapi_server.models.sslcr500_response import Sslcr500Response
from openapi_server.models.sslcr502_response import Sslcr502Response
from openapi_server.models.sslcr503_response import Sslcr503Response
from openapi_server.models.sslcr504_response import Sslcr504Response
from openapi_server.models.sslcr_request import SslcrRequest
from openapi_server import util


async def sslcr(request: web.Request, body=None) -> web.Response:
    """Class X School Leaving Certificate

    API to verify Class X School Leaving Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = SslcrRequest.from_dict(body)
    return web.Response(status=200)
