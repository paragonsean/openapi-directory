from typing import List, Dict
from aiohttp import web

from openapi_server.models.phcer400_response import Phcer400Response
from openapi_server.models.phcer401_response import Phcer401Response
from openapi_server.models.phcer404_response import Phcer404Response
from openapi_server.models.phcer500_response import Phcer500Response
from openapi_server.models.phcer502_response import Phcer502Response
from openapi_server.models.phcer503_response import Phcer503Response
from openapi_server.models.phcer504_response import Phcer504Response
from openapi_server.models.phcer_request import PhcerRequest
from openapi_server.models.rpcer_request import RpcerRequest
from openapi_server import util


async def phcer(request: web.Request, body=None) -> web.Response:
    """Pharmacist Registration Certificate

    API to verify Pharmacist Registration Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = PhcerRequest.from_dict(body)
    return web.Response(status=200)


async def rpcer(request: web.Request, body=None) -> web.Response:
    """Pharmacist Renewal certificate

    API to verify Pharmacist Renewal certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = RpcerRequest.from_dict(body)
    return web.Response(status=200)
