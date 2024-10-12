from typing import List, Dict
from aiohttp import web

from openapi_server.models.delcs400_response import Delcs400Response
from openapi_server.models.delcs401_response import Delcs401Response
from openapi_server.models.delcs404_response import Delcs404Response
from openapi_server.models.delcs500_response import Delcs500Response
from openapi_server.models.delcs502_response import Delcs502Response
from openapi_server.models.delcs503_response import Delcs503Response
from openapi_server.models.delcs504_response import Delcs504Response
from openapi_server.models.delcs_request import DelcsRequest
from openapi_server import util


async def delcs(request: web.Request, body=None) -> web.Response:
    """Dealer License

    API to verify Dealer License.

    :param body: Request format
    :type body: dict | bytes

    """
    body = DelcsRequest.from_dict(body)
    return web.Response(status=200)


async def malcs(request: web.Request, body=None) -> web.Response:
    """Manufacturer License

    API to verify Manufacturer License.

    :param body: Request format
    :type body: dict | bytes

    """
    body = DelcsRequest.from_dict(body)
    return web.Response(status=200)


async def palcs(request: web.Request, body=None) -> web.Response:
    """Packers License

    API to verify Packers License.

    :param body: Request format
    :type body: dict | bytes

    """
    body = DelcsRequest.from_dict(body)
    return web.Response(status=200)


async def relcs(request: web.Request, body=None) -> web.Response:
    """Repairer License

    API to verify Repairer License.

    :param body: Request format
    :type body: dict | bytes

    """
    body = DelcsRequest.from_dict(body)
    return web.Response(status=200)
