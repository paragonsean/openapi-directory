from typing import List, Dict
from aiohttp import web

from openapi_server.models.brlcs400_response import Brlcs400Response
from openapi_server.models.brlcs401_response import Brlcs401Response
from openapi_server.models.brlcs404_response import Brlcs404Response
from openapi_server.models.brlcs500_response import Brlcs500Response
from openapi_server.models.brlcs502_response import Brlcs502Response
from openapi_server.models.brlcs503_response import Brlcs503Response
from openapi_server.models.brlcs504_response import Brlcs504Response
from openapi_server.models.brlcs_request import BrlcsRequest
from openapi_server import util


async def brlcs(request: web.Request, body=None) -> web.Response:
    """Bar License

    API to verify Bar License.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BrlcsRequest.from_dict(body)
    return web.Response(status=200)


async def dpcer(request: web.Request, body=None) -> web.Response:
    """Dependency Certificate

    API to verify Dependency Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BrlcsRequest.from_dict(body)
    return web.Response(status=200)


async def fmcer(request: web.Request, body=None) -> web.Response:
    """Family Membership Certificate

    API to verify Family Membership Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BrlcsRequest.from_dict(body)
    return web.Response(status=200)


async def incer(request: web.Request, body=None) -> web.Response:
    """Income Certificate

    API to verify Income Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BrlcsRequest.from_dict(body)
    return web.Response(status=200)


async def lccep(request: web.Request, body=None) -> web.Response:
    """Local Candidate/ Status Certificate

    API to verify Local Candidate/ Status Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BrlcsRequest.from_dict(body)
    return web.Response(status=200)


async def ndcer(request: web.Request, body=None) -> web.Response:
    """No Dues/ Objection Certificate

    API to verify No Dues/ Objection Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BrlcsRequest.from_dict(body)
    return web.Response(status=200)


async def obcer(request: web.Request, body=None) -> web.Response:
    """OBC Certificate

    API to verify OBC Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BrlcsRequest.from_dict(body)
    return web.Response(status=200)


async def rmcer(request: web.Request, body=None) -> web.Response:
    """Marriage Certificate

    API to verify Marriage Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BrlcsRequest.from_dict(body)
    return web.Response(status=200)


async def rscer(request: web.Request, body=None) -> web.Response:
    """Residence Certificate

    API to verify Residence Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BrlcsRequest.from_dict(body)
    return web.Response(status=200)


async def rucer(request: web.Request, body=None) -> web.Response:
    """Regional Language(s) Certificate

    API to verify Regional Language(s) Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BrlcsRequest.from_dict(body)
    return web.Response(status=200)


async def sicrd(request: web.Request, body=None) -> web.Response:
    """Senior Citizen Identity Card/ Certificate

    API to verify Senior Citizen Identity Card/ Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BrlcsRequest.from_dict(body)
    return web.Response(status=200)


async def vlcer(request: web.Request, body=None) -> web.Response:
    """Valuation Certificate

    API to verify Valuation Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BrlcsRequest.from_dict(body)
    return web.Response(status=200)
