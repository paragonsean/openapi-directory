from typing import List, Dict
from aiohttp import web

from openapi_server.models.etcer400_response import Etcer400Response
from openapi_server.models.etcer401_response import Etcer401Response
from openapi_server.models.etcer404_response import Etcer404Response
from openapi_server.models.etcer500_response import Etcer500Response
from openapi_server.models.etcer502_response import Etcer502Response
from openapi_server.models.etcer503_response import Etcer503Response
from openapi_server.models.etcer504_response import Etcer504Response
from openapi_server.models.etcer_request import EtcerRequest
from openapi_server.models.govid_request import GovidRequest
from openapi_server.models.sicer_request import SicerRequest
from openapi_server import util


async def etcer(request: web.Request, body=None) -> web.Response:
    """Enlistment Certificate

    API to verify Enlistment Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = EtcerRequest.from_dict(body)
    return web.Response(status=200)


async def govid(request: web.Request, body=None) -> web.Response:
    """ID Card

    API to verify ID Card.

    :param body: Request format
    :type body: dict | bytes

    """
    body = GovidRequest.from_dict(body)
    return web.Response(status=200)


async def sicer(request: web.Request, body=None) -> web.Response:
    """Sanction Letter/ Certificate

    API to verify Sanction Letter/ Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = SicerRequest.from_dict(body)
    return web.Response(status=200)
