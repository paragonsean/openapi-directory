from typing import List, Dict
from aiohttp import web

from openapi_server.models.alimw400_response import Alimw400Response
from openapi_server.models.alimw401_response import Alimw401Response
from openapi_server.models.alimw404_response import Alimw404Response
from openapi_server.models.alimw500_response import Alimw500Response
from openapi_server.models.alimw502_response import Alimw502Response
from openapi_server.models.alimw503_response import Alimw503Response
from openapi_server.models.alimw504_response import Alimw504Response
from openapi_server.models.alimw_request import AlimwRequest
from openapi_server import util


async def alimw(request: web.Request, body=None) -> web.Response:
    """Application for License for Inter State Migrant Workmen

    API to verify Application for License for Inter State Migrant Workmen.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlimwRequest.from_dict(body)
    return web.Response(status=200)


async def alsbl(request: web.Request, body=None) -> web.Response:
    """Application/ License for Boilers

    API to verify Application/ License for Boilers.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlimwRequest.from_dict(body)
    return web.Response(status=200)


async def alsfc(request: web.Request, body=None) -> web.Response:
    """Application/ License for Factory

    API to verify Application/ License for Factory.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlimwRequest.from_dict(body)
    return web.Response(status=200)


async def apptu(request: web.Request, body=None) -> web.Response:
    """Application realted to Trade Unions

    API to verify Application realted to Trade Unions.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlimwRequest.from_dict(body)
    return web.Response(status=200)


async def clcer(request: web.Request, body=None) -> web.Response:
    """Registration Certificate for Contract Labour License

    API to verify Registration Certificate for Contract Labour License.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlimwRequest.from_dict(body)
    return web.Response(status=200)


async def noocl(request: web.Request, body=None) -> web.Response:
    """Notice of Closure

    API to verify Notice of Closure.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlimwRequest.from_dict(body)
    return web.Response(status=200)


async def srcer(request: web.Request, body=None) -> web.Response:
    """Registration Certificate of Shops And Commercial Establishment

    API to verify Registration Certificate of Shops And Commercial Establishment.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AlimwRequest.from_dict(body)
    return web.Response(status=200)
