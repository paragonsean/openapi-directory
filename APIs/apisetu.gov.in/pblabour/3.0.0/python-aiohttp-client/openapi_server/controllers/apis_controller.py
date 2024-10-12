from typing import List, Dict
from aiohttp import web

from openapi_server.models.alsfc400_response import Alsfc400Response
from openapi_server.models.alsfc401_response import Alsfc401Response
from openapi_server.models.alsfc404_response import Alsfc404Response
from openapi_server.models.alsfc500_response import Alsfc500Response
from openapi_server.models.alsfc502_response import Alsfc502Response
from openapi_server.models.alsfc503_response import Alsfc503Response
from openapi_server.models.alsfc504_response import Alsfc504Response
from openapi_server.models.alsfc_request import AlsfcRequest
from openapi_server import util


async def alsfc(request: web.Request, body=None) -> web.Response:
    """Application/ License for Factory

    API to verify Application/ License for Factory.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlsfcRequest.from_dict(body)
    return web.Response(status=200)


async def clcer(request: web.Request, body=None) -> web.Response:
    """Registration Certificate for Contract Labour License

    API to verify Registration Certificate for Contract Labour License.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlsfcRequest.from_dict(body)
    return web.Response(status=200)


async def srcer(request: web.Request, body=None) -> web.Response:
    """Registration Certificate of Shops And Commercial Establishment

    API to verify Registration Certificate of Shops And Commercial Establishment.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlsfcRequest.from_dict(body)
    return web.Response(status=200)
